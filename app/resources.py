# coding: utf-8
import http

from flask import jsonify, make_response
from flask_restful import Resource
from webargs.flaskparser import use_args

from app.schemas import PaymentCreditCardSchema
from app.db import db


class PaymentResource(Resource):

    @use_args(
        PaymentCreditCardSchema(
            strict=True, only=("amount", "buyer", "credit_card", "X-CLIENT")), locations=("headers", "json"))
    def post(self, payment):
        """
       Captura o pagamento do comprador.
       ---
       parameters:
         - in: header
           name: X-CLIENT
           schema:
             type: string
           required: true
         - in: body
           name: data
           required: true
           schema:
             id: Payload
             required:
               - amount
             properties:
               amount:
                  type: string
               buyer:
                  type: object
                  properties:
                    name:
                      type: string
                    email:
                      type: string
                    cpf:
                      type: string
               creditcard:
                  type: object
                  properties:
                    holder_name:
                      type: string
                    number:
                      type: string
                    expiration_date:
                       type: string
                    cvv:
                       type: string
       responses:
         200:
           description: Pagamento realizado com sucesso.
           schema:
             type: object
         403:
           description: Cliente inválido.
           schema:
             type: object
             properties:
               errors:
                 type: object
                 properties:
                    client:
                      type: array
                      items:
                        type: string
         422:
           description: Houve algum erro ao processar a requisição
           schema:
             type: object
        """

        db.session.add(payment)
        db.session.commit()

        return make_response(
            jsonify(mensagem="payment created successfully"), http.HTTPStatus.OK)


class BoletoResource(Resource):

    def post(self):
        pass
