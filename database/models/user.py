from tortoise import fields, models
import datetime
from tortoise.queryset import QuerySet
from tortoise.fields.relational import _NoneAwaitable


class UserModel(models.Model):
    """Data model for user."""

    # Fields
    user_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    name = fields.CharField(max_length=200)
    username = fields.CharField(max_length=200, unique=True)
    password = fields.CharField(max_length=200)
    manager = fields.BooleanField()

    # relationship
    person = fields.OneToOneField("models.PersonModel", related_name="user_person")

    class Meta:
        table = "User"

    def to_json(self):
        model_data = {}
        for field_name, field_object in self._meta.fields_map.items():
            value = getattr(self, field_name)
            if isinstance(
                field_object,
                (fields.ForeignKeyField.__class__, fields.OneToOneField.__class__),
            ):
                value = value.id if value else None
            elif isinstance(value, datetime.datetime):
                value = int(round(value.timestamp())) if value else None
            elif isinstance(value, (fields.ReverseRelation, _NoneAwaitable)):
                continue
            model_data[field_name] = value
        return {
            key: value
            for key, value in model_data.items()
            if not isinstance(value, QuerySet)
        }
