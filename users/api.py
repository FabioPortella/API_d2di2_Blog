from ninja import Router
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

from .schemas import MessageSchema, TypeUserSchema, UserSchema 
from .models import User


users_router = Router()

@users_router.post('/', response={201: UserSchema, 400: MessageSchema, 500: MessageSchema})
def create_user(request, user_e_type: TypeUserSchema):
    try:
        user = User(**user_e_type.user.dict())
        user.password = make_password(user_e_type.user.password)
        user.full_clean()  # usar para reconhecer os validators
        user.save()
        assign_role(user, user_e_type.type_user.type)
        return 201, user
    except ValidationError as e:
        return 400, MessageSchema(message='Erro de Validação', errors=e.message_dict)
    except Exception as e:
        return 500, {'errors': 'Erro ao criar usuário.'}
    