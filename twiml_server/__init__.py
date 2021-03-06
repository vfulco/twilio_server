from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
db = SQLAlchemy(app)

from resources.endpoint import Endpoint
from resources.messages import Messages

api.add_resource(Endpoint, '/twilioendpoint')
api.add_resource(Messages, '/messages/<account_sid>')

