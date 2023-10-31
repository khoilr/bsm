from tortoise import fields, models


class CameraModel(models.Model):
    """Tortoise-based camera model."""
    # Fields
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.CharField(max_length=256)
    connect_uri = fields.CharField(max_length=256)
    # type like socket, stream, ezviz,...
    type = fields.IntField()

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # Relationship
    zone = fields.ForeignKeyField("models.ZoneModel")

    # user = fields.ReverseRelation["models.UserModel"]

    class Meta:
        table = "Camera"

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
