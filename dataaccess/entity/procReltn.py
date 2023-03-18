from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class ProcReltn(db.Model):
    __tablename__ = 'proc_reltn'
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.String)
    assessment_id = db.Column(db.Integer)
    good = db.Column(db.Integer)
    many = db.Column(db.Integer)
    bad = db.Column(db.Integer)

    def __repr__(self):
        return f'<User {self.id}>'


class ProcReltnSchema(ma.Schema):
    class Meta:
        model = ProcReltn

    id = fields.Integer()
    user_id = fields.String()
    assessment_id = fields.Integer()
    good = fields.Integer()
    many = fields.Integer()
    bad = fields.Integer()
