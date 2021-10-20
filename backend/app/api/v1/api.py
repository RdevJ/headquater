from fastapi import APIRouter

from app.api.v1.endpoints import article

api_router = APIRouter()
api_router.include_router(article.router, prefix='/articles', tags=['articles'])
