from ninja import ModelSchema, Schema
from .models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email", "password", "username", "first_name", "last_name", "data_nascimento", "tipo"]


class MessageSchema(Schema):
    message: str
    errors: dict = None

class AuthSchema(Schema):
    email: str
    password: str
    callbackUrl: str
    nome: str