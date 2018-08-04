# coding: utf-8
import http
from marshmallow import post_load, validates_schema, ValidationError
from marshmallow_sqlalchemy import ModelSchema
from app.models import Payment, Type, Client
from app.db import db


class PaymentCreditCardSchema(ModelSchema):

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
