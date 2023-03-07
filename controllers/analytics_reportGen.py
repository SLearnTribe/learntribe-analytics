from flask_classful import FlaskView,route
from service.analytics_service import AnalyticsService
from flask import jsonify
from authorization.jwt_verification import jwt_verification

class AnalyticsReportGen(FlaskView):
    analytics_service = AnalyticsService()

    def index(self):
        return jsonify(message="Invalid api, bad request"), 400

    @route('/candidate/genReport', methods=['GET'])
    @jwt_verification
    def evaluate_candidate_activities(self, keycloak_id):  # For Development
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        result = self.analytics_service.retrieve_candidate_activities(keycloak_id=keycloak_id)

        return result, 202