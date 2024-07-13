from ninja import ModelSchema
from .models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email", "password", "username", "first_name", "last_name"]