import json
import os
from fastapi import APIRouter, Request, Body, UploadFile, File, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests as rq
from datetime import datetime as dt
from server.web.api.setting import *
from typing import Optional, Annotated, BinaryIO

router = APIRouter(prefix='/webhook')

load_dotenv('telegram_bot.env')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')


# Camera_Pydantic = pydantic_model_creator(CameraModel)

def sendTelegramMessage(msg):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=-{TELEGRAM_CHATID}&text={msg}'
    result = rq.get(url=url)
    return result


def sendTelegramPhotoMsg(caption: str, filePath: str):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto?chat_id=-{TELEGRAM_CHATID}'
    fileData = (open(filePath, 'rb'))
    formData = {'photo': fileData, }
    print(formData)
    result = rq.post(url=url, files=formData, data={'caption': caption})
    return result


def sendTelegramPhotoMsg(caption: str, fileData: BinaryIO):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto?chat_id=-{TELEGRAM_CHATID}'
    # fileData = (open(filePath, 'rb'))
    formData = {'photo': fileData, }
    print(formData)
    result = rq.post(url=url, files=formData, data={'caption': caption})
    return result


@router.post('/')
async def getAllCamera(req: Request):
    data = await req.json()
    msg = data['msg']
    print(msg)
    respond = sendTelegramMessage(msg=msg)
    result = (respond.status_code == 200)
    if result:
        return JSONResponse({
            'status': 200,
            "msg": 'Success'
        })
    return JSONResponse({
        'status': respond.status_code,
        "msg": respond.json(),
    })


# data = {'Datetime': 1698305376, 'FrameFilePath': 'camera_web/images/frames/272afb1e-8f18-47e2-b77f-062b5183d70f.jpg',
#         'Confidence': 4.284321115759667, 'X': 313, 'Y': 321, 'Width': 74, 'Height': 74, 'FaceID': 1}


@router.post('/detection')
async def hanldeDetection(
        # file: Annotated[bytes, File()],
        photo: Annotated[UploadFile, File(...)],
        data: Annotated[str, Form()],
):
    try:
        print("File data:", photo.file)
        # print(data)
        jsonData=json.loads(data)
        print('Json data:',jsonData)
        
        # handle data receive
        dateTime = dt.fromtimestamp(int(jsonData['Datetime']))
        # fileName = str(data['FrameFilePath']).split('/').pop()
        # faceID = int(data['FaceID'])
        # respond = sendTelegramMessage(
        #     f'Detected person with face ID [{faceID}] in Zone 2 at {dateTime}\nImage detected:\n{SERVER_SCHEME}{SERVER_HOST}:{SERVER_PORT}/api/image/{fileName}')
        # result = (respond.status_code == 200)
        respond = sendTelegramPhotoMsg(
            f'Có người xuất hiện tại Zone 2 lúc {dateTime}', fileData=photo.file)
        result = (respond.status_code == 200)

        # result = True
        if result:
            print(respond.json())
            return JSONResponse({
                'status': 200,
                "msg": 'Message sent!'
            })
        print("DOne")

    except Exception as e:
        print(e.__cause__)
        return JSONResponse(
            status_code=200, content={
            'status': 400,
            "msg": 'Error hanlde data',
            'error:': e.__str__(),
        })

    # respond = sendTelegramMessage(msg=msg)
    # result = (respond.status_code == 200)
    # if (result):
    #     return JSONResponse({
    #         'status': 200,
    #         "msg": 'Success'
    #     })
    # return JSONResponse({
    #     'status': respond.status_code,
    #     "msg": respond.json(),
    # })
    # return JSONResponse({data})


@router.get('/test')
async def getAllCamera(req: Request):
    respond = sendTelegramMessage('Send test message from Webhook BMS')
    result = (respond.status_code == 200)
    if result:
        return JSONResponse({
            'status': 200,
            "msg": 'Success'
        })
    return JSONResponse({
        'status': respond.status_code,
        "msg": respond.json(),
    }
    )
