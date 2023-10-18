from tortoise import fields, models

class RegisteredFaceModel(models.Model):
    """Tortoise-based log model."""
    # Fields
    face_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    #Relationship
    person = fields.ForeignKeyField("models.PersonModel", related_name="personmodel")
    class Meta:
        table = "Face"
