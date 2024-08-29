from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter

app = FastAPI()


@app.get("/")
def core() -> dict[str, str]:
    return {"hello": "world"}
