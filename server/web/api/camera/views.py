import json

from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_model_creator

from bms_server.db.dao.camera import CameraDao
from bms_server.db.models.camera import CameraModel

router = APIRouter()
Camera_Pydantic = pydantic_model_creator(CameraModel)


@router.get('/')
async def getAllCamera():
    # cameraDAO= CameraDao()
    cameras = await Camera_Pydantic.from_queryset(CameraModel.all())

    return json.dumps({
        "count": cameras.count(),
        "data": [camera.model_dump_json() for camera in cameras]
    })


@router.get('/{id}')
async def getCameraByID(id: int):
    camera = await CameraDao.getOne(id=id)
    if camera:
        await Camera_Pydantic.from_tortoise_orm(camera)
        return json.dumps({
            "status": 200,
            "data": camera
        })
    return {
        "status": 404,
        "msg": "Not found camera"
    }
