from tortoise import fields, models


class EventLogModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    id = fields.IntField(pk=True)
    video_url = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # relationship
    event = fields.ForeignKeyField("models.EventModel", related_name="log_event")

    class Meta:
        table = "EventLog"

    def to_json(self):
        model_data = {}
        for field_name, field_object in self._meta.fields_map.items():
            value = getattr(self, field_name)
            if isinstance(field_object, (fields.ForeignKeyField, fields.OneToOneField)):
                value = value.id if value else None
            elif isinstance(value, fields.DatetimeField):
                value = value.isoformat() if value else None
            model_data[field_name] = value
        return model_data
