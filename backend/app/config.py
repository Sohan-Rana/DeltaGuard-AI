from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """সব config environment variable থেকে আসে; কোনো secret hardcode নয়।"""

    app_env: str = "development"
    database_url: str = ""
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
