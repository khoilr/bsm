from tortoise import fields, models


class DummyModel(models.Model):
    """Model for demo purpose."""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)  # noqa: WPS432
    description=fields.CharField(max_length=155)

    def __str__(self) -> str:
        return self.name

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
