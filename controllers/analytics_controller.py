from flask_classful import FlaskView, route
from flask import jsonify, request

from service.analytics_service import AnalyticsService


class AnalyticsControllerView(FlaskView):
    analytics_service = AnalyticsService()

    def index(self):
        return jsonify(message="invalid api, bad request"), 400

    @route('/candidate/activities', methods=['POST'])
    def evaluate_candidate_activities(self):
        keycloak_id = request.json['keyCloakId']
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        result = self.analytics_service.retrieve_candidate_activities(keycloak_id=keycloak_id)

        return result, 202

    @route('/candidate/jobs', methods=['POST'])
    def evaluate_considered_jobs(self):
        keycloak_id = request.json['keyCloakId']
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        result = self.analytics_service.retrieve_considered_jobs(keycloak_id=keycloak_id)
        return result, 202

    @route('/hr/activities', methods=['POST'])
    def evaluate_hr_hirings(self):
        keycloak_id = request.json['keyCloakId']
        page = request.args['page']
        limit = request.args['limit']
        category = request.args['category']
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        if category == 'IN_PROGRESS':
            result = self.analytics_service.evaluate_hirings_in_progress(keycloak_id=keycloak_id)
        else:
            result = self.analytics_service.evaluate_hirings_in_last_month(keycloak_id=keycloak_id)
        return result, 202