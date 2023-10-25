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
