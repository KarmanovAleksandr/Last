from fastapi import APIRouter
from .news import router as router_news
from .auth import router as router_auth


router = APIRouter()
router.include_router(router_auth)
router.include_router(router_news)