from tortoise import fields, models


class EventLogModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    id = fields.IntField(pk=True)
    video_url = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # relationship
    event = fields.ForeignKeyField("models.EventModel", related_name="log_event")

    class Meta:
        table = "EventLog"
