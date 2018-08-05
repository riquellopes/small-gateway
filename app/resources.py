# coding: utf-8
import http

from flask import jsonify, make_response, abort, current_app
from flask_restful import Resource
from webargs.flaskparser import use_args
from flasgger import swag_from

from app.schemas import PaymentCreditCardSchema, PaymentBoletoSchema, PaymentReponseSchema
from app.models import Payment
from app.db import db


class CreditCardResource(Resource):

    @use_args(
        PaymentCreditCardSchema(
            strict=True, only=("amount", "buyer", "credit_card", "X-CLIENT")), locations=("headers", "json"))
    @swag_from('docs/credit_card.yml')
    def post(self, payment):
        current_app.logger.info(
            "After process: type {}, credit {} buyer {}".format(
                payment.type, payment.credit_card, payment.buyer))

        db.session.add(payment)
        db.session.commit()

        current_app.logger.info(
            "Before proecss: payment {}, type {}, credit {} buyer".format(
                payment.id, payment.type.id, payment.credit_card, payment.buyer))

        return make_response(
            jsonify(mensagem="payment created successfully"), http.HTTPStatus.OK)


class BoletoResource(Resource):

    @use_args(
        PaymentBoletoSchema(
            strict=True, only=("amount", "buyer", "X-CLIENT")), locations=("headers", "json"))
    @swag_from('docs/boleto.yml')
    def post(self, payment):
        db.session.add(payment)
        db.session.commit()

        return make_response(
            jsonify(payment_code=payment.code), http.HTTPStatus.OK)


class PaymentResource(Resource):

    def get(self):
        schema = PaymentReponseSchema(many=True, exclude=['created_date', 'update_date'])
        data = schema.dump(Payment.query.order_by(
            Payment.created_date.desc()
        ).all())
        return make_response(jsonify(results=data.data))


class PaymentoDetailsResource(Resource):

    def get(self, id):
        payment = Payment.query.filter(Payment.id == id)
        if payment.count() == 0:
            abort(404)

        schema = PaymentReponseSchema(exclude=['created_date', 'update_date'])
        data = schema.dump(payment.first())

        return make_response(jsonify(result=data.data))
