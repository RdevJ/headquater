from typing import Any, Dict, Optional

from sqlalchemy.orm.session import Session


class CreateMixin(object):
    model: Any
    payload: Any

    def create(self, db: Session, data: Optional[Dict[str, Any]] = None) -> Any:
        payload = data or self.payload
        obj = self.model(**payload)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


class ReadAllMixin(object):
    def read_all(self, db: Session) -> Any:
        return db.query(self.model).all()
