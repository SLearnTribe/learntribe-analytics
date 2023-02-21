import json
import os
import uuid
from flask import Flask
from flask_cors import CORS
import consul
import socket
from authorization.jwt_verification import jwt_verification
from controllers.analytics_controller import *
from dataaccess.entity.userObReltn import *
from dataaccess.entity.usrAstReltn import *

app = Flask(__name__)
# Format : sql://username:password@uri/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keycloak:password@38.242.132.44:5432/inquisitve'
CORS(app, resources={r"/api/v1/analytics": {"origins": ["http://www.smilebat.xyz", "http://localhost:3000"]}})
db.init_app(app)
ma.init_app(app)
consul_client = consul.Consul(host="38.242.132.44", port=8500)
service_id = f"flask_app_{str(uuid.uuid4())}"


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def register_service_with_consul(port):
    consul_client.agent.service.register(
        name="sb-ana",
        service_id=service_id,
        address="localhost/api/v1/analytics",
        port=port,
        check=consul.Check.http("localhost/health", port, "30s")
    )


def deregister_service_with_consul():
    consul_client.agent.service.deregister(service_id)


AnalyticsControllerView.register(app, route_base='/api/v1/analytics')


@app.route('/validate', methods=['GET'])
@jwt_verification
def checks(decoded_jwt):
    return json.dumps({"message": "JWT verified",
                       "sub": decoded_jwt['sub']})


@app.route("/health", methods=['GET'])
def health_check():
    health_check_is_successful = True
    if health_check_is_successful:
        return {"status": "ok"}, 200
    else:
        return {"status": "not ok"}, 500


if __name__ == "__main__":
    try:
        port = get_free_port()
        print(f"RJ : {port}")
        register_service_with_consul(port)
        app.run(port=port, debug=True, use_reloader=False)
    except Exception as e:
        print(f"Exception : {e}")
    finally:
        deregister_service_with_consul()
