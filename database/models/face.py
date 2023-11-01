from tortoise import fields, models
import os
import io
import uuid
from tortoise.fields import TextField
from io import IOBase
import datetime
from tortoise.queryset import QuerySet


def is_binary_file(file_path: str) -> bool:
    """
    Check if the file is stored as binary file.

    Args:
        file_path (str): Path to file

    Returns:
        bool: Binary file or not
    """
    TEXTCHARS = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
    with open(file_path, 'rb') as f:
        content = f.read(1024)
        return bool(content.translate(None, TEXTCHARS))


class ConfigurationError(Exception):
    """Configuration Error."""

    def __init__(self, message):
        super().__init__(message)


class FileField(TextField):
    """Alternative classes for image storing using binary values."""

    def __init__(self, *, upload_root: str, **kwargs):
        super().__init__(**kwargs)
        if not os.path.exists(self.upload_root):
            raise ConfigurationError('No such directory: {}'.format(self.upload_root))

        self.upload_root = upload_root

    def _is_binary(self, file: IOBase):
        return not isinstance(file, io.TextIOBase)

    def to_db_value(self, value: IOBase, instance):
        is_binary = self._is_binary(value)
        if hasattr(value, 'name'):
            name = value.name
        else:
            name = str(uuid.uuid4())

        if os.path.isfile(os.path.join(self.upload_root, name)):
            name = '{}-{}'.format(str(uuid.uuid4()), name)

        mode = 'w' if not is_binary else 'wb'

        path = os.path.join(self.upload_root, name)

        with open(path, mode) as f:
            f.write(value.read())

        return path

    def to_python_value(self, value: str):
        if is_binary_file(value):
            mode = 'rb'
            buffer = io.BytesIO()
        else:
            mode = 'r'
            buffer = io.StringIO()

        buffer.name = os.path.split(value)[-1]

        with open(value, mode) as f:
            buffer.write(f.read())

        buffer.seek(0)
        return buffer


class FaceModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    face_id = fields.IntField(pk=True)
    FrameFilePath = fields.TextField(null=True)
    X = fields.FloatField(null=True)
    Y = fields.FloatField(null=True)
    Width = fields.IntField(null=True)
    Height = fields.IntField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # relationship
    person = fields.ForeignKeyField("models.PersonModel", related_name="person_model")

    class Meta:
        table = "Face"

    def to_json(self):
        model_data = {}
        for field_name, field_object in self._meta.fields_map.items():
            value = getattr(self, field_name)
            if isinstance(field_object, (fields.ForeignKeyField.__class__, fields.OneToOneField.__class__)):
                value = value.id if value else None
            elif isinstance(value, datetime.datetime):
                value = int(round(value.timestamp())) if value else None
            elif isinstance(value,(fields.ReverseRelation)):
                continue
            model_data[field_name] = value
        return {key: value for key, value in model_data.items() if not isinstance(value, QuerySet)}
