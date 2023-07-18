from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import tables
from ..models.news import News_Create, News_Updade


class NewsService:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def _get(self,news_id: int, user_id: int) -> tables.News:
        news = (
            self.session
            .query(tables.News)
            .filter_by(id=news_id, user_id = user_id)
            .first()
        )
        if not news:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return news

    def get_list(self, user_id: int) -> List[tables.News]:
        news = (
            self.session
            .query(tables.News)
            .filter_by(user_id = user_id)
            .all()
        )
        return news

    def get_by_id(self, news_id: int, user_id: int) -> tables.News:
        return self._get(news_id, user_id)

    def get_list_by_category(self, category: str, user_id: int) -> List[tables.News]:
        news = (
            self.session
            .query(tables.News)
            .filter_by(category=category)
            .all()
        )
        return news

    def create_news(self, news_data: News_Create, user_id: int) -> tables.News:
        news = tables.News(**news_data.dict(), user_id=user_id,)
        self.session.add(news)
        self.session.commit()
        return news

    def update_news(self, news_id: int, news_data: News_Updade, user_id: int) -> tables.News:
        news = self._get(news_id, user_id)
        for field, value in news_data:
            setattr(news, field, value)
        self.session.commit()
        return news

    def delete(self, news_id: int, user_id: int) -> None:
        news = self._get(news_id, user_id)
        self.session.delete(news)
        self.session.commit()