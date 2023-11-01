from tortoise import fields, models
import datetime
from tortoise.queryset import QuerySet


class EventModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    id = fields.IntField(pk=True)
    description = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Event"

    def to_json(self):
        model_data = {}
        for field_name, field_object in self._meta.fields_map.items():
            value = getattr(self, field_name)
            if isinstance(field_object, (fields.ForeignKeyField.__class__, fields.OneToOneField.__class__)):
                value = value.id if value else None
            elif isinstance(value, datetime.datetime):  
                value = int(round(value.timestamp())) if value else None
            model_data[field_name] = value
        return {key: value for key, value in model_data.items() if not isinstance(value, QuerySet)}
