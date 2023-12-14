from flask import Flask
from controllers.users import *


def test_get_users_success(mocker):
    mocker.patch('api.controllers.user.findAll', return_value=['user1', 'user2'])
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    response = app.test_client().get('/api/users')
    assert response.status_code == 200
    assert response.json == {'data': ['user1', 'user2']}
