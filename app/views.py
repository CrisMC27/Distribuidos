from django.shortcuts import render
from .models import Envio

def inicio(request):
    return render(request, 'inicio.html')

def ver_envios(request):
    pais_seleccionado = request.GET.get('pais')
    if pais_seleccionado:
        envios = Envio.objects.filter(pais=pais_seleccionado)
    else:
        envios = Envio.objects.all()

    # Obtener lista de países únicos
    paises = Envio.objects.values_list('pais', flat=True).distinct()

    return render(request, 'envios.html', {
        'envios': envios,
        'paises': paises,
        'pais_seleccionado': pais_seleccionado,
    })