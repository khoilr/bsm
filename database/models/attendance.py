from tortoise import fields, models

class AttendaceTrackingModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    tracking_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    camera = fields.ForeignKeyField("models.ZoneModel", related_name="cameramodel_attendance")
    face = fields.ForeignKeyField("models.RegisteredFaceModel", related_name="facemodel_tracking")
    class Meta:
        table = "AttendanceTracking"
