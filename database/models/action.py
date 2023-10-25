from tortoise import fields, models


class ActionModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    id = fields.IntField(pk=True)
    percentage = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # Relationship
    camera = fields.OneToOneField("models.ZoneModel",
                                  related_name="camera_attendance")
    face = fields.ForeignKeyField("models.RegisteredFaceModel",
                                  related_name="face_tracking")
    # event = fields.ForeignKeyField("models.EventModel", related_name="action_event")
    log = fields.ForeignKeyField('models.EventLogModel', 'action_log')

    class Meta:
        table = "Action"
