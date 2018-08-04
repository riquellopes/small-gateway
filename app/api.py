# coding: utf-8
from flask_restful import Api
from flask_cors import CORS
from app import app as application
from app.db import db


def setup_app():
    db.init_app(application)
    CORS(application)

    return application


app = setup_app()
