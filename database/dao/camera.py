from typing import List, Optional, Union
from tortoise.contrib.pydantic import pydantic_model_creator
from database.models.camera import CameraModel


class CameraDao:
    """Class for accessing dummy table."""

    async def create(self, name: str) -> None:
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        await CameraModel.create(name=name)

    async def getOne(self, id: Optional[int] = None, ) -> Union[CameraModel, None]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        if id:
            query = CameraModel.filter(id=id).first()
            return await query
        return None

    async def getAll(self, limit: Optional[int] = 1000, offset: Optional[int] = 0) -> \
        List[CameraModel]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        result= await (CameraModel.all().offset(offset).limit(limit))
        return result

    async def filter(self, name: Optional[str] = None) -> List[CameraModel]:
        """
        Get specific dummy model.

        :param name: name of dummy instance.
        :return: dummy models.
        """
        query = CameraModel.all()
        if name:
            query = query.filter(name=name)
        return await query
