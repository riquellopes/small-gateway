
def test_get_status_200_and_get_number_of_boleto(test_client, boleto, client):
    data = {
        "amount": 50,
        "buyer": {
            "name": "Will Smith",
            "email": "will.smith@example.com",
            "cpf": "93621378448"
        }
    }

    response = test_client.post(
        "/api/v1/boleto/", headers={"X-CLIENT": client.id}, json=data)

    assert response.status_code == 200
    assert response.json["payment_code"] == "000001"


def test_get_status_422_when_to_put_a_invalid_cpf(test_client, boleto, client):
    data = {
        "amount": 50,
        "buyer": {
            "name": "Will Smith",
            "email": "will.smith@example.com",
            "cpf": "00000000000"
        }
    }

    response = test_client.post(
        "/api/v1/boleto/", headers={"X-CLIENT": client.id}, json=data)

    assert response.status_code == 422
    data = response.json
    assert data['errors']['buyer']['cpf'][0] == 'Invalid number.'


def test_should_get_status_422_when_to_send_the_invalid_email(test_client, boleto, client):
    data = {
        "amount": 50,
        "buyer": {
            "name": "Will Smith",
            "email": "xxxxxx",
            "cpf": "00000000000"
        }
    }

    response = test_client.post(
        "/api/v1/boleto/", headers={"X-CLIENT": client.id}, json=data)

    assert response.status_code == 422
    data = response.json

    assert data['errors']['buyer']['email'][0] == 'Not a valid email address'
