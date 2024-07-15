from ninja import ModelSchema, Schema
from .models import Noticia


class NoticiaSchema(ModelSchema):
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

class MessageSchema(Schema):
    message: str
