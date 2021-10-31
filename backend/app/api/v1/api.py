from fastapi import APIRouter

from app.api.v1.endpoints import article
from app.api.v1.endpoints import tag

api_router = APIRouter()
api_router.include_router(article.router, prefix='/articles', tags=['articles'])
api_router.include_router(tag.router, prefix='/tags', tags=['tags'])
