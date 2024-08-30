from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # auth
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = '.env'


settings = Settings()
