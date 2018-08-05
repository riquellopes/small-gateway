
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
