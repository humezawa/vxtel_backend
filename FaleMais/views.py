from django.shortcuts import render, redirect
from .form import LigacaoForm
from .models import Tarifa


def home(request):
    return render(request, 'FaleMais/home.html')


def consultar_ligacao(request):
    data = {}
    form = LigacaoForm(request.POST or None)
    if form.is_valid():
        info_dict = form.cleaned_data
        tarifa_list = Tarifa.objects.filter(DDD_origem=info_dict['DDD_origem'], DDD_destino=info_dict['DDD_destino'])
        if len(tarifa_list) > 0:
            tarifa = tarifa_list[0]
            if info_dict['tempo'] > int(info_dict['plano_falemais']):
                preco = (info_dict['tempo'] - int(info_dict['plano_falemais'])) * tarifa.preco_por_minuto

            else:
                preco = 0

            info_dict['preco'] = '%.2f' % preco
            return render(request, 'Falemais/preco.html', info_dict)

        else:
            return redirect('url_consultar_ligacao_error')

    data['form'] = form
    return render(request, 'FaleMais/ligacao_form.html', data)


def consultar_ligacao_error(request):
    return render(request, 'FaleMais/cl_error.html')
