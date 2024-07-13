from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

def validate_nascimento(value):
    # Verifica se a data não está no futuro
    if value > date.today():
        raise ValidationError(
            _('A data de nascimento não pode estar no futuro.'),
            params={'value': value},
        )