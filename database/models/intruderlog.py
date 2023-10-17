from tortoise import fields, models

class LogModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    log_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    camera = fields.ForeignKeyField("models.ZoneModel",related_name="cameramodel")
    face = fields.ForeignKeyField("models.RegisteredFaceModel", related_name="facemodel")
    class Meta:
        table = "Log"
