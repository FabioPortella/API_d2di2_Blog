from ninja import NinjaAPI
from users.api import users_router
from noticias.api import noticias_router


api = NinjaAPI()
api.add_router('users/', users_router)
api.add_router('noticias/', noticias_router)