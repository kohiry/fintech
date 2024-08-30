from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter

from transaction.router import tr_router
from transaction.scheme import TransactionScheme

app = FastAPI()
app.include_router(tr_router)


@app.webhooks.post("transaction has coocked")
def new_subscription(body: TransactionScheme):
    """
    When a transaction coocked, we will send u status
    """
    # logic transaction


@app.get("/")
def core() -> dict[str, str]:
    return {"hello": "world"}
