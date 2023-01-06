from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.enums.hiring_status import HiringStatus
from models.enums.userObReltnType import UserObReltnType

db = SQLAlchemy()
ma = Marshmallow()


class UserObReltn(db.Model):
    __tablename__ = 'USR_OB_RELTN'
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    userId = db.Column("userId", db.String)
    hiringStatus = db.Column("hiringStatus", db.Enum(HiringStatus))
    userObReltn = db.Column("userObReltn", db.Enum(UserObReltnType))
    jobId = db.Column("jobId", db.Integer)

    def __repr__(self):
        return f'<User {self.userId}>'


class UserObReltnSchema(ma.Schema):
    class Meta:
        fields = ("id",
                  "userId",
                  "hiringStatus",
                  "userObReltn",
                  "jobId")
