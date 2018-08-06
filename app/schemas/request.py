# coding: utf-8
import re
import http
import luhnpy
import datetime

from marshmallow import (
    post_load,
    validates_schema,
    validates,
    ValidationError, fields, validate, )

from marshmallow_sqlalchemy import ModelSchema
from app.models import Payment, Type, Client
from pycpfcnpj import cpfcnpj

from .response import (
    CardResponseSchema, BuyerResponseSchema, TypeResponseSchema, ClientResponseSchema)

from app.db import db


class CardSchema(CardResponseSchema):
    holder_name = fields.Str(
        required=True,
    )
    cvv = fields.Str(
        required=True,
    )

    @validates("number")
    def validate_number(self, number):
        if number.isdigit() is False:
            raise ValidationError(
                "The credit card should be a numeral.")

        if len(number) > 0 and int(number) == 0:
            raise ValidationError("Invalid credit card.")

        if luhnpy.verify(number) is False:
            raise ValidationError("Invalid credit card.")

    @validates("expiration_date")
    def validate_expiration_date(self, expiration_date):
        if re.match(r'\d{2}/\d{4}', expiration_date) is None:
            raise ValidationError("The expiration_date isn't valid date.")

        expiration_date_parse = datetime.datetime.strptime(
            expiration_date, "%m/%Y"
        )

        if expiration_date_parse.date() < datetime.datetime.today().date():
            raise ValidationError(
                "The credit card it's expired")


class BuyerSchema(BuyerResponseSchema):
    email = fields.Str(
        required=True,
        validate=validate.Email(error='Not a valid email address'),
    )

    name = fields.Str(
        required=True,
    )

    @validates("cpf")
    def validate_cpf(self, cpf):

        if cpfcnpj.validate(cpf) is False:
            raise ValidationError("Invalid number.")


class PaymentBaseSchema(ModelSchema):
    buyer = fields.Nested(BuyerSchema)
    type = fields.Nested(TypeResponseSchema)
    client = fields.Nested(ClientResponseSchema)

    class Meta:
        model = Payment
        sqla_session = db.session

    @validates_schema
    def validate(self, data):
        if Client.query.filter(Client.id == data.get("X-CLIENT")).count() is 0:
            raise ValidationError(
                "Client does not exist.",
                status_code=http.client.FORBIDDEN, field_names="client")


class PaymentCreditCardSchema(PaymentBaseSchema):
    credit_card = fields.Nested(CardSchema, required=True)

    @post_load
    def add_extra_data(self, data):
        # Adding default type for payment with credit card.
        data["type_id"] = Type.CREDIT_CARD
        data["client_id"] = data.pop("X-CLIENT")
        return data


class PaymentBoletoSchema(PaymentBaseSchema):

    @post_load
    def add_extra_data(self, data):
        # Adding default type for payment with boleto.
        data["type_id"] = Type.BOLETO
        data["client_id"] = data.pop("X-CLIENT")
        return data
