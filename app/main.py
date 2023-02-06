from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseConfig

from app.outer.routers.router import api_router

app = FastAPI(
    title="agriculture-classification-backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix="/api"
)

BaseConfig.arbitrary_types_allowed = True
