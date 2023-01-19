from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from marshmallow_enum import EnumField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models.enums.employmentType import EmploymentType
from models.enums.jobStatus import JobStatus

db = SQLAlchemy()
ma = Marshmallow()


class OthersBusiness(db.Model):
    __tablename__ = 'OTHERS_BUSINESS'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=None))
    description = db.Column(db.String(length=None))
    rolesAndResponsibilities = db.Column(db.String(length=None))
    qualificationRequired = db.Column(db.String(length=None))
    requiredSkills = db.Column(db.String(length=None))
    experienceRequired = db.Column(db.Integer)
    createdBy = db.Column(db.String(length=None))
    businessName = db.Column(db.String(length=None))
    location = db.Column(db.String(length=None))
    createdDate = db.Column(db.DateTime)
    JobStatus = db.Column(db.Enum(JobStatus))
    employmentType = db.Column(db.Enum(EmploymentType))

    # id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    # title = db.Column("title", db.LargeBinary)
    # description = db.Column("description", db.LargeBinary)
    # rolesAndResponsibilities = db.Column("rolesAndResponsibilities", db.LargeBinary)
    # qualificationRequired = db.Column("qualificationRequired", db.LargeBinary)
    # requiredSkills = db.Column("requiredSkills", db.LargeBinary)
    # experienceRequired = db.Column("experienceRequired", db.Integer)
    # createdBy = db.Column("createdBy", db.String)
    # businessName = db.Column("businessName", db.String)
    # location = db.Column("location", db.String)
    # createdDate = db.Column("createdDate", db.DateTime, default=datetime.utcnow())
    # JobStatus = db.Column("JobStatus", db.Enum(JobStatus))
    # employmentType = db.Column("employmentType", db.Enum(EmploymentType))

    def __repr__(self):
        return f'<User {self.id}>'


class OthersBusinessSchema(ma.Schema):
    class Meta:
        model = OthersBusiness

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    rolesAndResponsibilities = fields.String()
    qualificationRequired = fields.String()
    requiredSkills = fields.String()
    experienceRequired = fields.Integer()
    createdBy = fields.String()
    businessName = fields.String()
    location = fields.String()
    createdDate = fields.DateTime()
    JobStatus = EnumField(enum=JobStatus)
    employmentType = EnumField(enum=EmploymentType)

    # id = ma.fields.Int(required=True)
    # title = ma.fields.Str()
    # description = ma.fields.Str()
    # rolesAndResponsibilities = ma.fields.Str()
    # qualificationRequired = ma.fields.Str()
    # requiredSkills = ma.fields.Str()
    # experienceRequired = ma.fields.Int()
    # createdBy = ma.fields.Str()
    # businessName = ma.fields.Str()
    # location = ma.fields.Str()
    # createdDate = ma.fields.DateTime()
    # JobStatus = ma.fields.Enum("JobStatus")
    # employmentType = ma.fields.Enum("EmploymentType")
    # fields = ("id",
    #           "title",
    #           "description",
    #           "rolesAndResponsibilities",
    #           "qualificationRequired",
    #           "requiredSkills",
    #           "experienceRequired",
    #           "createdBy",
    #           "businessName",
    #           "location",
    #           "createdDate",
    #           "JobStatus",
    #           "employmentType")
