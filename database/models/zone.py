from tortoise import fields, models


class ZoneModel(models.Model):
    """Tortoise-based zone model."""
    # Fields
    zone_id = fields.IntField(pk=True)
    description = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Zone"
