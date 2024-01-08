from flask_restx import Namespace, Resource, fields
from flask import jsonify, make_response

health_check_namespace = Namespace("health_check")

class HealthCheck(Resource):
    def get(self):
        response = {}
        response["status"] = "OK."
        return make_response(jsonify(response), 200)

health_check_namespace.add_resource(HealthCheck, "")
