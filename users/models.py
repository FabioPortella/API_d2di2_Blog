from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_nascimento


class User(AbstractUser):

    email = models.EmailField( unique=True)
    data_nascimento = models.DateField(null=True, blank=True, validators=[validate_nascimento])
    tipo = models.CharField(max_length=10, choices=[("leitor", "Leitor"), ("autor","Autor")], default="leitor")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email