from typing import List
from ninja import Router

from .models import Noticia
from .schemas import NoticiaSchema


noticias_router = Router()

@noticias_router.get('/', response={200: List[NoticiaSchema]})
def listar_noticias(request):
    noticias = Noticia.objects.all()
    return 200, noticias