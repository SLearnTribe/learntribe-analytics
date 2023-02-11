import json
import subprocess
import sys
import uuid

from flask import Flask
from flask_cors import CORS
import consul
import socket
import multiprocessing
from authorization.jwt_verification import jwt_verification
from controllers.analytics_controller import *
from dataaccess.entity.userObReltn import *
from dataaccess.entity.usrAstReltn import *

app = Flask(__name__)
# Format : sql://username:password@uri/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keycloak:password@38.242.132.44:5432/inquisitve'
CORS(app)
db.init_app(app)
ma.init_app(app)
consul_client = consul.Consul(host='38.242.132.44', port=8500)
service_id = f"flask_app_{str(uuid.uuid4())}"


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def register_service_with_consul(port):
    # return
    consul_client.agent.service.register(
        name="sb-ana",
        service_id=service_id,
        address="localhost/api/v1/analytics",
        port=port,
        check=consul.Check.http("localhost/health", port, "30s")
    )


def deregister_service_with_consul():
    # return
    consul_client.agent.service.deregister(service_id)

'''  Used for testing DB put
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
'''


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
    port = get_free_port()
    print(f"RJ : {port}")
    register_service_with_consul(port)
    # workers = multiprocessing.cpu_count() * 2 + 1
    try:
        app.run(port=port, debug=True)
        '''Code to use gunicorn'''
        # process = subprocess.Popen(["gunicorn", "--workers", str(workers), "-b", f":{port}", "main:app"],
        #                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #
        # while True:
        #     output = process.stdout.readline()
        #     if output == b'' and process.poll() is not None:
        #         break
        #     if output:
        #         print(output.strip().decode())
        #     err = process.stderr.readline()
        #     if err == b'' and process.poll() is not None:
        #         break
        #     if err:
        #         print(err.strip().decode(), file=sys.stderr)
    except Exception as e:
        print(f"Exception : {e}")
    finally:
        deregister_service_with_consul()
