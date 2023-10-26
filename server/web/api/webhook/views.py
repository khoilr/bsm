import json
import os
from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests as rq
from datetime import datetime as dt
from server.web.api.setting import *
router = APIRouter(prefix='/webhook')

load_dotenv('telegram_bot.env')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')


# Camera_Pydantic = pydantic_model_creator(CameraModel)

def sendTelegramMessage(msg):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=-{TELEGRAM_CHATID}&text={msg}'
    result = rq.get(url=url)
    return result


@router.post('/')
async def getAllCamera(req: Request):
    data = await req.json()
    msg = data['msg']
    print(msg)
    respond = sendTelegramMessage(msg=msg)
    result = (respond.status_code == 200)
    if (result):
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
async def hanldeDetection(req: Request):
    print(req)
    data = {}
    try:
        data = await req.json()
        # handle data receive
        dateTime = dt.fromtimestamp(int(data['Datetime']))
        fileName = str(data['FrameFilePath']).split('/').pop()
        faceID = int(data['FaceID'])
        respond = sendTelegramMessage(
            f'Detected person with face ID [{faceID}] in Zone 2 at {dateTime}\nImage detected:\n{SERVER_SCHEME}{SERVER_HOST}:{SERVER_PORT}/api/image/{fileName}')
        result = (respond.status_code == 200)
        if result:
            return JSONResponse({
                'status': 200,
                "msg": 'Message sent!'
            })

    except Exception as e:
        print("Error handle detection ", e)
        return JSONResponse({
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
    return JSONResponse(data)


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
