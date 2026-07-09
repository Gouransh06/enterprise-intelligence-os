from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Intelligence OS"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()