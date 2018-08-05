import pytest
from .factories import CreditCardPaymentFactory, BoletoPaymentFactory


@pytest.fixture
def mockisons(credit_card, boleto):
    CreditCardPaymentFactory.create(type=credit_card)
    BoletoPaymentFactory.create(type=boleto)


def test_get_status_200_when_call_payment_list(test_client):
    response = test_client.get("/api/v1/payment/")

    assert response.status_code == 200


def test_service_payment_list_should_get_2_results(test_client, mockisons):
    response = test_client.get("/api/v1/payment/")

    assert response.status_code == 200
    assert len(response.json['results']) == 2
