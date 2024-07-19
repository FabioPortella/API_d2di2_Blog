from ninja import Router
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

from .schemas import MessageSchema, UserSchema 
from .models import User


users_router = Router()

@users_router.post('/', response={201: UserSchema, 400: MessageSchema, 500: MessageSchema})
def create_user(request, user: UserSchema):
    try:
        user = User(**user.dict())
        user.password = make_password(user.password)
        user.full_clean()  # usar para reconhecer os validators
        user.save()
        return 201, user
    except ValidationError as e:
        return 400, MessageSchema(message='Erro de Validação', errors=e.message_dict)
    except Exception as e:
        return 500, {'errors': 'Erro ao criar usuário.'}
    