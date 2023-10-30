
from fastapi import APIRouter, Request, Body


router = APIRouter(prefix='/image')

@router.get('/{id}')
async def getImageByID(imageID):
    print("ID receive "+str(imageID))
    # handle later