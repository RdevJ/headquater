from app.api.v1.endpoints import answer, article, question, tag
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(article.router, prefix='/articles', tags=['articles'])
api_router.include_router(tag.router, prefix='/tags', tags=['tags'])
api_router.include_router(answer.router, prefix='/answers', tags=['answers'])
api_router.include_router(question.router, prefix='/questions', tags=['questions'])
api_router.include_router(question.router, prefix='/quiz', tags=['quiz'])
