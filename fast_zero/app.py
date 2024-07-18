import socket
from http import HTTPStatus

from fastapi import FastAPI  # type: ignore
from fastapi.responses import HTMLResponse  # type: ignore

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return {'message': 'Hello World!', 'IP': f'{s.getsockname()[0]}'}


@app.get('/hello', response_class=HTMLResponse)
def hello_world():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
