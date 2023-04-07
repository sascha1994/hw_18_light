from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
