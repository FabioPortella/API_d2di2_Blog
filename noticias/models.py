from django.utils import timezone
from users.models import User
import uuid
from django.db import models

class Noticia(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True, null=True, blank=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):
        # Atualiza o campo 'data_publicacao' com a data e horário atual sempre que o objeto é salvo
        self.data_modificacao = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-data_modificacao']