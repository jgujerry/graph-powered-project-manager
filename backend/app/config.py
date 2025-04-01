import os

from pydantic_settings import BaseSettings

__all__ = ["settings"]


class BaseSettings(BaseSettings):
    # ENVIRONMENT
    FASTAPI_ENV: str
    
    # fASTAPI
    DEBUG: str = False
    SECRET_KEY: str = "<abc123>"
    
    # CORS
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    
    # MONGO
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_DATABASE: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str


class DevSettings(BaseSettings):
    FASTAPI_ENV: str = "dev"
    DEBUG: bool = True


class ProdSettings(BaseSettings):
    FASTAPI_ENV: str = "prod"
    SECRET_KEY: str = os.environ.get("FASTAPI_SECRET_KEY")


def get_settings(env):
    """Return configuration based on environment"""
    if env == "prod":
        return ProdSettings()

    if env == "dev":
        return DevSettings()

    raise ValueError(f"Not a valid environment, please use 'dev' or 'prod'")


settings = get_settings(os.getenv("FASTAPI_ENV", "dev"))
