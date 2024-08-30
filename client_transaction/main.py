from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter
from starlette.middleware.cors import CORSMiddleware

from transaction.router import tr_router
from transaction.scheme import TransactionScheme

app = FastAPI()
app.include_router(tr_router)

origins = [
    "http://localhost",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)


@app.get("/")
def core() -> dict[str, str]:
    return {"hello": "world"}
