from ninja import Router
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

from .schemas import UserSchema, TypeUserSchema
from .models import User


users_router = Router()

@users_router.post('/', response={200: dict, 400: dict, 500: dict})
def create_user(request, user_e_type: TypeUserSchema):
    try:
        user = User(**user_e_type.user.dict())
        user.password = make_password(user_e_type.user.password)
        user.full_clean()  # usar para reconhecer os validators
        user.save()
        assign_role(user, user_e_type.type_user.type)
    except ValidationError as e:
        return 400, {'errors': e.message_dict}
    except Exception as e:
        return 500, {'errors': 'Erro interno do servidor, solicite um administrador.'}

    return {'Id do Usuário': user.id}