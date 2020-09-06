from django.shortcuts import render
from .form import LigacaoForm


def consultar_ligacao(request):
    data = {}
    form = LigacaoForm(request.POST or None)
    if form.is_valid():
        print(form.tempo)

    data['form'] = form
    return render(request, 'FaleMais/ligacao_form.html', data)

