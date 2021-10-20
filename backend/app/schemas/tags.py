from pydantic import BaseModel


class Tag(BaseModel):
    label: str
