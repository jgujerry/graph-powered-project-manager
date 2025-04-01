from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from app.routes import health, project

__version__ = "0.0.1"


@asynccontextmanager
async def lifesapn(app: FastAPI):
    """FastAPI application lifespan - Handles database connection"""
    mongodb_uri = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DATABASE}"
    app.mongodb_client = AsyncIOMotorClient(mongodb_uri)
    app.mongodb = app.mongodb_client[settings.MONGO_DATABASE]
    
    yield
    
    app.mongodb_client.close()


app = FastAPI(
    title="GPPM API",
    version=__version__,
    debug=settings.DEBUG,
    lifespan=lifesapn,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
    allow_credentials=False,  # TODO: update based on requirement
)

app.include_router(health.router, prefix="/api")
app.include_router(project.router, prefix="/api")
