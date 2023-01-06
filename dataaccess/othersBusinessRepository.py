from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from dataaccess.entity.othersBusiness import UserBusiness, UserBusinessSchema

db = SQLAlchemy()
user_business = UserBusinessSchema()
users_business = UserBusinessSchema(many=True)


def find_all_by_id(job_id: list):
    others_business = UserBusiness.query.filter(id.in_(job_id)).all()
    if others_business:
        result = users_business.dump(others_business)
        return jsonify(result)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id(user_id: str):
    others_business = UserBusiness.query.filter_by(createdBy=user_id).all()
    if others_business:
        result = users_business.dump(others_business)
        return jsonify(result)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404
