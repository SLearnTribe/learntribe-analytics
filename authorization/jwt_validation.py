"""
Created on 18/11/18
Author Rahul Joshi

Function to deal with JWT exchanged with keycloak.
"""

import json
import os
from functools import wraps
from flask import Flask, request
from jose import jwt

# app = Flask(__name__)
# ISSUER = "http://localhost:8085/auth/realms/master"
# KEYCLOAK_PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmrHA0Ver4Ui3Jvd8LbUtjT+YV4pm80puev0X5zbdUZj5p1KhpFr38sLCYdj+gcGDLyKerIJvU7OqqFE7wSEX1lOtHpiaJaV16pwK6QD5u2eLS5visZLZKCixjxxdPpYlP+U1Itb3yFZLKwHXlk8LNYONfYU3c1lliFtoVcytQ9gbTi9r5vnbgHf57rmr8+a4vSDKW5h01Z4i+4AkB2QAmAoxpN2XLd6D9+mbo1GSCXteAEqOWc6C9UWys/xPbxFP+XQYfnsZnfnS4a62HkW0iT1eTNW/148a7G8LKHXw+JY3aeZLnGIICJ9uLB06G8GezAGZTfGalkTd/EJBiqwjzwIDAQAB
# -----END PUBLIC KEY-----'''

ISSUER = os.getenv('ISSUER', 'http://localhost:8085/auth/realms/master')
KEYCLOAK_PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----' + \
                      os.getenv('KEYCLOAK_PUBLIC_KEY',
                                'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmrHA0Ver4Ui3Jvd8LbUtjT+YV4pm80puev0X5zbdUZj5p1KhpFr38sLCYdj+gcGDLyKerIJvU7OqqFE7wSEX1lOtHpiaJaV16pwK6QD5u2eLS5visZLZKCixjxxdPpYlP+U1Itb3yFZLKwHXlk8LNYONfYU3c1lliFtoVcytQ9gbTi9r5vnbgHf57rmr8+a4vSDKW5h01Z4i+4AkB2QAmAoxpN2XLd6D9+mbo1GSCXteAEqOWc6C9UWys/xPbxFP+XQYfnsZnfnS4a62HkW0iT1eTNW/148a7G8LKHXw+JY3aeZLnGIICJ9uLB06G8GezAGZTfGalkTd/EJBiqwjzwIDAQAB') + \
                      '-----END PUBLIC KEY-----'


def jwt_verification(f):
    """
    Decorator for the JWT validation.
    :param :
    :return: Decoded JWT
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        jwt_token = request.headers.get("Authorization").split(" ")[1]

        try:
            decoded_jwt = jwt.decode(jwt_token, KEYCLOAK_PUBLIC_KEY,
                                     algorithms=["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384",
                                                 "ES512", "PS256", "PS512", "RS512"], issuer=ISSUER)
        except jwt.ExpiredSignatureError:
            return json.dumps({"error": "JWT has expired"}), 419  # Authentication Timeout
        except jwt.JWTClaimsError:
            return json.dumps({"error": "JWT has invalid claims"}), 400  # Bad Request
        except jwt.JWTError:
            return json.dumps({"error": "Invalid JWT"}), 401  # Unauthorized
        except Exception as e:
            return json.dumps({"error": str(e)}), 500  # Internal Server Error

        return f(decoded_jwt, *args, **kwargs)

    return decorated_function


'''Usage'''
# @app.route("/", methods=["GET"])
# @jwt_verification
# def index(decoded_jwt):
#     return json.dumps({"message": "JWT verified",
#                        "sub": decoded_jwt['sub']})
