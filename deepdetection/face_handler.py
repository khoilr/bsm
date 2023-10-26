import json
import os

import requests as rq
from dotenv import load_dotenv
import numpy as np

load_dotenv()
SERVER_SCHEME = os.getenv('SERVER_SCHEME')
SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.getenv('SERVER_PORT')


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
        rq.post(url, data=json.dumps(data, cls=NpEncoder))
    except Exception as e:
        print("Error call API")
        print(e)
