import json
import os

import requests as rq
from dotenv import load_dotenv
from requests_toolbelt import MultipartEncoder
import numpy as np

############REMOTE ENV#############
load_dotenv()
############LOCAL ENV##############
# load_dotenv('server.env')
###################################
SERVER_SCHEME =os.getenv('SERVER_SCHEME')
SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.getenv('SERVER_PORT')

print(f'API URL: {SERVER_SCHEME}{SERVER_HOST}:{SERVER_PORT}')

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def handleFaceDetected(data: dict):
    try:
        url = f'{SERVER_SCHEME}{SERVER_HOST}:{SERVER_PORT}/api/webhook/detection'
        print("Data send:", data)
        print(os.getcwd() + '/' + data['FrameFilePath'])
        f = open(file=os.getcwd() + '/' + data['FrameFilePath'], mode='rb')
        files = [
            ('photo', f)
        ]

        data = json.dumps(data, cls=NpEncoder)

        print(url)
        # data = json.dumps(data, cls=NpEncoder)
        respond = rq.post(url, files=files, data={'data': data})
        print(respond.text)
        print(respond.headers['Content-Type'])
    except Exception as e:
        print("Error call API")
        # print(e.with_traceback())
