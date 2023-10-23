from tortoise import fields, models


class PersonModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    person_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    gender = fields.IntField()
    dob = fields.DatetimeField()
    phone = fields.CharField(max_length=15)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Person"
