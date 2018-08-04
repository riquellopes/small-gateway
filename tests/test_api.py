import pytest
from .factories import TypeFactory, ClientFactory


@pytest.fixture
def credit_card():
    return TypeFactory(id=1, name="credit card")


@pytest.fixture
def client():
    return ClientFactory(id=1, name="loja do gugu")


def test_should_get_status_301(test_client):
    response = test_client.get("/")

    assert response.status_code == 302


def test_should_get_status_200(test_client):
    response = test_client.get("/", follow_redirects=True)

    assert response.status_code == 200


def test_should_get_status_status_403_when_x_client_not_found(test_client, client):
    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": 1000})

    assert response.status_code == 403


def test_get_status_200_when_a_new_transaction_of_capture_is_done(test_client, credit_card, client):
    data = {
        "amount": 50,
        "buyer": {
            "name": "Will Smith",
            "email": "will.smith@example.com",
            "cpf": "93621378448"
        },
        "credit_card": {
            "holder_name": "Will Ferrell",
            "number": "4485114090992814",
            "expiration_date": "02/2050",
            "cvv": "850"
        }
    }

    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": client.id}, json=data)
    assert response.status_code == 200


def test_get_status_422_when_credit_card_it_is_not_a_number(test_client, credit_card, client):
    data = {
        "credit_card": {
            "holder_name": "Will Ferrell",
            "number": "xxxxxxxxxxxxxxxxx",
            "expiration_date": "02/2050",
            "cvv": "850"
        }
    }

    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": client.id}, json=data)
    assert response.status_code == 422

    data = response.json
    assert data['errors']['credit_card']['number'][0] == 'The credit card should be a numeral.'


def test_get_status_422_when_to_send_a_invalid_credit_card(test_client, credit_card, client):
    data = {
        "credit_card": {
            "holder_name": "Will Ferrell",
            "number": "4929941961046990",
            "expiration_date": "02/2050",
            "cvv": "850"
        }
    }

    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": client.id}, json=data)
    assert response.status_code == 422

    data = response.json
    assert data['errors']['credit_card']['number'][0] == 'Invalid credit card.'


def test_get_422_when_buyer_send_only_0000000000000000_as_number(
        test_client, credit_card, client):
    data = {
        "credit_card": {
            "holder_name": "Will Ferrell",
            "number": "0000000000000000",
            "expiration_date": "02/2050",
            "cvv": "850"
        }
    }

    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": client.id}, json=data)
    assert response.status_code == 422

    data = response.json
    assert data['errors']['credit_card']['number'][0] == 'Invalid credit card.'


def test_get_422_when_to_send_the_credit_card_expired(
        test_client, credit_card, client):
    data = {
        "credit_card": {
            "holder_name": "Will Ferrell",
            "number": "4485297637447408",
            "expiration_date": "02/2000",
            "cvv": "850"
        }
    }

    response = test_client.post(
        "/api/v1/capture/", headers={"X-CLIENT": client.id}, json=data)
    assert response.status_code == 422

    data = response.json
    assert data['errors']['credit_card']['expiration_date'][0] == "The credit card it's expired"
