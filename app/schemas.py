# coding: utf-8
import http
import luhnpy
import datetime

from marshmallow import post_load, validates_schema, validates, ValidationError, fields
from marshmallow_sqlalchemy import ModelSchema
from app.models import Payment, Type, Client, Card
from app.db import db


class CardSchema(ModelSchema):

    class Meta:
        model = Card
        sqla_session = db.session

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
        expiration_date_parse = datetime.datetime.strptime(
            expiration_date, "%m/%Y"
        )

        if expiration_date_parse.date() < datetime.datetime.today().date():
            raise ValidationError(
                "The credit card it's expired")


class PaymentCreditCardSchema(ModelSchema):
    credit_card = fields.Nested(CardSchema)

    class Meta:
        model = Payment
        sqla_session = db.session

    @post_load
    def add_extra_data(self, data):
        # Adding default type for payment with credit card.
        data["type"] = Type.query.filter_by(
            id=Type.CREDIT_CARD).first()

        data["client_id"] = data.pop("X-CLIENT")
        return data

    @validates_schema
    def validate(self, data):
        if Client.query.filter(Client.id == data.get("X-CLIENT")).count() is 0:
            raise ValidationError(
                "Client does not exist.",
                status_code=http.client.FORBIDDEN, field_names="client")
