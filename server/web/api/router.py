from fastapi.routing import APIRouter

from server.web.api import authentication, imagelive, camera,webhook

api_router = APIRouter()
api_router.include_router(authentication.router)
api_router.include_router(imagelive.router)
api_router.include_router(camera.router)
api_router.include_router(webhook.router)
