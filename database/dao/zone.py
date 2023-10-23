from typing import List, Optional, Union

from bms_server.db.models.zone import ZoneModel


class ZoneDao:
    """Class for accessing dummy table."""

    async def create(self, name: str) -> None:
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        await ZoneModel.create(name=name)

    async def getOne(self, id: Optional[int]=None,) -> Union[ZoneModel, None]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        if id:
            query = ZoneModel.filter(id=id).first()
            return await query
        return None

    async def getAll(self, limit: int, offset: int) -> List[ZoneModel]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        return await ZoneModel.all().offset(offset).limit(limit)

    async def filter(self, name: Optional[str] = None) -> List[ZoneModel]:
        """
        Get specific dummy model.

        :param name: name of dummy instance.
        :return: dummy models.
        """
        query = ZoneModel.all()
        if name:
            query = query.filter(name=name)
        return await query
