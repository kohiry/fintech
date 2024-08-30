from fastapi import HTTPException


def get_error_user_not_authenticate() -> HTTPException:
    return HTTPException(status_code=401, detail="Login User failed")
