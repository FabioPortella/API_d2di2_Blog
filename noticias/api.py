from typing import List, Optional
import uuid
from ninja import Router

from .models import Noticia
from .schemas import NoticiaSchema, MessageSchema


noticias_router = Router()


@noticias_router.get('/', response={200: List[NoticiaSchema], 404: MessageSchema, 500: MessageSchema})
def listar_noticias(request, titulo: Optional[str] = None):
    try:
        if titulo:
            noticias = Noticia.objects.filter(titulo__icontains=titulo)
            if not noticias:
                return 404, {"message": "Título não cadastrado"}
            return 200, noticias
        return 200, Noticia.objects.all()
    except Exception as e:
        return 500, {"message": "Erro ao listar notícias"}
    

@noticias_router.get('/{id}', response={200: NoticiaSchema, 404: MessageSchema, 500: MessageSchema})
def obter_noticia(request, id: str):
    try:
        noticia = Noticia.objects.get(id=id)
        return 200, noticia
    except Noticia.DoesNotExist:
        return 404, {"message": "Notícia não encontrada"}
    except Exception as e:
        return 500, {"message": "Erro ao obter notícia"}
    

@noticias_router.delete('/{id}', response={200: MessageSchema, 404: MessageSchema, 500: MessageSchema})
def excluir_noticia(request, id: str):
    try:
        noticia = Noticia.objects.get(id=id)
        noticia.delete()
        return 200, {"message": "Notícia excluida com sucesso"}
    except Noticia.DoesNotExist:
        return 404, {"message": "Notícia não encontrada"}
    except Exception as e:
        return 500, {"message": "Erro ao obter notícia"}
