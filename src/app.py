from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from .api import router
from .models.auth import User
from .rabbit import add_message, read_message
from .rabbit import message
from .services.auth import get_current_user
from .settings import settings

app = FastAPI()

app.include_router(router)


@app.get("/")
def say_hello():
    return message


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(settings.redis_url, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.post("/add_queue")
def msg(text, user: User = Depends(get_current_user)):
    add_message(text)
    return {"text adding": "completed"}


@app.get("/read_queue")
def read(user: User = Depends(get_current_user)):
    read_message()
    return {"message reading": "started"}
