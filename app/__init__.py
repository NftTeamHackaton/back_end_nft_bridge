from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_restful
from .config import Config
from flask_cors import CORS
from flask_crontab import Crontab

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
api = flask_restful.Api(app)
migrate = Migrate(app, db)
cors = CORS(app)
crontab = Crontab(app)

from app import models, controllers, services
