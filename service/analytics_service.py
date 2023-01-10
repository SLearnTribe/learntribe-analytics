import json
from flask import jsonify
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from converters.analytics_converter import AnalyticsConverter
from dataaccess.entity.othersBusiness import OthersBusiness
from dataaccess.entity.userObReltn import UserObReltn
from dataaccess.othersBusinessRepository import find_all_by_id, find_by_user_id, find_by_user_id_and_current_date
from models.response.candidatea_ctivities_response import CandidateActivitiesResponse
from dataaccess.userAstReltnRepository import count_by_user_id_and_filter
from dataaccess.userObReltnRepository import count_by_user_id_and_status, find_by_user_id_and_status
from models.response.hr_hiriing_response import HrHiringsResponse


class AnalyticsService:

    def create_hiring_response(self, others_business: OthersBusiness, hiring_status: str):
        job_count = (
            UserObReltn.query
            .filter(
                and_(UserObReltn.others_business_id == others_business.id, UserObReltn.hiring_status == hiring_status))
            .count()
        )

        if job_count > 0:
            return AnalyticsConverter.to_response(others_business, job_count)

        return HrHiringsResponse()

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

    def evaluate_hirings_in_progress(self, keycloak_id: str, page: int, per_page: int):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        created_jobs = find_by_user_id(user_id=keycloak_id, page=page, per_page=per_page)

        responses = []
        for job in created_jobs:
            response = self.create_hiring_response(job, "IN_PROGRESS")
            # job_count = UserObReltnRepository.query.filter_by(job_id=job.id, hiring_status="IN_PROGRESS").count()
            if response.job_count > 0:
                responses.append(response)

        return jsonify(responses)

    def evaluate_hirings_in_last_month(self, keycloak_id: str, page: int, per_page: int):
        if keycloak_id is None:
            return jsonify({"error": "User Id cannot be null"})

        created_jobs = (OthersBusiness.query
                        # .options(joinedload(OthersBusiness.user_ob_reltns))
                        .filter(and_(OthersBusiness.user_id == keycloak_id, OthersBusiness.current_date.isnot(None)))
                        .paginate(page=page, per_page=per_page)
                        .items
                        )
        created_jobs = find_by_user_id_and_current_date(user_id=keycloak_id,
                                                        page=page,
                                                        per_page=per_page)

        responses = []
        for job in created_jobs:
            response = self.create_hiring_response(job, "HIRED")
            if response.job_count > 0:
                responses.append(response)

        return jsonify({"hiring_responses": responses})
