# coding: utf-8
from app.db import db
from factory import SubFactory
from factory.alchemy import SQLAlchemyModelFactory as Factory
from app.models import Client, Buyer, Card, Type, Payment


class ClientFactory(Factory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"


class BuyerFactory(Factory):
    class Meta:
        model = Buyer
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"


class CardFactory(Factory):
    class Meta:
        model = Card
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"


class TypeFactory(Factory):
    class Meta:
        model = Type
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"


class PaymentFactory(Factory):

    class Meta:
        model = Payment
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    card = SubFactory(CardFactory)
    type = SubFactory(TypeFactory)
    buyer = SubFactory(BuyerFactory)
    client = SubFactory(ClientFactory)
