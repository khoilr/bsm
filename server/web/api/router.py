from fastapi.routing import APIRouter

from server.web.api import authentication
from server.web.api import imagelive

api_router = APIRouter()
api_router.include_router(authentication.router)
api_router.include_router(imagelive.router)
