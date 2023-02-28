import uuid
from flask import Flask
from flask_cors import CORS
import consul
import socket
import logging
from authorization.jwt_verification import jwt_verification
from controllers.analytics_controller import *
from dataaccess.entity.userObReltn import *
from dataaccess.entity.usrAstReltn import *

app = Flask(__name__)
# Format : sql://username:password@uri/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keycloak:password@38.242.132.44:5432/inquisitve'
CORS(app, resources={r"/api/v1/*": {"origins": ['www.smilebat.xyz', 'http://localhost:3000'],
                                    "methods": ['GET,PUT,POST,DELETE'],
                                    "allow_headers": ['authorization', 'Content-Type'],
                                    "vary_header": ['Access-Control-Request-Method',
                                                    'Origin',
                                                    'Access-Control-Request-Headers'],
                                    }})
db.init_app(app)
ma.init_app(app)
consul_client = consul.Consul(host="consul", port=8500)
# consul_client = consul.Consul(host="www.smilebat.xyz", port=8500)
service_id = f"sb-ana-{str(uuid.uuid4())}"
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger('sb-ana')


def get_free_port():
    logger.info("Evaluating free ports")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def register_service_with_consul(host, port):
    logger.info('Registering to Consul with Hostname : ' + host)
    try:
        consul_client.agent.service.register(
            name="sb-ana",
            service_id=service_id,
            port=port,
            address=host,
            tags=[],
            check=consul.Check.http(url=f'http://{host}:{port}/actuator/health',
                                    interval='30s',
                                    timeout='5s')
        )
    except ConnectionError:
        logger.error('Consul Host is down')


def deregister_service_with_consul():
    consul_client.agent.service.deregister(service_id)


AnalyticsControllerView.register(app, route_base='/api/v1/analytics')


@app.route("/actuator/health", methods=['GET'])
def health_check():
    health_check_is_successful = True
    if health_check_is_successful:
        return jsonify(status="ok"), 200
    else:
        return jsonify(status="Not ok"), 500


if __name__ == "__main__":
    try:
        host = socket.gethostname()
        port = get_free_port()
        # port=8153
        register_service_with_consul(host, port)
        app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
    except Exception as e:
        logging.error(f"Exception : {e}")
    finally:
        deregister_service_with_consul()
