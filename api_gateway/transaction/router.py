import httpx
from fastapi import APIRouter

from transaction.scheme import TransactionScheme

tr_router = APIRouter(prefix="/transaction", tags=["Transaction"])


@tr_router.post("/")
async def transaction_send(transaction: TransactionScheme) -> TransactionScheme:

    # rpc to client service (coming soon)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post('', json=transaction.model_dump_json())
            response_data = response.json()
            print(response_data)
    except Exception as e:
        print(e)
        raise
    else:
        print(f'transaction: {transaction}, sent')
    finally:
        pass
    return transaction
