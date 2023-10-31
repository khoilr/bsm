import json

from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_model_creator

from database.dao.camera import CameraDAO
from database.models.camera import CameraModel

router = APIRouter(prefix='/camera')


# Camera_Pydantic = pydantic_model_creator(CameraModel)


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
