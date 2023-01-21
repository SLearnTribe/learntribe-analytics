from datetime import datetime, timedelta

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

from dataaccess.entity.othersBusiness import OthersBusiness, OthersBusinessSchema

db = SQLAlchemy()
others_business_schema = OthersBusinessSchema()
others_businesses_schema = OthersBusinessSchema(many=True)


def find_all_by_id(job_ids: tuple):
    others_business = OthersBusiness.query.filter(OthersBusiness.id.in_(job_ids)).all()
    print(others_business)
    if others_business:
        result = others_businesses_schema.dump(others_business)
        print(result)
        return result
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id(user_id: str, page: int, per_page: int):
    others_business = OthersBusiness.query.filter_by(created_by=user_id) \
        .paginate(page=page, per_page=per_page) \
        .items

    if others_business:
        # print("Rahul1")
        return others_business
        # result = others_businesses_schema.dump(others_business)
        # print(result)
        # return result
    else:
        # print("Rahul2")
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id_and_current_date(user_id: str, page: int, per_page: int):
    others_businesses = OthersBusiness.query \
        .filter(and_(OthersBusiness.id == user_id,
                     OthersBusiness.created_date >= (datetime.now() - timedelta(days=30)))) \
        .paginate(page=page, per_page=per_page) \
        .items

    if others_businesses:
        others_businesses_data = others_businesses_schema.dump(others_businesses)
        return jsonify(others_businesses_data)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404
