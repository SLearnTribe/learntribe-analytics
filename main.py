from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_header
from controllers.analytics_controller import *
from dataaccess.entity.userObReltn import *
from dataaccess.entity.usrAstReltn import *
from flask_oidc import OpenIDConnect
from okta_jwt_verifier import AccessTokenVerifier
import jwt

from helpers.authorization import AuthorizationHelper

app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'super-secret'
# app.config['JWT_ENCODE_ISSUER'] = 'http://localhost:8085/auth/realms/master'
# app.config['JWT_DEFAULT_REALM'] = 'master'
# app.config.update({
#     'SECRET_KEY': 'super-secret',
#     'TESTING': True,
#     'DEBUG': True,
#     'OIDC_CLIENT_SECRETS': 'client-secrets.json',
#     'OIDC_ID_TOKEN_COOKIE_SECURE': False,
#     'OIDC_REQUIRE_VERIFIED_EMAIL': False,
#     'OIDC_USER_INFO_ENABLED': True,
#     'OIDC_OPENID_REALM': 'master',
#     'OIDC_SCOPES': ["openid", "web-origins", "phone", "profile",
#                     "offline_access", "microprofile-jwt", "address", "roles", "email"],
#     'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
# })
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keycloak:password@localhost:5432/rahul'
# dialect+driver://username:password@host:port/database
CORS(app)
JWTManager(app)
db.init_app(app)
ma.init_app(app)

# oidc.init_app(app)
ah = AuthorizationHelper('./configurations/authorization.ini')


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Tables created")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('tables dropped!')


@app.cli.command('db_seed')
def db_seed():
    user_ob1 = UserObReltn(id='1',
                           userId='1',
                           hiringStatus='HIRED',
                           userObReltn='CANDIDATE',
                           jobId='1')
    user_ast1 = UserAstReltn(id='1',
                             userId='1',
                             assessmentId='1',
                             assessmentTitle='C#',
                             status='COMPLETED',
                             userAstReltnType='ASSIGNED')
    db.session.add(user_ob1)
    db.session.add(user_ast1)
    db.session.commit()
    print('data filled in tables')


AnalyticsControllerView.register(app, route_base='/api/v1/analytics')


@app.route('/access', methods=['POST'])
def temp_access():
    uid = request.form['uid']
    access_token = create_access_token(identity=uid)
    return jsonify(token=access_token), 200


@app.route('/checks', methods=['POST'])
def checks():
    token_header = request.headers['Authorization'].split(' ')[1]
    # return token_header
    txt = ah.verify_jwt(token_header)[0]
    if txt:
        return jsonify(result="True"), 200
    else:
        return jsonify(result="False"), 400
    # return jsonify(temp=ah.verify_jwt(token_header)), 403


if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True)
