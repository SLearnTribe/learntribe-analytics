import json
from flask import Flask
from flask_cors import CORS
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


@app.route('/validate', methods=['GET'])
@jwt_verification
def checks(decoded_jwt):
    return json.dumps({"message": "JWT verified",
                       "sub": decoded_jwt['sub']})


if __name__ == "__main__":
    app.run(debug=True)
