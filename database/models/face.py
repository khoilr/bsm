from tortoise import fields, models
from typing import List, Union, Type, Optional, Any
import json

from tortoise.fields.base import Field
from tortoise.models import Model


class IntArrayField(Field, list):
    """
    Int Array field specifically for PostgreSQL.

    This field can store list of int values.
    """

    SQL_TYPE = "int[]"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_db_value(
        self, value: List[int], instance: "Union[Type[Model], Model]"
    ) -> Optional[List[int]]:
        return value

    def to_python_value(self, value: Any) -> Optional[List[int]]:
        if isinstance(value, str):
            array = json.loads(value.replace("'", '"'))
            return [int(x) for x in array]
        return value
    
class RegisteredFaceModel(models.Model):
    """Tortoise-based face model."""
    # Fields
    face_id = fields.IntField(pk=True)
    frame = fields.TextField()
    picture = fields.TextField()
    boundary = IntArrayField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    person = fields.ForeignKeyField("models.PersonModel", related_name="personmodel")
    class Meta:
        table = "Face"
