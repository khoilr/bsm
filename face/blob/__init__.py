import requests
import os
from dotenv import load_dotenv

load_dotenv()

BLOB_HOST = os.environ.get("BLOB_HOST", "localhost")
BLOB_PORT = os.environ.get("BLOB_PORT", 30003)


def upload_blob(file_path):
    with open(file_path, "rb") as f:
        url = f"http://{BLOB_HOST}:{BLOB_PORT}/upload"
        method = "POST"
        files = {"file": f}
        response = requests.request(
            method,
            url,
            files=files,
            timeout=60,
        )

        return response.json()
