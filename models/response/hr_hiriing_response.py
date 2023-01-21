from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

ma = Marshmallow()


class HrHiringsResponse:
    job_title = ""
    skills = ""
    job_posted_on = ""
    job_status = ""
    job_count = 0

    def __init__(self):
        self.job_title = ""
        self.skills = ""
        self.job_posted_on = ""
        self.job_status = ""
        self.job_count = 0

    # def __getattr__(self, name: str):
    #     return self.__dict__[f"{name}"]
    #
    # def __setattr__(self, name: str, value):
    #     self.__dict__[f"{name}"] = value

    # @property
    # def job_title(self):
    #     return self.job_title
    #
    # @job_title.setter
    # def job_title(self, value):
    #     self.job_title = value
    #
    # @property
    # def skills(self):
    #     return self.skills
    #
    # @skills.setter
    # def skills(self, value):
    #     self.skills = value
    #
    # @property
    # def job_posted_on(self):
    #     return self.job_posted_on
    #
    # @job_posted_on.setter
    # def job_posted_on(self, value):
    #     self.job_posted_on = value
    #
    # @property
    # def job_status(self):
    #     return self.job_status
    #
    # @job_status.setter
    # def job_status(self, value):
    #     self.job_status = value
    #
    # @property
    # def job_count(self):
    #     return self.job_count
    #
    # @job_count.setter
    # def job_count(self, value):
    #     self.job_count = value


class HrHiringsResponseSchema(ma.Schema):
    class Meta:
        fields = ('job_title', 'skills', 'job_posted_on', 'job_status', 'job_count')
