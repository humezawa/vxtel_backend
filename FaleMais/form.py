from django import forms
from django.forms import ModelForm
from .models import Ligacao


# formulario de dados de ligacao
class LigacaoForm(forms.Form):
    # escolhas diponiveis para os planos
    FALEMAIS_PLANS = [
        (30, 'FaleMais 30'),
        (60, 'FaleMais 60'),
        (120, 'FaleMais 120')
    ]

    # escolhas disponiveis para os DDDs
    DDD = [
        ('011', '011'),
        ('016', '016'),
        ('017', '017'),
        ('018', '018')
    ]

    DDD_origem = forms.ChoiceField(label='DDD_origem', choices=DDD, widget=forms.Select)
    DDD_destino = forms.ChoiceField(label='DDD_destino', choices=DDD, widget=forms.Select)
    tempo = forms.FloatField(label='Tempo em Minutos')
    plano_falemais = forms.ChoiceField(label='Plano FaleMais', choices=FALEMAIS_PLANS, widget=forms.Select)

class LigacaoForm2(ModelForm):
    class Meta:
        model = Ligacao
        fields = ['DDD_origem', 'DDD_destino', 'tempo', 'plano_falemais']