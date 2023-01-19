from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from dataaccess.entity.usrAstReltn import UserAstReltn, UserAstReltnSchema

app = Flask(__name__)
db = SQLAlchemy(app)
user_ast_reltn_schema = UserAstReltnSchema()
users_ast_reltn_schema = UserAstReltnSchema(many=True)


def find_by_user_id(keycloak_id: str):
    user_ast_reltn = UserAstReltn.query.filter_by(userId=keycloak_id).all()
    if user_ast_reltn:
        result = users_ast_reltn_schema.dump(user_ast_reltn)
        return jsonify(result), 200
    else:
        return jsonify(message="The keycloakID does not exist"), 404


def find_by_user_id_and_filter(keycloak_id: str, status: str):
    user_ast_reltn = UserAstReltn.query.filter_by(userId=keycloak_id, status=status).all()
    if user_ast_reltn:
        result = users_ast_reltn_schema.dump(user_ast_reltn)
        return jsonify(result)
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def count_by_user_id_and_filter(keycloak_id: str, status: str):
    count = UserAstReltn.query.filter_by(user_id=keycloak_id, status=status).count()
    if count is not None:
        return count
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


def find_all_by_user_ast_reltn(keycloak_id: str, assessment_id: str):
    user_ast_reltn = UserAstReltn.query.filter_by(userId=keycloak_id, assessmentId=assessment_id).all()
    if user_ast_reltn:
        result = users_ast_reltn_schema.dump(user_ast_reltn)
        return jsonify(result), 200
    else:
        return jsonify(message="The keycloakID does not exist or wrong status"), 404


# def find_all_by_assessment_title(keycloak_id: str, skills: tuple):
#     user_ast_reltn = UserAstReltn.query.filter_by(userId=keycloak_id, assessmentTitle.in_(skills)).all()
#     if user_ast_reltn:
#         result = users_ast_reltn_schema.dump(user_ast_reltn)
#         return jsonify(result), 200
#     else:
#         return jsonify(message="The keycloakID does not exist or wrong status"), 404
