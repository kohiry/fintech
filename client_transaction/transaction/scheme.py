from enum import Enum

from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int = 1
    username: str = 'Big wallet'
    amount: float = 1000.0  # узкое место, уверен есть более надеждные способы для хранения денег во float


class TransactionStatus(Enum):
    SEND = 'SEND'
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class TransactionScheme(BaseModel):
    user: UserScheme
    cost: float = 10.2
    status: TransactionStatus = TransactionStatus.SEND
