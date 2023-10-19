from tortoise import fields, models

class PersonModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    person_id = fields.IntField(pk=True)
    person_name = fields.CharField(max_length=200)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.person_name
    
    class Meta:
        table = "Person"
