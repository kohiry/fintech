from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter

from api_gateway.transaction.router import tr_router

app = FastAPI()
app.include_router(tr_router)


@app.get("/")
def core() -> dict[str, str]:
    return {"hello": "world"}
