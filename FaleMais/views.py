from django.shortcuts import render, redirect
from .form import LigacaoForm
from .models import Tarifa


# plataforma de inicio.
def home(request):
    return render(request, 'FaleMais/home.html')


def consultar_ligacao(request):
    data = {}

    # instancia de formulario
    form = LigacaoForm(request.POST or None)

    # confere se o formulario esta completamente preenchido
    if form.is_valid():
        # coletade dados do formulario
        info_dict = form.cleaned_data
        # fintragem de Tarifas para conferir se a ligacao e valida ou n.
        tarifa_list = Tarifa.objects.filter(DDD_origem=info_dict['DDD_origem'], DDD_destino=info_dict['DDD_destino'])
        if len(tarifa_list) > 0:
            tarifa = tarifa_list[0]

            # confere se o tempo de chamada e maior que o tempo minimo para cobranca do plano
            if info_dict['tempo'] > int(info_dict['plano_falemais']):
                preco = (info_dict['tempo'] - int(info_dict['plano_falemais'])) * tarifa.preco_por_minuto * 1.1

            else:
                preco = 0

            # adiciona o preco como argumento
            info_dict['preco'] = '%.2f' % preco
            return render(request, 'Falemais/preco.html', info_dict)

        else:
            return redirect('url_consultar_ligacao_error')

    data['form'] = form
    return render(request, 'FaleMais/ligacao_form.html', data)


# view de erro de consulta
def consultar_ligacao_error(request):
    return render(request, 'FaleMais/cl_error.html')
