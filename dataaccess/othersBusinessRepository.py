from datetime import datetime, timedelta

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

from dataaccess.entity.othersBusiness import OthersBusiness, OthersBusinessSchema

db = SQLAlchemy()
others_business_schema = OthersBusinessSchema()
others_businesses_schema = OthersBusinessSchema(many=True)


def find_all_by_id(job_id: list):
    others_business = OthersBusiness.query.filter(OthersBusiness.id.in_(job_id)).all()
    if others_business:
        result = others_businesses_schema.dump(others_business)
        return jsonify(result)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id(user_id: str, page: int, per_page: int):
    others_business = OthersBusiness.query.filter_by(createdBy=user_id) \
        .paginate(page=page, per_page=per_page) \
        .items
    # return others_business
    if others_business:
        result = others_businesses_schema.dump(others_business)
        return jsonify(result)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id_and_current_date(user_id: str, page: int, per_page: int):
    others_businesses = OthersBusiness.query \
        .filter(and_(OthersBusiness.id == user_id,
                     OthersBusiness.createdDate >= (datetime.now() - timedelta(days=30)))) \
        .paginate(page=page, per_page=per_page) \
        .all()
    #   .items

    if others_businesses:
        others_businesses_data = others_businesses_schema.dump(others_businesses)
        return jsonify(others_businesses_data)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404
