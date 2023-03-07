from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

ma = Marshmallow()


class HrHiringsResponse:
    businessName = ""
    employmentType = ""
    jobTitle = ""
    skills = ""
    jobPostedOn = ""
    jobStatus = ""
    jobCount = 0

    def __init__(self):
        self.businessName = ""
        self.employmentType = ""
        self.jobTitle = ""
        self.skills = ""
        self.jobPostedOn = ""
        self.jobStatus = ""
        self.jobCount = 0

    # def __getattr__(self, name: str):
    #     return self.__dict__[f"{name}"]
    #
    # def __setattr__(self, name: str, value):
    #     self.__dict__[f"{name}"] = value


    # @property
    # def businessName(self):
    #     return self.businessName
    #
    # @businessName.setter
    # def businessName(self, value):
    #     self.businessName = value
    #
    # @property
    # def employmentType(self):
    #    return self.employmentType
    # 
    # @employmentType.setter
    # def employmnetType(self,value):
    #    self.employmentType = value 
    #
    # @property
    # def jobTitle(self):
    #     return self.jobTitle
    #
    # @jobTitle.setter
    # def jobTitle(self, value):
    #     self.jobTitle = value
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
    # def jobPostedOn(self):
    #     return self.jobPostedOn
    #
    # @jobPostedOn.setter
    # def jobPostedOn(self, value):
    #     self.jobPostedOn = value
    #
    # @property
    # def jobStatus(self):
    #     return self.jobStatus
    #
    # @jobStatus.setter
    # def jobStatus(self, value):
    #     self.jobStatus = value
    #
    # @property
    # def jobCount(self):
    #     return self.jobCount
    #
    # @jobCount.setter
    # def jobCount(self, value):
    #     self.jobCount = value


class HrHiringsResponseSchema(ma.Schema):
    class Meta:
        fields = ('employmentType', 'businessName' ,'jobTitle', 'skills', 'jobPostedOn', 'jobStatus', 'jobCount')
