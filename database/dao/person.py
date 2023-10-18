from typing import List, Optional, Union

from database.models.person import PersonModel


class PersonDAO:
    """Class for accessing person table."""

    async def create(self, person_name: str) -> PersonModel:
        """
        Create new person object.

        Args:
            person_name (str): name of person

        Returns:
            PersonModel: person object
        """
        return await PersonModel.create(person_name=person_name)

    async def get_all(self, limit: int, offset: int) -> List[PersonModel]:
        """
        Get all person models with limit/offset pagination.

        Args:
            limit (int): limit of dummies.
            offset (int): offset of dummies.

        Returns:
            List[PersonModel]: all person.
        """
        return await PersonModel.all().offset(offset).limit(limit)

    async def get(
        self,
        person_name: Optional[str] = None,
    ) -> Union[PersonModel, None]:
        """
        Get specific person model.

        Args:
            person_name (Optional[str], optional): person name. Defaults to None.

        Returns:
            Union[PersonModel, None]: person object, return None if none exists
        """
        if person_name:
            query = PersonModel.all().filter(person_name=person_name).first()
        else:
            return None
        return await query
