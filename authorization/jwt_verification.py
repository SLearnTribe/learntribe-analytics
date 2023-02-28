"""
Created on 19/01/23

Author Rahul Joshi

Function to deal with JWT exchanged with keycloak.
"""

import json
import os
from functools import wraps
from flask import request
from jose import jwt


ISSUER = os.getenv('ISSUER', 'http://www.smilebat.xyz/realms/master')
KEYCLOAK_PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----\n' + \
                      os.getenv('KEYCLOAK_PUBLIC_KEY',
                                'MIICmTCCAYECBgGGl6mK5zANBgkqhkiG9w0BAQsFADAQMQ4wDAYDVQQDDAVuZ2lueDAeFw0yMzAyMjgxMDUzMzZaFw0zMzAyMjgxMDU1MTZaMBAxDjAMBgNVBAMMBW5naW54MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzAmQudrBHMK4m+08tGkq01k0eIpdFwA+n/fe43GtO1vwye6+d2Vvx4zD4CR0lgpnJKAjuQM7gqiZrJ6XHmV/VlZk0ZB9KcqiG7KOlJlSFk0iYMApCBtQ9qvwr9W6UOzYvEzYv29WuaPj72qFjc3CRCYQGIfxxPcidNePv/z6vpidNIyNwI9WWRmoZ4CNSit8A4CO41ppq+ZrWQmBgZn7XfCJH4GDIMyL5ezjXfQXzcXrrFKaNbbquJqwhIZLUYu2CMzA20A1s2JE9/9P5eJcdN2IdQlk0icbnrpHtW8JldNfKRcOyqbmn3J9TQ/iTLvlduX3Sh5gqCUQQGa4EGXVrQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQC78JPGe9DqP1dICt3W12nC67NOfXtnEFIKo28kQ3U06BWD0WpkpERlBgfm8QjOUOptSKnRPXc7ui/VT5ffKPsjgAmNcDJJmzujLoGRW4sf5obhEAfNO7MC3+jnNFvIB3ptzp5hLRCmG5QMxllo/szd8Nzhzp2WVg4ocEh5OZLhI5JuR6tj32JFQXO8wzDt9wcTZPV5gtgPiXHD+vmyIfFK+s1CTeReaQnfDi3H9T7c1LjxtTRkEZx/Qf4YIHp3oNPQRvymM4to2aSBxFsMtO+ML0U6gJcJO9qY/9MJOS4VoSGECuY3Khd8Bmu23v10DMJqUyGFlcLdD9+KYFoYk5xR') + \
                      '\n-----END PUBLIC KEY-----'


def jwt_verification(f):
    """
    Decorator for the JWT validation.

    Usage :\n
    @app.route("/", methods=["GET"])\n
    @jwt_verification\n
    def index(decoded_jwt):\n
    return json.dumps({"message": "JWT verified","sub": decoded_jwt['sub']})

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
