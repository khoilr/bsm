import json
import os
from fastapi import APIRouter,Request,Body
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests as rq
from ast import literal_eval

router = APIRouter(prefix='/webhook')

load_dotenv('telegram_bot.env')

TELEGRAM_BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAME_CHATID=os.getenv('TELEGRAME_CHATID')

# Camera_Pydantic = pydantic_model_creator(CameraModel)

def sendTelegramMessage(msg):
    url=f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=-{TELEGRAME_CHATID}&text={msg}'
    result=rq.get(url=url)
    return result;

@router.post('/')
async def getAllCamera(req:Request):
    data=await req.json()
    msg=data['msg']
    print(msg)
    respond = sendTelegramMessage(msg=msg)
    result=(respond.status_code==200)
    if(result):
        return JSONResponse({
            'status':200,
            "msg":'Success'
        })
    return JSONResponse({
            'status':respond.status_code,
            "msg":respond.json(),
        }
    )
   
@router.get('/test')
async def getAllCamera(req:Request):
    respond = sendTelegramMessage('Send test message from Webhook BMS')
    result=(respond.status_code==200)
    if(result):
        return JSONResponse({
            'status':200,
            "msg":'Success'
        })
    return JSONResponse({
            'status':respond.status_code,
            "msg":respond.json(),
        }
    )
    

