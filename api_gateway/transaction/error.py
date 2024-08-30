from fastapi import HTTPException


def get_error_transaction_failed() -> HTTPException:
    return HTTPException(status_code=500, detail="Transaction failed")

