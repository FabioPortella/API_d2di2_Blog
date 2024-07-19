from ninja import Router
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from .schemas import AuthSchema, MessageSchema, UserSchema 
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
    

@users_router.post('/autenticar/', response={200:UserSchema, 400: MessageSchema, 500: MessageSchema})
def autenticar(request, user_aut:AuthSchema): 
 
    try:
        user = authenticate(username=user_aut.email, password=user_aut.password)
        if user:
            return 200, user
        else:
            return 400, MessageSchema(message='Email e/ou senha inválido(s)')
        
    except Exception as e:
        return 500, {'errors': 'Erro na autenticação.'}
