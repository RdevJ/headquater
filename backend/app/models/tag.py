from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from app.db.base_class import Base


class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
