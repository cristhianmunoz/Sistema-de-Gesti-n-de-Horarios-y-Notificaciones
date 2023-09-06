from django.urls import path

from gestion_voluntarios.controller import voluntario_home_controller, voluntario_confirmacion_controller
from gestion_voluntarios.controller import voluntario_habilidad_controller
from gestion_voluntarios.controller import voluntario_horario_controller
from gestion_voluntarios.controller import asignar_voluntarios_controller
from gestion_voluntarios.controller import emergencia_controller
from gestion_voluntarios.controller import voluntario_notificacion_controller


from gestion_voluntarios.controller import voluntario_login_controller
from gestion_voluntarios.controller import priorizar_voluntario_controller

urlpatterns = [
    # path('', voluntario_view.index, name='index'),
    path('voluntario', voluntario_home_controller.index, name='voluntario'),
    path('habilidad', voluntario_habilidad_controller.index, name='habilidad'),
    path('horario', voluntario_horario_controller.index, name='horario'),
    path('actividad', asignar_voluntarios_controller.index, name='actividad'),
    path('asignar', asignar_voluntarios_controller.asignar_voluntarios, name='asignar_voluntarios'),
    path('emergencia', emergencia_controller.index, name='emergencia'),
    path('registrar_emergencia', emergencia_controller.registrar_emergencia, name='registrar_emergencia'),
    path('cargar_emergencia', emergencia_controller.cargar_emergencia, name='cargar_emergencia'),
    #path('enviar_notificacion', voluntario_notificacion_controller.ver_notificacion, name='enviar_notificacion'),
    path('notificacion', voluntario_notificacion_controller.ver_notificacion, name='notificacion'),
    path('confirmar_emergencia', voluntario_home_controller.cambiar_estado, name='confirmar_emergencia'),
    path('notificacion2', voluntario_confirmacion_controller.regresar_notificaciones, name='notificacion2'),
    path('notificacion3', voluntario_home_controller.eliminar_emergencia, name='notificacion3'),

    path('voluntario_login', voluntario_login_controller.index, name='voluntario_login'),
    path('priorizar', priorizar_voluntario_controller.index, name='index'),
]
