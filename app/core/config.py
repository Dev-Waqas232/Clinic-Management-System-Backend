from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DB_URL: str
    PORT: int = 8000
    HOST: str = "0.0.0.0"


settings = Settings()  # type: ignore
