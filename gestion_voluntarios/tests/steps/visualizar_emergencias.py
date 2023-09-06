import django
import os
import datetime
import random

from behave import *
from faker import Faker

from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.actividad_model import Actividad
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

use_step_matcher("parse")


@step("que soy un voluntario que aún no ha atendido una emergencia")
def step_impl(context):
    nombre_emergencia = faker.name()
    asunto = faker.sentence()
    ubicacion = faker.city()
    hora_entrada = datetime.time(hour=random.randint(7, 9), minute=random.randint(0, 59))    # esta hora debe empatar con el horario de los voluntarios
    num_voluntarios = 1
    es_atendida = True
    es_enviada = False

    context.mi_emergencia = Emergencia(nombre=nombre_emergencia,
                                       asunto=asunto,
                                       ubicacion=ubicacion,
                                       hora_entrada=hora_entrada,
                                       num_voluntarios_necesarios=num_voluntarios,
                                       es_atendida=es_atendida,
                                       es_enviada=es_enviada)
    context.mi_emergencia.save()

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

    #context.mi_voluntario.agregar_emergencia(context.mi_emergencia)


@step("deseo observar cuántas emergencias se me han enviado")
def step_impl(context):
    # context.mi_voluntario.id = 4
    context.emergencias_enviadas = context.mi_voluntario.get_emergencias()
    for em in context.emergencias_enviadas:
        print(em.nombre)
    # raise NotImplementedError(u'STEP: Cuando deseo observar cuántas emergencias se me han enviado')


@step('el número de emergencias que visualizo es "{numero_emergencias_recibidas}"')
def step_impl(context, numero_emergencias_recibidas):
    context.num_emergencias = 0
    for i in range(len(context.emergencias_enviadas) - 1):
            context.num_emergencias += 1
    print(context.num_emergencias)
    print(numero_emergencias_recibidas)
    assert context.num_emergencias == int(numero_emergencias_recibidas)
    # raise NotImplementedError(u'STEP: Entonces el número de emergencias que visualizo es
    # "<numero_emergencias_recibidas>"')