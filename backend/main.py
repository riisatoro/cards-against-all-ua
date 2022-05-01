import typing

from fastapi import FastAPI


app = FastAPI()


@app.get('/health')
def health_check() -> str:
    return 'ok'
