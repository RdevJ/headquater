from pydantic import BaseModel


class TagDb(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TagCreate(BaseModel):
    name: str
