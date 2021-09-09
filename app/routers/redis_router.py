from fastapi import APIRouter
from app.redis.redis import Redis
import logging
import json
import os
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

"""
This Module is for query endpoints.

Client can access this application through GET/POST/PUT/DELETE /queries

"""

router = APIRouter()
redis = Redis()
logger = logging.getLogger("garage")


@router.get("/redis/set/keys/{key}", tags=["redis"], description="Test endpoint")
def redis_set(key: str):

    if redis.check_exists_key(key):
        return {"The %s key already existed" % key}
    else:
        logger.info("new key")
        with open("test/test_data/redis_input.json") as f:
            data = json.load(f)

        redis.set_data(data, key)
        return {"Successfully registered"}


@router.get("/redis/get/keys/{key}", tags=["redis"], description="Test endpoint")
def redis_get(key: str):

    if redis.check_exists_key(key):
        logger.info("key exists")
        json_compatible_item_data = jsonable_encoder(redis.get_data(key))
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"The %s key is not existed" % key}
