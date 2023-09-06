from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from gestion_voluntarios.model.dia_semana_model import DiaSemana
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.horario_model import Horario


def index(request):
    # Obteniendo los parámetros enviados por GET
    id_voluntario = request.GET.get('id_voluntario')

    # Comunicándose con los modelos para obtener los datos
    contexto = obtener_contexto(id_voluntario)

    # Enviando los datos obtenidos a la vista
    return render(request=request, template_name='voluntario_home_view.html', context=contexto)


def comprobar_operacion_creacion(request):
    operacion = request.POST.get('operacion')
    return operacion and operacion == 'creacion'


def comprobar_operacion_eliminacion(request):
    operacion = request.POST.get('operacion')
    return operacion and operacion == 'eliminacion'


def comprobar_operacion_edicion(request):
    operacion = request.POST.get('operacion')
    return operacion and operacion == 'edicion'


def obtener_contexto(id_voluntario):
    voluntario = Voluntario.obtener_voluntario_por_id(id_voluntario)
    habilidades = Habilidad.obtener_habilidades_por_id_voluntario(id_voluntario)
    periodos = Periodo.obtener_periodos_por_id_voluntario(id_voluntario)
    horario = Horario.obtener_horario_por_id_voluntario(id_voluntario)
    catalogo_habilidades = HabilidadMedica.labels
    dias_semana = DiaSemana.labels

    return {
        'voluntario': voluntario,
        'habilidades': habilidades,
        'periodos': periodos,
        'catalogo_habilidades': catalogo_habilidades,
        'dias_semana': dias_semana,
        'id_horario': horario.id
    }


def cambiar_estado(request):
    print("id_voluntario2", request.POST.get('id_voluntario'))
    print("opción: ", request.POST.get('confirmacion'))
    contexto = {}
    if request.POST.get('confirmacion') == 'confirmar':
        id_voluntario = request.POST.get('id_voluntario')
        Voluntario.objects.filter(id=id_voluntario).update(estado='O')
        contexto = {'voluntario': Voluntario.obtener_voluntario_por_id(id_voluntario)}

    return render(request, 'confirmacion.html', contexto)

def eliminar_emergencia(request):
    print("RECHAZAR")
    contexto = {}
    if request.POST.get('rechazo') == 'rechazar':
        id_voluntario = request.POST.get('id_voluntario')
        # Elimina la emergencia que rechaza
        id_emergencia = request.POST.get('id_emergencia')
        voluntario = Voluntario.obtener_voluntario_por_id(id_voluntario)
        emergencia_borrar = Emergencia.objects.get(id=id_emergencia)
        emergencia_borrar.delete()
        emergencias = voluntario.get_emergencias()
        contexto = {'emergencias': emergencias,
                    'voluntario': Voluntario.obtener_voluntario_por_id(id_voluntario)}

    return render(request, 'notificacion.html', contexto)