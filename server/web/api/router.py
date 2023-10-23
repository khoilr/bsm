from fastapi.routing import APIRouter

from bms_server.web.api import authentication, imagelive, camera

api_router = APIRouter()
api_router.include_router(authentication.router)
api_router.include_router(imagelive.router)
api_router.include_router(camera.router,prefix='/camera')
