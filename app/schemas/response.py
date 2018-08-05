from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from app.models import Payment, Client, Type, Buyer, Card
from app.db import db


class CardResponseSchema(ModelSchema):

    class Meta:
        model = Card
        sqla_session = db.session


class BuyerResponseSchema(ModelSchema):

    class Meta:
        model = Buyer
        sqla_session = db.session


class TypeResponseSchema(ModelSchema):

    class Meta:
        model = Type
        sqla_session = db.session


class ClientResponseSchema(ModelSchema):

    class Meta:
        model = Client
        sqla_session = db.session


class PaymentReponseSchema(ModelSchema):
    buyer = fields.Nested(BuyerResponseSchema)
    type = fields.Nested(TypeResponseSchema)
    client = fields.Nested(ClientResponseSchema)
    credit_card = fields.Nested(CardResponseSchema)

    class Meta:
        model = Payment
        sqla_session = db.session
