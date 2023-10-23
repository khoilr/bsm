from tortoise import fields, models


class EventModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    id = fields.IntField(pk=True)
    description = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Event"
