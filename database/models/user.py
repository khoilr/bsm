from tortoise import fields, models


class UserModel(models.Model):
    """Data model for user."""

    # Fields
    user_id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    name = fields.CharField(max_length=200)
    username = fields.CharField(max_length=200, unique=True)
    password = fields.CharField(max_length=200)
    manager = fields.BooleanField()

    # relationship
    person = fields.OneToOneField('models.PersonModel', related_name='user_person')

    class Meta:
        table = "User"
