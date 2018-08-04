# coding: utf-8
from flask import redirect
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
from app import app as application
from app.db import db
from app.resources import PaymentResource


def setup_app():
    db.init_app(application)
    CORS(application)
    Swagger(application)

    api = Api(application, prefix="/api/v1")
    api.add_resource(PaymentResource, "/capture/", methods=['POST'])

    return application


app = setup_app()


@app.route("/")
def home():
    return redirect('/apidocs')
