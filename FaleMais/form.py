from django.forms import ModelForm
from .models import Ligacao


class LigacaoForm(ModelForm):
    class Meta:
        model = Ligacao
        fields = ['DDD_origem', 'DDD_destino', 'tempo', 'plano_falemais']
