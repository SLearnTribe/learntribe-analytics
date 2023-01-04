import json

from flask_classful import FlaskView, route
from flask import jsonify, request, Flask
from flask_jwt_extended import jwt_required
from flask_oidc import OpenIDConnect

from service.analytics_service import AnalyticsService

from okta_jwt_verifier import AccessTokenVerifier, JWTVerifier
import asyncio







oidc = OpenIDConnect()


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

        return jsonify(result=result), 200

    @route('/candidate/jobs')
    def evaluate_considered_jobs(self):
        return

    @route('/hr/activities')
    def evaluate_hr_hirings(self):
        return
