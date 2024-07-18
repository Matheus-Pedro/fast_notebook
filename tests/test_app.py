import socket
from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_read_root_is_ok():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert


def test_read_root_return_hello_world_with_ip():
    client = TestClient(app)  # Arrange (Organizar)

    response = client.get('/')  # Act (Agir)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))

    assert response.json() == {
        'message': 'Hello World!',
        'IP': f'{s.getsockname()[0]}',
    }  # Assert (Afirmar)


def test_hello_world_is_real():
    client = TestClient(app)

    response = client.get('/hello')

    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    )
