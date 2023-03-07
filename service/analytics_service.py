import json
from flask import jsonify
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from converters.analytics_converter import AnalyticsConverter
from dataaccess.entity.othersBusiness import OthersBusiness
from dataaccess.entity.userObReltn import UserObReltn
from dataaccess.othersBusinessRepository import find_all_by_id, find_by_user_id, find_by_user_id_and_current_date
from models.response.candidate_activities_response import CandidateActivitiesResponse
from dataaccess.userAstReltnRepository import count_by_user_id_and_filter
from dataaccess.userObReltnRepository import count_by_user_id_and_status, find_by_user_id_and_status, \
    count_by_job_hiring_status
from models.response.hr_hiriing_response import HrHiringsResponse, HrHiringsResponseSchema

hr_hiring_response_schema = HrHiringsResponseSchema()
hr_hiring_response_schemas = HrHiringsResponseSchema(many=True)


class AnalyticsService:

    def create_hiring_response(self, others_business: OthersBusiness, hiring_status: str):
        # print("Rahul")
        print(others_business.id)
        job_count = count_by_job_hiring_status(job_id=others_business.id,
                                               hiring_status=hiring_status)
        # job_count = (
        #     UserObReltn.query
        #     .filter(
        #         and_(UserObReltn.others_business_id == others_business.id, UserObReltn.hiring_status == hiring_status))
        #     .count()
        # )
        print(job_count)
        if job_count > 0:
            return AnalyticsConverter.to_response(others_business=others_business,
                                                  job_count=job_count)

        return HrHiringsResponse()

    def retrieve_candidate_activities(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        completed_assessments = count_by_user_id_and_filter(keycloak_id=keycloak_id,
                                                            status="COMPLETED")
        jobs_applied = count_by_user_id_and_status(keycloak_id=keycloak_id,
                                                   hiring_status="IN_PROGRESS")
        # return jsonify(jobsApplied)

        candidate_activities_response = CandidateActivitiesResponse(completed=completed_assessments,
                                                                    jobs_applied=jobs_applied,
                                                                    interview_scheduled=0)
        return json.dumps(candidate_activities_response.__dict__)

    def retrieve_considered_jobs(self, keycloak_id: str):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        in_progress = find_by_user_id_and_status(keycloak_id=keycloak_id,
                                                 hiring_status="IN_PROGRESS")
        # print(in_progress)

        '''take out job_id from above result'''
        job_ids = tuple(job_id['id'] for job_id in in_progress)
        print(job_ids)
        # job_ids = (95, 140)   For Test purpose
        result = find_all_by_id(job_ids=job_ids)
        return jsonify(result)

    def evaluate_hirings_in_progress(self, keycloak_id: str, page: int, per_page: int):
        if keycloak_id is None:
            return jsonify(message="Keycloak_Id cannot be null"), 402

        created_jobs = find_by_user_id(user_id=keycloak_id, page=page, per_page=per_page)
        print(created_jobs)
        responses = []
        # if created_jobs[1] == 404:
        #     return jsonify(responses)
        for job in created_jobs:
            response = self.create_hiring_response(job, "IN_PROGRESS")
            # job_count = UserObReltnRepository.query.filter_by(job_id=job.id, hiring_status="IN_PROGRESS").count()
            if response.job_count > 0:
                result = hr_hiring_response_schema.dump(response)
                responses.append(result)
        print(responses)
        return jsonify(responses)

    def evaluate_hirings_in_last_month(self, keycloak_id: str, page: int, per_page: int):
        if keycloak_id is None:
            return jsonify({"error": "User Id cannot be null"})

        created_jobs = find_by_user_id_and_current_date(user_id=keycloak_id,
                                                        page=page,
                                                        per_page=per_page)

        responses = []
        for job in created_jobs:
            response = self.create_hiring_response(job, "HIRED")
            if response.job_count > 0:
                responses.append(response)

        return jsonify({"hiring_responses": responses})
