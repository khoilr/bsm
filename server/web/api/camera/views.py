import json

from fastapi import APIRouter, FastAPI

from database.dao.camera import CameraDAO
from database.models.camera import CameraModel

router = APIRouter(prefix='/camera')


# Camera_Pydantic = pydantic_model_creator(CameraModel)

from server.services.redis.dependency import get_redis_pool
from loguru import logger
import asyncio 
from redis.asyncio import ConnectionPool, Redis
@router.get("/blabla")
async def listen_for_changes(app: FastAPI, polling_interval: int = 1):
    prev_value = None
    redis_pool =   app.state.redis_pool
    async with Redis(connection_pool=redis_pool) as redis:
        while True:
            current_value = await redis.get('key') 
            if prev_value != current_value:
                logger.info(f"Value changed to: {current_value}")
                prev_value = current_value
            else:
                logger.info(f"No changes detected")
@router.get('/')
async def getAllCamera():
    # cameraDAO= CameraDao()
    # cameras = await Camera_Pydantic.from_queryset(CameraModel.all())
    cameras = await  CameraModel.all()
    return json.dumps({
        "count": cameras.__sizeof__(),
        "data": [camera.id for camera in cameras]
    })


@router.get('/{id}')
async def getCameraByID(id: int):
    camera = await CameraDAO().get(id=id)
    if camera:
        # await Camera_Pydantic.from_tortoise_orm(camera)
        return {
            "status": 200,
            "data": camera.name
        }
    return {
        "status": 404,
        "msg": "Not found camera"
    }
