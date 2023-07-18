import pika
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from .settings import settings
from .api import router
from .rabbit import add_message, read_message

app = FastAPI()

app.include_router(router)

@app.get("/")
def say_hello():
    return {"message": "server is working"}


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(settings.redis_url, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.post("/add_queue")
def msg(text):
    add_message(text)
    return {"text adding": "completed"}

@app.get("/read_queue")
def read():
    read_message()
    return {"message reading" : "started"}

