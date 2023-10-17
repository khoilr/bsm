from tortoise import fields, models

class CameraModel(models.Model):
    """Tortoise-based camera model."""
    # Fields
    camera_id = fields.IntField(pk=True)
    camera_name = fields.CharField(max_length=256)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    zone = fields.ForeignKeyField("models.ZoneModel")
    user = fields.ReverseRelation["models.UserModel"]


    class Meta:
        table = "Camera"
