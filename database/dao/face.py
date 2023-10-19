from typing import List, Optional, Union

from database.models.face import RegisteredFaceModel


class FaceDAO:
    """Class for accessing face table."""

    async def create(self, frame: str, picture: str, boundary: list[int]) -> RegisteredFaceModel:
        """
        Add single face to session.

        Args:
            frame (str): face frame
            picture (str): face picture
            boundary (list[int]): boundary array

        Returns:
            RegisteredFaceModel: Face model.
        """
        return await RegisteredFaceModel.create(
            frame=frame,
            picture=picture,
            boundary=boundary
        )

    async def get_all(self, limit: int, offset: int) -> List[RegisteredFaceModel]:
        """
        Get all Face models with limit/offset pagination.

        Args:
            limit (int): limit of dummies.
            offset (int): offset of dummies.

        Returns:
            List[RegisteredFaceModel]: face models.
        """
        return await RegisteredFaceModel.all().offset(offset).limit(limit)

    async def filter(self, frame:  Optional[str] = None, picture:  Optional[str] = None, boundary:  Optional[list[int]] = None) -> List[RegisteredFaceModel]:
        """
        Get specific face model.

        Args:
            frame (Optional[str], optional): face frame. Defaults to None.
            picture (Optional[str], optional): face picture. Defaults to None.
            boundary (Optional[list[int]], optional): boundary array. Defaults to None.

        Returns:
            List[RegisteredFaceModel]: user models.
        """
        query = RegisteredFaceModel.all()
        try:
            query = query.filter(frame=frame, picture=picture, boundary=boundary)
        except:
            return None
        return await query

    async def get(
        self,
        face_id: Optional[int] = None,
        picture: Optional[str] = None,
    ) -> Union[RegisteredFaceModel, None]:
        """
        Get specific face model.

        Args:
            face_id (Optional[int], optional): face id. Defaults to None.
            picture (Optional[str], optional): picture. Defaults to None.

        Returns:
            Union[RegisteredFaceModel, None]: face object, return None if none exists
        """
        query = RegisteredFaceModel.all()
        if face_id:
            query = query.filter(face_id=face_id).first()
        elif picture:
            query = query.filter(picture=picture).first()
        else:
            return None
        return await query
