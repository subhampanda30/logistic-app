from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql://user:password@localhost/db_name"
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()