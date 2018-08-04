# coding: utf-8
import http
from marshmallow import post_load, validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import ModelSchema
from app.models import Payment, Type, Client, Card
from app.db import db


class CardSchema(ModelSchema):

    class Meta:
        model = Card
        sqla_session = db.session

    @validates_schema
    def validate(self, data):
        number = data.get("number")

        if number.isdigit() is False:
            raise ValidationError(
                "The credit card should be a numeral.", field_names="number")

        if len(number) > 0 and int(number) == 0:
            raise ValidationError(
                "Credit card is invalid.", field_names="number")


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
                "Client does not exist.", status_code=http.client.FORBIDDEN)
