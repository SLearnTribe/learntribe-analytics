from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.assessment_status import AssessmentStatus
from models.userAstReltnType import UserAstReltnType

db = SQLAlchemy()
ma = Marshmallow()


class UserAstReltn(db.Model):
    __tablename__ = 'USR_AST_RELTN'
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    userId = db.Column("userId", db.String)
    assessmentId = db.Column("assessmentId", db.Integer)
    assessmentTitle = db.Column("assessmentTitle", db.String)
    status = db.Column("status", db.Enum(AssessmentStatus))
    userAstReltnType = db.Column("userAstReltnType", db.Enum(UserAstReltnType))

    def __repr__(self):
        return f'<User {self.userId}>'


class UserAstReltnSchema(ma.Schema):
    class Meta:
        fields = ("id",
                  "userId",
                  "assessmentId",
                  "assessmentTitle",
                  "status",
                  "userAstReltnType")
