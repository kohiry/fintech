from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    P_DB: str
    P_USER: str
    P_PASS: str
    P_HOST: str
    P_PORT: int

    class Config:
        env_file = '.env'


settings = Settings()
