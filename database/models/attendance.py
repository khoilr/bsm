from tortoise import fields, models


class AttendaceTrackingModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    tracking_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # Relationship
    camera = fields.ForeignKeyField("models.ZoneModel",
                                    related_name="cameramodel_attendance")
    face = fields.ForeignKeyField("models.RegisteredFaceModel",
                                  related_name="facemodel_tracking")

    class Meta:
        table = "AttendanceTracking"

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
