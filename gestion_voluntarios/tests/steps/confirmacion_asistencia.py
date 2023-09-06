import django
import os
import datetime
import random

from behave import *
from faker import Faker

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.controller.voluntario_notificacion_controller import obtener_voluntarios_confirmados, \
    contar_elementos, notificar, letra_random

django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

use_step_matcher("parse")


@step("que soy un voluntario y se me han notificado '{num_emergencias}' emergencias")
def step_impl(context, num_emergencias):
    """
        :type context: behave.runner.Context
    """
    # Creación del voluntario
    nombre_voluntario = 'Guiomar'
    apellido_voluntario = 'Torre'
    edad_voluntario = 21
    # estado = letra_random()
    estado = 'D'
    es_asignado = False
    tiene_emergencia = False
    context.mi_voluntario = Voluntario(id=4,
                                       nombre=nombre_voluntario,
                                       apellido=apellido_voluntario,
                                       edad=edad_voluntario,
                                       estado=estado,
                                       es_asignado=es_asignado,
                                       tiene_emergencia=tiene_emergencia)
    context.mi_voluntario.save()

    context.emergencias_enviadas = context.mi_voluntario.get_emergencias()
    assert len(context.emergencias_enviadas) == int(num_emergencias)
    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("confirmo mi asistencia a una emergencia")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    context.mi_voluntario.confirmar_asistencia()
    # raise NotImplementedError(u'STEP: Y se requiere \'<numero_requerido>\' voluntarios para la emergencia médica')


@step("mi estado cambia a '{estado}'")
def step_impl(context, estado):
    """
    :type context: behave.runner.Context
    """
    context.nuevo_estado = context.mi_voluntario.estado
    assert estado == context.nuevo_estado
    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')
