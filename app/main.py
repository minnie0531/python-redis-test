from fastapi import FastAPI
from .routers import router, redis_router
import yaml
import logging.config
import logging

# Set logging configuration
with open("./app/config/logging_config.yaml", "r") as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)

# Tags for representative endpoints
tags = [
    {
        "name": "routers",
        "description": "Operations with xxx",
    },
    {"name": "redis", "description": "Operation with redis"},
]

# Define Fast api and description
app = FastAPI(
    title="Garage MVP FastAPI MAS template",
    description="This is a template of python MSA used in Garage project.",
    version="0.0.1",
    openapi_tags=tags,
)

# Set logger name to project
logger = logging.getLogger("garage")
logger.warning("START Application")

# Add routers to main
app.include_router(router.router)
app.include_router(redis_router.router)
logger.debug("hello!!!!!!")

# This path is for health check or test
@app.get("/")
async def root():
    return {"Hello World :D"}
