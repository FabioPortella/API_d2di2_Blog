from typing import List, Optional
from ninja import Router

from users.models import User

from .models import Noticia
from .schemas import NoticiaSchema, NoticiaInserirSchema, MessageSchema


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
def obter_noticia(request, id: int):
    try:
        noticia = Noticia.objects.get(id=id)
        return 200, noticia
    except Noticia.DoesNotExist:
        return 404, {"message": "Notícia não encontrada"}
    except Exception as e:
        return 500, {"message": "Erro ao obter notícia"}
    

@noticias_router.post('/', response={201: NoticiaSchema, 400: MessageSchema, 404: MessageSchema})
def inserir_noticia(request, noticia: NoticiaInserirSchema):
    # verificando se usuário tem permissão para inserir
    user = request.user
    if not user.groups.filter(name='autor').exists():
        return 400, {"message": "Usuário não tem permissão para inserir notícias"}
    
    try:
        usuario = User.objects.get(id=noticia.autor)
    except User.DoesNotExist:
        return 404, {"message": "Usuário não existe"}
    
    noticia = Noticia.objects.create(
        titulo = noticia.titulo,
        sub_titulo = noticia.sub_titulo,
        texto = noticia.texto,
        autor = usuario,
        publicado = noticia.publicado,
    )
    return 201, noticia


#TODO: Criar alterar noticia


@noticias_router.delete('/{id}', response={200: MessageSchema, 400: MessageSchema, 404: MessageSchema, 500: MessageSchema})
def excluir_noticia(request, id: int):
    # verificando se usuário tem permissão para deletar
    usuario = request.user
    if not usuario.groups.filter(name='autor').exists():
        return 400, {"message": "Usuário não tem permissão excluir notícia"}
    
    try:        
        noticia = Noticia.objects.get(id=id)
        noticia.delete()
        return 200, {"message": "Notícia excluida com sucesso"}
    except Noticia.DoesNotExist:
        return 404, {"message": "Notícia não encontrada"}
    except Exception as e:
        return 500, {"message": "Erro ao obter notícia"}
