from typing import Any, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.dependency import get_db
from app.datastore.commands.tags.create import CreateTagCommand
from app.datastore.commands.tags.delete import DeleteTagCommand
from app.datastore.commands.tags.update import UpdateTagCommand
from app.datastore.queries.tags.list import TagsQuery
from app.schemas.tags import TagCreate, TagDb

router = APIRouter()


@router.get("/", response_model=List[TagDb])
def read_articles(db: Session = Depends(get_db)) -> Any:
    return TagsQuery().get_tags(db=db)


@router.post('/', response_model=TagDb)
def create_article(tag: TagCreate, db: Session = Depends(get_db)) -> Any:
    return CreateTagCommand(payload=tag).create_tag(db=db)


@router.put('/{tag_id}', response_model=TagDb)
def update_article(tag_id: int, tag: TagCreate, db: Session = Depends(get_db)) -> Any:
    return UpdateTagCommand(payload=tag, tag_id=tag_id).update_tag(db=db)


@router.delete('/{tag_id}', response_model=TagDb)
def delete_article(tag_id: int, db: Session = Depends(get_db)) -> Any:
    tag = DeleteTagCommand(tag_id=tag_id).delete_tag(db=db)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag
