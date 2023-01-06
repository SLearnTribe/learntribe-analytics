from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models.enums.employmentType import EmploymentType
from models.enums.jobStatus import JobStatus

db = SQLAlchemy()
ma = Marshmallow()


class UserBusiness(db.Model):
    __tablename__ = 'OTHERS_BUSINESS'
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    title = db.Column("title", db.LargeBinary)
    description = db.Column("description", db.LargeBinary)
    rolesAndResponsibilities = db.Column("rolesAndResponsibilities", db.LargeBinary)
    qualificationRequired = db.Column("qualificationRequired", db.LargeBinary)
    requiredSkills = db.Column("requiredSkills", db.LargeBinary)
    experienceRequired = db.Column("experienceRequired", db.Integer)
    createdBy = db.Column("createdBy", db.String)
    businessName = db.Column("businessName", db.String)
    location = db.Column("location", db.String)
    createdDate = db.Column("createdDate", db.DateTime, default=datetime.utcnow())
    JobStatus = db.Column("JobStatus", db.Enum(JobStatus))
    employmentType = db.Column("employmentType", db.Enum(EmploymentType))

    def __repr__(self):
        return f'<User {self.id}>'


class UserBusinessSchema(ma.Schema):
    class Meta:
        fields = ("id",
                  "title",
                  "description",
                  "rolesAndResponsibilities",
                  "qualificationRequired",
                  "requiredSkills",
                  "experienceRequired",
                  "createdBy",
                  "businessName",
                  "location",
                  "createdDate",
                  "JobStatus",
                  "employmentType")
