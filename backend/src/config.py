from typing import Optional

from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".docker/.env")

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: Optional[str] = "5432"
    DATABASE_URL: Optional[str] = None
    DEBUG: bool = False

    ZOOM_API_KEY: str
    ZOOM_API_SECRET: str
    ZOOM_USER_ID: str
    ZOOM_ACCOUNT_ID: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql+psycopg2://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
                f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
            )


settings = Settings()
