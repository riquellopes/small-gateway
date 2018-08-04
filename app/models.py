# coding: utf-8
from datetime import datetime
from app.db import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    holder_name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.String(10), nullable=False)
    cvv = db.Column(db.String(10), nullable=False)


class Type(db.Model):
    CREDIT_CARD = 1
    BOLETO = 2

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(10, 2))

    card_id = db.Column(db.Integer, db.ForeignKey(Card.id))
    type_id = db.Column(db.Integer, db.ForeignKey(Type.id), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey(Buyer.id), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(Buyer.id), nullable=False)

    # relationships
    card = db.relationship("Card", foreign_keys=[card_id])
    type = db.relationship("Type", foreign_keys=[type_id])
    buyer = db.relationship("Buyer", foreign_keys=[buyer_id])
    client = db.relationship("Client", foreign_keys=[client_id])

    created_date = db.Column(db.DateTime, default=datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
