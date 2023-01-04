from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataaccess.entity.userObReltn import UserObReltn, UserObReltnSchema

app = Flask(__name__)
db = SQLAlchemy(app)
user_ob_schema = UserObReltnSchema()
users_ob_schema = UserObReltnSchema(many=True)


def find_by_user_id(keycloak_id: str):
    user_ob_reltn = UserObReltn.query.filter_by(userId=keycloak_id).all()
    if user_ob_reltn:
        result = users_ob_schema.dump(user_ob_reltn)
        return jsonify(result), 200
    else:
        return jsonify(message="The keycloakID does not exist"), 404


def find_by_related_job_id(keycloak_id: str, job_id: str):
    user_ob_reltn = UserObReltn.query.filter(userId=keycloak_id, jobId=job_id).all()
    if user_ob_reltn:
        result = users_ob_schema.dump(user_ob_reltn)
        return jsonify(result), 200
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_by_user_id_and_status(keycloak_id: str, hiring_status: str):
    user_ob_reltn = UserObReltn.query.filter(userId=keycloak_id, hiringStatus=hiring_status).all()
    if user_ob_reltn:
        result = users_ob_schema.dump(user_ob_reltn)
        return jsonify(result), 200
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def count_by_user_id_and_status(keycloak_id: str, hiring_status: str):
    count = UserObReltn.query.filter_by(userId=keycloak_id, hiringStatus=hiring_status).count()
    if count is not None:
        return count, 200
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def count_by_job_hiring_status(job_id: str, hiring_status: str):
    count = UserObReltn.query.filter(jobId=job_id, hiringStatus=hiring_status).count()
    if count is not None:
        return count, 200
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404
