import random

from django.http import HttpResponse
from pyexpat.errors import messages

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from django.shortcuts import render
from gestion_voluntarios.controller.emergencia_controller import solicitar_servicios_voluntarios


def index(request):
    print("Dentro del index")
    context = {}
    # context.update(get_emergencia(request))
    return render(request, 'notificacion.html', context)


def obtener_voluntarios_confirmados(lista_voluntarios, num_voluntarios_requeridos):
    lista_confirmados = []
    for i in range(num_voluntarios_requeridos):
        lista_confirmados.append(lista_voluntarios[i])

    return lista_confirmados


def contar_elementos(lista):
    contador = 0
    for x in lista:
        contador += 1

    return contador


def letra_random():
    letras = ['D', 'O']
    return random.choice(letras)


def obtener_nombres(lista):
    aux_lista = ""
    if len(lista) == 0:
        aux_lista = "null"
        return aux_lista
    tamanio = len(lista)
    for voluntario in lista:
        if lista.index(voluntario) < tamanio - 1:
            aux_lista += voluntario.to_string() + ", "
        else:
            aux_lista += voluntario.to_string()
    return aux_lista


def index(request):
    print("Dentro del index")
    context = {}
    context.update(get_contexto(request))
    return render(request, 'notificacion.html', context)


def get_contexto(request):
    voluntarios = Voluntario.objects.all()
    emergencia = Emergencia.objects.all()
    contexto = {
        'voluntarios': voluntarios,
        'emergencia': emergencia}
    return render(request, 'notificacion.html', contexto)


def notificar(emergencia, lista_voluntarios):
    for voluntario in lista_voluntarios:
        texto = F'{emergencia.nombre} \n{emergencia.asunto} \nEstimado {voluntario.nombre}, se solicita su presencia en ' \
                F'{emergencia.ubicacion} a las {emergencia.hora_entrada}\n'
        print(texto)


def ver_notificacion(request):
    print("id_voluntario", request.POST.get('id_voluntario'))
    context = {}
    if request.method == "POST":
        if "ver_notificaciones" == request.POST.get('operacion'):
            id_voluntario = request.POST.get('id_voluntario')
            voluntario = Voluntario.obtener_voluntario_por_id(id_voluntario)
            emergencias = voluntario.get_emergencias()
            context = {'emergencias': emergencias, 'voluntario': voluntario}

    return render(request, 'notificacion.html', context)

