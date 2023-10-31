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
