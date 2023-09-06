from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from gestion_voluntarios.model.voluntario_model import Voluntario

"""
class NotificacionView(View):
    def get(self, request, pk):
        # Obtener los datos de otra clase
        mi_voluntario = Voluntario.objects.get(pk=pk)
        voluntario = request.get_voluntarios()
        titulo = f"Emergencia médica: {voluntario.nombre}"
        print(voluntario.nombre)
        # Renderizar el template con los datos
        return render(request, '../view/notificacion.html',
                      {'titulo': titulo})

    def post(self, request, pk):
        # Obtener los datos de otra clase
        mi_voluntario = Voluntario.objects.get(pk=pk)

        # Obtener la opción seleccionada por el usuario
        opcion = request.POST.get('opcion')

        # Manejar la opción seleccionada por el usuario
        if opcion == 'confirmar':
            print("Ha confirmado su asistencia")
            # Hacer algo si el usuario confirma la acción
        elif opcion == 'rechazar':
            print("Ha rechazado la emergencia médica")
            # Hacer algo si el usuario rechaza la acción

        # Redirigir al usuario a otra página
        return HttpResponseRedirect('/voluntario_home_view.html')

    def notificar_emergencia(request):
        voluntario = request.get_voluntarios()
        titulo = f"Emergencia médica: {voluntario.nombre}"
        print(voluntario.nombre)
        return render(request, '../view/notificacion.html', {'titulo': titulo})

    def get_voluntarios(self):
        data = models.objects.all()
            return render(request, 'my_template.html', {'data': data})

        return voluntarios"""

