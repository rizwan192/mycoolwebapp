import logging
import os

from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app():
    app = Flask(__name__)

    app.logger.setLevel(logging.INFO)
    cors.init_app(app)

    from project.controllers import api
    api.init_app(app)

    return app
