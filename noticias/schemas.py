from ninja import ModelSchema, Schema

from users.schemas import UserSchema
from .models import Noticia


class NoticiaSchema(ModelSchema):
    autor: UserSchema
    class Meta:
        model = Noticia
        fields = [
            "id", 
            "titulo", 
            "sub_titulo", 
            "texto",
            "autor", 
            "data_publicacao", 
            "data_modificacao",
            "publicado"
        ]


class NoticiaInserirSchema(ModelSchema):    
    class Meta:
        model = Noticia
        fields = [
            "titulo", 
            "sub_titulo", 
            "texto",
            "autor", 
            "publicado"
        ]


class MessageSchema(Schema):
    message: str
