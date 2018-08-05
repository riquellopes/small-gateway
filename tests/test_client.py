
def test_when_service_is_called_without_x_client_the_status_should_be_403(test_client):
    response = test_client.post(
        "/api/v1/credit-card/capture/")

    assert response.status_code == 403
    assert response.json['errors']['client'][0] == "Client does not exist."


def test_should_get_status_status_403_when_x_client_not_found(test_client):
    response = test_client.post(
        "/api/v1/credit-card/capture/", headers={"X-CLIENT": 1000})

    assert response.status_code == 403
    assert response.json['errors']['client'][0] == "Client does not exist."
