import time

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from auth.router import router as auth_router
from operations.router import router as operation_router


app = FastAPI(title="Trading App")

app.include_router(auth_router)
app.include_router(operation_router)


@app.get("/long_operation")
@cache(expire=60)
async def index():
    time.sleep(4)
    return dict(hello="world")


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="trading-app-cache")


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", log_level="info", reload=True)
