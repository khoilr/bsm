from tortoise import fields, models

class CameraModel(models.Model):
    """Tortoise-based camera model."""
    # Fields
    camera_id = fields.IntField(pk=True)
    camera_name = fields.CharField(max_length=256)
    is_for_attendance = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    zone = fields.ForeignKeyField("models.ZoneModel", related_name="Zone_camera")
    face_logs = fields.ReverseRelation["models.RegisteredFaceModel"]
    attendance_logs = fields.ReverseRelation["models.AttendaceTrackingModel"]
    user = fields.ReverseRelation["models.UserModel"]


    class Meta:
        table = "Camera"
