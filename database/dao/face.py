from typing import List, Optional, Union

from database.models.face import FaceModel


class FaceDAO:
    """Class for accessing face table."""

    async def create(self, frame: str, picture: str, boundary: list[int]) -> FaceModel:
        """
        Add single face to session.

        Args:
            frame (str): face frame
            picture (str): face picture
            boundary (list[int]): boundary array

        Returns:
            FaceModel: Face model.
        """
        return await FaceModel.create(
            frame=frame,
            picture=picture,
            boundary=boundary
        )

    async def get_all(self, limit: int, offset: int) -> List[FaceModel]:
        """
        Get all Face models with limit/offset pagination.

        Args:
            limit (int): limit of dummies.
            offset (int): offset of dummies.

        Returns:
            List[FaceModel]: face models.
        """
        return await FaceModel.all().offset(offset).limit(limit)

    async def filter(self, frame:  Optional[str] = None, picture:  Optional[str] = None, boundary:  Optional[list[int]] = None) -> List[FaceModel]:
        """
        Get specific face model.

        Args:
            frame (Optional[str], optional): face frame. Defaults to None.
            picture (Optional[str], optional): face picture. Defaults to None.
            boundary (Optional[list[int]], optional): boundary array. Defaults to None.

        Returns:
            List[FaceModel]: user models.
        """
        query = FaceModel.all()
        try:
            query = query.filter(frame=frame, picture=picture, boundary=boundary)
        except:
            return None
        return await query

    async def get(
        self,
        face_id: Optional[int] = None,
        picture: Optional[str] = None,
    ) -> Union[FaceModel, None]:
        """
        Get specific face model.

        Args:
            face_id (Optional[int], optional): face id. Defaults to None.
            picture (Optional[str], optional): picture. Defaults to None.

        Returns:
            Union[FaceModel, None]: face object, return None if none exists
        """
        query = FaceModel.all()
        if face_id:
            query = query.filter(face_id=face_id).first()
        elif picture:
            query = query.filter(picture=picture).first()
        else:
            return None
        return await query
