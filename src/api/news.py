import time

from fastapi import APIRouter, Depends
from typing import List
from fastapi_cache.decorator import cache
from ..models.news import News, News_Create, News_Updade
from ..services.news import NewsService
from ..models.auth import User
from ..services.auth import get_current_user



router = APIRouter(prefix='/news', tags=["News"])


@router.get('/all', response_model=List[News])
@cache(expire=40)
def get_all_news(service: NewsService = Depends(), user: User = Depends(get_current_user)):
    time.sleep(6)
    return service.get_list(user_id=user.id)


@router.get('/cat/{category}', response_model=List[News])
def get_news_by_cat(category: str, service: NewsService = Depends(), user: User = Depends(get_current_user)):
    return service.get_list_by_category(category=category, user_id=user.id)


@router.get('/{news_id}', response_model=News)
def get_news_by_id(news_id: int, service: NewsService = Depends(), user: User = Depends(get_current_user)):
    return service.get_by_id(news_id, user_id=user.id)


@router.post('/add', response_model=News)
def add_news(news_data: News_Create, service: NewsService = Depends(), user: User = Depends(get_current_user)):
    return service.create_news(news_data, user_id=user.id)


@router.put('/upd_news/{news_id}', response_model=News)
def update_news(news_id: int, news_data: News_Updade, service: NewsService = Depends(),
                user: User = Depends(get_current_user)):
    return service.update_news(news_id, news_data, user_id=user.id)


@router.delete('/delete_news/{news_id}')
def delete_news(news_id: int, service: NewsService = Depends(), user: User = Depends(get_current_user)):
    return service.delete(news_id, user_id=user.id)