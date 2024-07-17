from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}
