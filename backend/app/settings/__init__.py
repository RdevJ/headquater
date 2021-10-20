from pydantic import BaseSettings

from app.settings.general import GeneralSettings


class Settings(
    GeneralSettings,
    BaseSettings,
):
    pass


settings = Settings()
