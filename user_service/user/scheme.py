from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    hashed_password: str


class UserScheme(BaseModel):
    username: str
    password: str
    amount: int | None = 1000

