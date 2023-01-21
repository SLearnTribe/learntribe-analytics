from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_enum import EnumField

from models.enums.hiring_status import HiringStatus
from models.enums.userObReltnType import UserObReltnType

db = SQLAlchemy()
ma = Marshmallow()


class UserObReltn(db.Model):
    __tablename__ = 'usr_ob_reltn'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.String)
    hiring_status = db.Column(db.Enum(HiringStatus))
    user_ob_reltn = db.Column(db.Enum(UserObReltnType))
    job_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<User {self.user_id}>'


class UserObReltnSchema(ma.Schema):
    class Meta:
        model = UserObReltn
        # fields = ("id",
        #           "userId",
        #           "hiringStatus",
        #           "userObReltn",
        #           "jobId")

    id = fields.Integer()
    user_id = fields.String()
    hiring_status = EnumField(enum=HiringStatus)
    user_ob_reltn = EnumField(enum=UserObReltnType)
    job_id = fields.Integer()
