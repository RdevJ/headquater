from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagDb(TagBase):
    id: int

    class Config:
        orm_mode = True
