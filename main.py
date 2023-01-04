from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_header
from controllers.analytics_controller import *
from dataaccess.entity.userObReltn import *
from dataaccess.entity.usrAstReltn import *
from flask_oidc import OpenIDConnect
from okta_jwt_verifier import AccessTokenVerifier
import jwt

app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'super-secret'
# app.config['JWT_ENCODE_ISSUER'] = 'http://localhost:8085/auth/realms/master'
# app.config['JWT_DEFAULT_REALM'] = 'master'
app.config.update({
    'SECRET_KEY': 'super-secret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client-secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'master',
    'OIDC_SCOPES': ["openid", "web-origins", "phone", "profile",
                    "offline_access", "microprofile-jwt", "address", "roles", "email"],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keycloak:password@localhost:5432/rahul'
# dialect+driver://username:password@host:port/database
app.config[''] = 'master'
CORS(app)
JWTManager(app)
db.init_app(app)
ma.init_app(app)


oidc.init_app(app)


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


@app.route('/check')
def check():
    # print("Temp#####")
    # jwt_verifier = JWTVerifier('http://localhost:8085/auth/realms/master', 'nginx', 'api://default')
    # jwt_verifier.verify_access_token('eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJpdXU4bXA3d0JsYzB2bmx5eUhRMTZEVDZTYmJvX0Y1LUd1Z0REZDU4a3BzIn0.eyJleHAiOjE2NzI4OTM2OTIsImlhdCI6MTY3Mjg1NzY5MiwianRpIjoiMDhjMjgxZmQtMjNhYS00MzMyLTgxYjctNjA0NDk2ZmQwNzUzIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDg1L2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6IjdkMjFhZDI1LTM0YWMtNGQ2ZC1hMDQ4LThlMmVlMDRkMTdkMyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLWNsaSIsInNlc3Npb25fc3RhdGUiOiIwNWZhODRkNC1jZjk1LTRmNTktOWFjNS1kMTEwOGZhZWNjNmIiLCJhY3IiOiIxIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiMDVmYTg0ZDQtY2Y5NS00ZjU5LTlhYzUtZDExMDhmYWVjYzZiIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhZG1pbiJ9.RdHVYmb5t4Kdv7CFBYI0JVCGTE2Szerub1sqxnSJmGiRgrDTyeLwknsPvfBg6OwTySw3U8QFqqXWLsfXEY4eajOc9poaHhsdW_LRwUMgC58ikfengCFlFszBABzGn4NJ29vbcfTIaOsKmxW92XYPxlYICkFkEMFxVviLUG8L1zpsVZM56ftw3a0sdNsCB7xU914amPuQY6fk-bKRDDeoR319p4cC6f1p_mLrsC6vkZSo4QacGasLxPI3rwveKLjN-gM6QE-imApMM8wrkEaAbfIUZgei_h549Qa-avwGyctax4vQ3vFYVEOQT9FZAebpzX_MKkhpmkzHS68HJ9IWXQ')
    # print('Token validated successfully.')
    # return "OK"
    # Public key from Keycloak realm -> Keys -> Public Key -> (view)
    public_key = """-----BEGIN PUBLIC KEY-----
    MIICmTCCAYECBgGFfiMhqjANBgkqhkiG9w0BAQsFADAQMQ4wDAYDVQQDDAVuZ2lueDAeFw0yMzAxMDQxODUzMjlaFw0zMzAxMDQxODU1MDlaMBAxDjAMBgNVBAMMBW5naW54MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy1ZG5tv4INkAsCzKqbyFZcm4zF3hP0t4Ij9R+m5P/oGmeek+FuFTntJJ4szhtlc76vlYMH5lhVm7enDEj9PS7QzmMgQeDR2XWNECCPUHfpwdTW+BxygwZfIEF/ptBB8urJdaNtm55qOYi5KhgnQ+xwO7IL/ej4kSklobxX9IOQENXz6A/MlXi+jtZ63hQggg2AP0ZDvCi7JUS7I4+9KaAbMyY/K+chtF2ZheWmpFMKBiot5awjz1PKcDiZaFXAsdydca4SF4lYQOLVH2z80FPuIeWZ0v8Sk2S3PQdCYzja32ZS2peklrTmsXSOvcGunrr+r6xSmRVy7gH/71HWz3vQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA0VTcpIpyHVTsjmsYnK0bW1p3tAbPaIIupajUhPYzUaIvsQut9s1LGZinSYP/H4f4TmledReGQRyQKTGbo/MOe7CRW0FMLmVcP8IaESEqw/MtvJiqEckK/Ph6I0VI2OluxE5CWQdhxB+rySn3ur6N9XHQbYNHPhJ2jKRxSFCsjqV3lceCuO2yniVmz0qZuwCqdK3cKU9usJpqemYuh94JBc6U5grMko/ZINDC/yyYE6+vpEgu9ddM7j3zbrvws9nuQ3LqapAyS/kHvaH7RDWDz+ihBV/+I6XXcT5WZVD2XR3NoPZ7RLHEbZnEFrNmTvOwArDd6Dm7ZMRohlOiEzr9T
    -----END PUBLIC KEY-----"""

    # Keycloak JWT RS256 access-token
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwODcyYzBkOS0xYmJjLTQ0YzMtYTUzMy01NTU0OWFmMjQyZmYifQ.eyJleHAiOjE2NzI4OTU1NzUsImlhdCI6MTY3Mjg1OTU3NSwianRpIjoiM2ZhNDllODItZjkwZC00YjlmLTkzZWEtMjliNGFiNjNhZjhkIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDg1L2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6IjdkMjFhZDI1LTM0YWMtNGQ2ZC1hMDQ4LThlMmVlMDRkMTdkMyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLWNsaSIsInNlc3Npb25fc3RhdGUiOiI2M2VlNjRjNS02ZDY0LTQ2YWItYjcxZC02OGVlN2E5NDA4OGUiLCJhY3IiOiIxIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiNjNlZTY0YzUtNmQ2NC00NmFiLWI3MWQtNjhlZTdhOTQwODhlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhZG1pbiJ9.usceKls13X53pkcWu8zUuKMAN1XXeN_PZofOt7ObECI'

    access_token_json = jwt.decode(access_token, public_key, audience='account', algorithms=["HS256"])
    print(access_token_json)


def is_access_token_valid(token, issuer):
    jwt_verifier = AccessTokenVerifier(issuer=issuer, audience='api://default')
    try:
        jwt_verifier.verify(token)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
