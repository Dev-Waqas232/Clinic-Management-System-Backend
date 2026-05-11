from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DB_URL: str
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    JWT_ACCESS_SECRET: str
    JWT_REFRESH_SECRET: str
    EMAIL_HOST: str
    EMAIL_PORT: str
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: SecretStr
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


settings = Settings()  # type: ignore
