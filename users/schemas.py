from ninja import ModelSchema, Schema
from .models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email", "password", "username", "first_name", "last_name", "data_nascimento"]


class TypeSchema(Schema):
    type: str


class TypeUserSchema(Schema):
    user: UserSchema
    type_user: TypeSchema


class MessageSchema(Schema):
    message: str