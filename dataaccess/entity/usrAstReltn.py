from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.enums.assessment_status import AssessmentStatus
from models.enums.userAstReltnType import UserAstReltnType

db = SQLAlchemy()
ma = Marshmallow()


class UserAstReltn(db.Model):
    __tablename__ = 'usr_ast_reltn'
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.String)
    assessment_id = db.Column(db.Integer)
    assessment_title = db.Column(db.String)
    status = db.Column(db.Enum(AssessmentStatus))
    user_ast_reltn_type = db.Column(db.Enum(UserAstReltnType))
    questions = db.Column(db.Integer)
    answered = db.Column(db.Integer)

    def __repr__(self):
        return f'<User {self.userId}>'


class UserAstReltnSchema(ma.Schema):
    class Meta:
        model = UserAstReltn
        fields = ("id",
                  "user_id",
                  "assessment_id",
                  "assessment_title",
                  "status",
                  "user_ast_reltn_type",
                  "questions",
                  "answered")
