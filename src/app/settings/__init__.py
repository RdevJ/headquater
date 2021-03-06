from datetime import timedelta
from typing import Any, Dict, Optional

from pydantic import BaseSettings, validator
from pydantic.networks import PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    INITIAL_REPETITION_TIMEDELTA = timedelta(days=2)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = ".env"


settings = Settings()
