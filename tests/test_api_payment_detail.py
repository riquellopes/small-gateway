import pytest
from .factories import CreditCardPaymentFactory, BoletoPaymentFactory


@pytest.fixture
def credicardison():
    return CreditCardPaymentFactory.create()


@pytest.fixture
def boletison():
    return BoletoPaymentFactory.create()


def test_get_detail_of_credit_card_payment_id(test_client, credicardison):
    response = test_client.get(
        "/api/v1/payment/{}".format(credicardison.id))

    assert response.status_code == 200
    assert response.json['result']['id'] == credicardison.id


def test_get_detail_of_boleto_payment_id(test_client, boletison):
    response = test_client.get(
        "/api/v1/payment/{}".format(boletison.id))

    assert response.status_code == 200
    assert response.json['result']['id'] == boletison.id


def test_get_status_404_when_payment_not_found(test_client, credicardison, boletison):
    response = test_client.get("/api/v1/payment/1000")

    assert response.status_code == 404
