from flask_classful import FlaskView, route
from flask import jsonify, request
from authorization.jwt_verification import jwt_verification
from service.analytics_service import AnalyticsService


class AnalyticsControllerView(FlaskView):
    analytics_service = AnalyticsService()

    def index(self):
        return jsonify(message="invalid api, bad request"), 400

    @route('/candidate/activities', methods=['POST'])
    # @jwt_verification # For production
    # def evaluate_candidate_activities(self, decoded_jwt):
    #     keycloak_id = decoded_jwt['sub']
    def evaluate_candidate_activities(self):  # For Development
        keycloak_id = request.json['keyCloakId']
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        result = self.analytics_service.retrieve_candidate_activities(keycloak_id=keycloak_id)

        return result, 202

    @route('/candidate/jobs', methods=['POST'])
    # @jwt_verification # For production
    # def evaluate_considered_jobs(self, decoded_jwt):
    #     keycloak_id = decoded_jwt['sub']
    def evaluate_considered_jobs(self):  # For Development
        keycloak_id = request.json['keyCloakId']
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        result = self.analytics_service.retrieve_considered_jobs(keycloak_id=keycloak_id)
        return result, 202

    @route('/hr/activities', methods=['POST'])
    # @jwt_verification # For production
    # def evaluate_hr_hirings(self, decoded_jwt):
    #     keycloak_id = decoded_jwt['sub']
    def evaluate_hr_hirings(self):  # For Development
        keycloak_id = request.json['keyCloakId']
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('limit', 25, type=int)
        category = request.args.get('category')
        if keycloak_id is None:
            return jsonify(message="Keycloak_id can't be empty"), 402
        if category == 'IN_PROGRESS':
            result = self.analytics_service.evaluate_hirings_in_progress(keycloak_id=keycloak_id,
                                                                         page=page,
                                                                         per_page=per_page)
        else:
            result = self.analytics_service.evaluate_hirings_in_last_month(keycloak_id=keycloak_id,
                                                                           page=page,
                                                                           per_page=per_page)
        return result, 202
