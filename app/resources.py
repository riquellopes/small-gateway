# coding: utf-8
from flask_restful import Resource


class PaymentResource(Resource):

    # @TODO to add a wrapping for validate the client
    def post(self):
        """
       Captura o pagamento do comprador.
       ---
       parameters:
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
        """
        pass
