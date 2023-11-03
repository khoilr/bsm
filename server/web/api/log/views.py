from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.dao.event_log import EventLogDAO
from database.dao.event import EventDAO
from database.dao.face import FaceDAO
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from server.web.api.utils import removeNoneParams

router = APIRouter(prefix="/log")


class LogDTO(BaseModel):
    video_url: str | None = Field(
        None,
    )
    image_id: str | None = Field(..., description="This field must not be empty")
    event: int | None = Field(None)
    face: int | None = Field(..., description="This field must not be empty")


@router.get("/")
async def getAllLog(faceID: Optional[int] = None):
    logs = await EventLogDAO.get_all()
    if faceID:
        logs = [log for log in logs if (str(log.face) == str(faceID))]
    print([log.to_json() for log in logs])
    return JSONResponse(
        {"count": logs.__len__(), "data": [log.to_json() for log in logs]}
    )


@router.get("/{id}")
async def getLogByID(
    id: str,
):
    try:
        logID = int(id)
        log = await EventLogDAO.get(logID)
        if log:
            return JSONResponse(log.to_json())
        else:
            return JSONResponse(
                status_code=400,
                content={"status": 400, "msg": f"Not found log with ID '{id}'"},
            )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "msg": e.__str__(),
            },
        )


@router.post("/")
async def createLog(log: LogDTO):
    try:
        params = {
            "video_url": log.video_url,
            "image_id": log.image_id,
            "event_id": log.event,
            "face_id": log.face,
        }
        # print(removeNoneParams(params=params))
        # if log.event:
        #     event = await EventDAO.get(int(log.event))
        #     print(event.to_json())
        #     params['event']=event
        # if log.face:
        #     face = await FaceDAO.get(int(log.face))
        #     print(face.to_json())
        #     params['face']=face
        print(removeNoneParams(params=params))
        createdLog = await EventLogDAO.create(**removeNoneParams(params=params))
        if createdLog:
            return JSONResponse(status_code=201, content=createdLog.to_json())
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"status": 400, "msg": e.__str__()}
        )


# @router.put("/{id}")
# async def updatePerson(person: LogDTO,id:str):
#     try:
#         personId = int(id)
#         params = {
#             "name": person.name,
#             "gender": person.gender,
#             "dob": person.dob,
#             "phone": person.phone,
#         }
#         print(removeNoneParams(params=params))
#         updatedPerson=await PersonDAO.update(person_id=personId,**removeNoneParams(params))
#         if updatedPerson:
#             return JSONResponse(status_code=200, content=updatedPerson.to_json())
#         else:
#             raise Exception('Not found person to update')
#     except Exception as e:
#         return JSONResponse(
#             status_code=400, content={"status": 400, "msg": e.__str__()}
#         )

# @router.delete("/{id}")
# async def deletePersonByID(id: str):
#     try:
#         personID=int(id)
#         deletedUser = await PersonDAO.delete(person_id=personID)

#         if deletedUser:
#             return JSONResponse(status_code=200, content={
#                 'status':200,
#                 'msg':f'Delete person with ID {id} succesfully'
#             })
#         else:
#             return JSONResponse(status_code=200, content={
#                 'status':200,
#                 'msg':'Not found person to delete'
#             })
#     except Exception as e:
#         return JSONResponse(
#             status_code=400, content={"status": 400, "msg": e.__str__()}
#         )
