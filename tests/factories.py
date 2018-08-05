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

    id = 1
    name = "Loja do GuGu"


class BuyerFactory(Factory):
    class Meta:
        model = Buyer
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    name = "Will Smith"
    email = "will@example.com"
    cpf = "66435618259"


class CardFactory(Factory):
    class Meta:
        model = Card
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    holder_name = "Will Ferrell"
    number = "4024007189386575"
    expiration_date = "20/2050"
    cvv = "185"


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

    credit_card = SubFactory(CardFactory)
    type = SubFactory(TypeFactory)
    buyer = SubFactory(BuyerFactory)
    client = SubFactory(ClientFactory)


class BoletoPaymentFactory(Factory):

    class Meta:
        model = Payment
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    type = SubFactory(TypeFactory)
    buyer = SubFactory(BuyerFactory)
    client = SubFactory(ClientFactory)
