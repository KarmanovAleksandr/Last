from pydantic import BaseModel
from datetime import date


class News_Base(BaseModel):
    header: str
    created_at: date
    category: str
    text: str

    class Config:
        from_attributes=True
        orm_mode = True


class News(News_Base):
    id: int


class News_Create(News_Base):
    pass


class News_Updade(News_Base):
    pass