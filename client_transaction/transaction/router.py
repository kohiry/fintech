from fastapi import APIRouter

from api_gateway.transaction.scheme import TransactionScheme

tr_router = APIRouter(prefix="/transaction", tags=["Transaction"])


@tr_router.post("/")
async def transaction_to_broker(transaction: TransactionScheme) -> TransactionScheme:
    # send to broker
    pass
