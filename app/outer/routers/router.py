from fastapi import APIRouter

from app.outer.interfaces.controllers import classification_controller, image_controller, type_controller

api_router = APIRouter()

api_router.include_router(type_controller.router)
api_router.include_router(classification_controller.router)
api_router.include_router(image_controller.router)
