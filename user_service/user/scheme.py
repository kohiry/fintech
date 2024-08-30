from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    hashed_password: str
