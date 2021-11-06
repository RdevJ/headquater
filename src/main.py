from fastapi import FastAPI

from app.api.v1.api import api_router
from app.settings import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)
