

def test_should_get_status_301(test_client):
    response = test_client.get("/")

    assert response.status_code == 302


def test_should_get_status_200(test_client):
    response = test_client.get("/", follow_redirects=True)

    assert response.status_code == 200


def _test_should_get_status_status_403_when_x_client_not_found(test_client):
    response = test_client.post(
        "/api/v1/capture/", headers={"x-client": 1000})

    assert response.status_code == 403
