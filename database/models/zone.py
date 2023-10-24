from tortoise import fields, models
class ZoneModel(models.Model):
    """Tortoise-based zone model."""
    # Fields
    zone_id = fields.IntField(pk=True)
    zone_name = fields.CharField(max_length=255)
    zone_description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    #Relationship
    cameras = fields.ReverseRelation["CameraModel"]
    
    def __str__(self):
        return self.zone_name

    class Meta:
        table = "Zone"
