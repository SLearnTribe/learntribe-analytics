from dataaccess.entity.othersBusiness import OthersBusiness
from models.response.hr_hiriing_response import HrHiringsResponse
from util import commons
from util.commons import Commons


class AnalyticsConverter:
    def __init__(self):
        self.commons = Commons()

    def to_response(self, others_business: OthersBusiness, job_count: int) -> HrHiringsResponse:
        response = HrHiringsResponse()
        response.job_title = others_business.title
        response.skills = others_business.requiredSkills
        if others_business.createdDate:
            response.job_posted_on = self.commons.format_instant(others_business.created_date)
        if others_business.status:
            response.job_status = others_business.JobStatus.name
        response.job_count = job_count
        response.business_name = others_business.businessName
        if others_business.employment_type:
            response.employment_type = others_business.employment_type.name
        return response
