from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter

from client_transaction.transaction.router import tr_router
from client_transaction.transaction.scheme import TransactionScheme

app = FastAPI()
app.include_router(tr_router)


@app.get("/")
def core() -> dict[str, str]:
    return {"hello": "world"}
