
from flask import Flask

from api.controllers.users import users_bp, get_users


def test_get_users_success(mocker):
    # Mock the findAll function to return some data
    mocker.patch('api.controllers.user.findAll', return_value=['user1', 'user2'])

    app = Flask(__name__)
    app.register_blueprint(users_bp)

    # Use the test client to simulate a GET request to /api/users
    response = app.test_client().get('/api/users')

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that the response data matches the expected data
    assert response.json == {'data': ['user1', 'user2'], 'single': False}

def test_get_users_failure(mocker):
    # Mock the findAll function to raise an exception
    mocker.patch('api.controllers.user.findAll', side_effect=Exception('Some error'))

    # Create a Flask test client
    app = Flask(__name__)
    app.register_blueprint(users_bp)

    # Use the test client to simulate a GET request to /api/users
    response = app.test_client().get('/api/users')

    # Assert that the response status code is 404
    assert response.status_code == 404

    # Assert that the response data contains the error message
    assert response.json == {'message': 'Some error', 'status_code': 404}
