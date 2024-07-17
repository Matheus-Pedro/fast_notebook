from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_read_root_is_ok():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert


def test_read_root_return_hello_world():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (Ação)

    assert response.json() == {'message': 'Hello World!'}  # Assert
