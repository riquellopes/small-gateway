# coding: utf-8
import http

from flask import jsonify, make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from flasgger import swag_from

from app.schemas import PaymentCreditCardSchema, PaymentBoletoSchema
from app.db import db


class PaymentResource(Resource):

    @use_args(
        PaymentCreditCardSchema(
            strict=True, only=("amount", "buyer", "credit_card", "X-CLIENT")), locations=("headers", "json"))
    @swag_from('docs/credit_card.yml')
    def post(self, payment):
        db.session.add(payment)
        db.session.commit()

        return make_response(
            jsonify(mensagem="payment created successfully"), http.HTTPStatus.OK)


class BoletoResource(Resource):

    @use_args(
        PaymentBoletoSchema(
            strict=True, only=("amount", "buyer", "X-CLIENT")), locations=("headers", "json"))
    def post(self, payment):
        db.session.add(payment)
        db.session.commit()

        return make_response(
            jsonify(payment_code=payment.code), http.HTTPStatus.OK)
