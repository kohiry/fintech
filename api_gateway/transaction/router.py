from fastapi import APIRouter

from api_gateway.transaction.scheme import TransactionScheme

tr_router = APIRouter(prefix="/transaction", tags=["Transaction"])


@tr_router.post("/")
def transaction_send(transaction: TransactionScheme) -> TransactionScheme:
    return transaction
