# coding: utf-8

from flask import redirect
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
from flask_migrate import Migrate
from flask_alembic import Alembic
from webargs.flaskparser import abort, parser

from app import app as application
from app.db import db
from app.resources import (
    CreditCardResource, BoletoResource, PaymentoDetailsResource, PaymentResource)


def setup_app():
    db.init_app(application)
    CORS(application)
    Swagger(application)
    Migrate(application, db)
    Alembic(application)

    api = Api(application, prefix="/api/v1")
    api.add_resource(CreditCardResource, "/credit-card/capture/", methods=['POST'])
    api.add_resource(BoletoResource, "/boleto/", methods=['POST'])
    api.add_resource(PaymentResource, "/payment/", methods=['GET'])
    api.add_resource(PaymentoDetailsResource, "/payment/<int:id>", methods=['GET'])

    return application


app = setup_app()


@app.route("/")
def home():
    return redirect('/apidocs')


# https://github.com/sloria/webargs/blob/dev/examples/flaskrestful_example.py#L72
# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(err.status_code, errors=err.messages)
