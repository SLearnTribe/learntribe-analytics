import json
from flask import jsonify

from dataaccess.entity.othersBusiness import UserBusiness
from dataaccess.othersBusinessRepository import find_all_by_id, find_by_user_id
from models.response.candidatea_ctivities_response import CandidateActivitiesResponse
from dataaccess.userAstReltnRepository import count_by_user_id_and_filter
from dataaccess.userObReltnRepository import count_by_user_id_and_status, find_by_user_id_and_status


class AnalyticsService:
    def retrieve_candidate_activities(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        completed_assessments = count_by_user_id_and_filter(keycloak_id=keycloak_id, status="COMPLETED")
        interview_calls = count_by_user_id_and_status(keycloak_id=keycloak_id, hiring_status="IN_PROGRESS")
        # return jsonify(interview_calls)

        candidate_activities_response = CandidateActivitiesResponse(completed=completed_assessments,
                                                                    interview_calls=interview_calls,
                                                                    jobs_applied=0)
        return json.dumps(candidate_activities_response.__dict__)

    def retrieve_considered_jobs(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        '''TODO : Pending serialization of enum'''
        in_progress = find_by_user_id_and_status(keycloak_id=keycloak_id, hiring_status="IN_PROGRESS")
        '''take out job_id from above result'''
        job_id = None
        result = find_all_by_id(job_id=job_id)
        return result

    def evaluate_hirings_in_progress(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        created_jobs = find_by_user_id(user_id=keycloak_id)
        return result

    def evaluate_hirings_in_last_month(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        created_jobs = find_by_user_id(user_id=keycloak_id)
        return result

    def create_hr_hirings_response(self, othr_buss_resp: UserBusiness):
