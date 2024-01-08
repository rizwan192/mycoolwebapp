from flask_restx import Api

from project.controllers.status import health_check_namespace

api = Api(version="1.0", title="My cool web app",
          prefix="/api/v1", doc="/docs")

api.add_namespace(health_check_namespace, path="/_status")
