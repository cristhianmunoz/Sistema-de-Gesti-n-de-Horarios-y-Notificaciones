from django.shortcuts import render

from gestion_voluntarios.model.voluntario_model import Voluntario


def regresar_notificaciones(request):
    context = {}
    if request.method == "POST":
        id_voluntario = request.POST.get('id_voluntario')
        voluntario = Voluntario.obtener_voluntario_por_id(id_voluntario)
        emergencias = voluntario.get_emergencias()
        context = {'emergencias': emergencias, 'voluntario': voluntario}

    return render(request, 'notificacion.html', context)
