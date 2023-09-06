from datetime import datetime
from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

import django
from django.db import models
from django.db import connection


class Emergencia(models.Model):
    # id = models.CharField(primary_key=True, max_length=50, default='')
    nombre = models.CharField(max_length=50, default='')
    asunto = models.CharField(max_length=200, default='')
    ubicacion = models.CharField(max_length=300, default='')
    hora_entrada = models.CharField(max_length=20, default='')
    num_voluntarios_necesarios = models.IntegerField(default=0)
    #habilidad_requerida = models.TextField(choices=HabilidadMedica.choices, default='')
    # activada = models.BooleanField(default=False)
    # debería ser un arreglo de voluntarios
    es_atendida = models.BooleanField(default=False)
    es_enviada = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)
    # vacantes = models.IntegerField(default=0)
    # habilidad_requerida = models.TextField(choices=HabilidadMedica.choices)
    # lista_priorizada = []
    # lista = []

    def verificar_emergencia(self):
        # Comprobar que todos tengan True
        if self.verificar_voluntarios() and self.verificar_actividades():
            # Se cambia el valor de la bandera
            self.es_atendida = True
            self.save()

    def verificar_actividades(self):
        # Recorrer actividades y verificar su valor en tiene_voluntario
        respuesta = False
        actividades = self.actividades.all()
        for actividad in actividades:
            if actividad.get_tiene_voluntario():
                respuesta = True
            else:
                respuesta = False
        return respuesta

    def verificar_voluntarios(self):
        # Recorrer voluntarios y verificar su valor en es_asignado
        respuesta = False
        voluntarios = self.voluntarios.all()
        for voluntario in voluntarios:
            if voluntario.get_es_asignado():
                respuesta = True
            else:
                respuesta = False
        return respuesta

    def add_voluntarios(self, voluntario):
        self.voluntarios.add(voluntario)

    def add_actividades(self, actividad):
        self.actividades.add(actividad)

    def get_es_atendida(self):
        return self.es_atendida

    def get_id(self):
        return self.id

    def get_voluntarios(self):
        return self.voluntarios.all()

    def get_actividades(self):
        return self.actividades.all()

    def notificar(self):
        texto = F'{self.asunto} \nEstimado {self.dirigido_a} el doctor {self.encargado} solicita su presencia en ' \
                F'{self.ubicacion} a las {self.hora_entrada} para atender un(a) {self.tipo_emergencia} ' \
                F'\nLas actividades a realizar son: \n {self.actividades} ' \
                F'\nConsideraciones a tener en cuenta: \n {self.detalle}'
        return texto

    def imprimir(nombre):
        print("imprimir: ", nombre)
        return 0

    @staticmethod
    def obtener_emergencia_por_id(id_emergencia):
        try:
            emergencia = Emergencia.objects.get(id=id_emergencia)
            return emergencia
        except Emergencia.DoesNotExist:
            return None

    @staticmethod
    def obtener_emergencia_activada():
        emergencias = Emergencia.objects.all()
        for emergencia in emergencias:
            if emergencia.activada == True:
                return emergencia

    def priorizar_voluntarios(self):
        lista_ordenada = [voluntario.horas_experiencia_habilidad(self.habilidad_requerida) for voluntario in self.lista]
        voluntarios_con_habilidad = list(filter(lambda x: x.titulo == self.habilidad_requerida, lista_ordenada))
        voluntarios_sin_habilidad = list(filter(lambda x: x.titulo != self.habilidad_requerida, lista_ordenada))
        self.lista_priorizada = (self.ordenar_voluntarios(voluntarios_con_habilidad) + self.ordenar_voluntarios(
            voluntarios_sin_habilidad))[:self.vacantes]
        return self.lista_priorizada

    def ordenar_voluntarios(self, lista_filter):
        return sorted(lista_filter, key=lambda x: x.horas_experiencia, reverse=True)

    def obtener_lista_nombres(self):
        lista_priorizada = [habilidad.voluntario for habilidad in self.lista_priorizada]
        return [voluntario.nombre + " " + voluntario.apellido for voluntario in lista_priorizada]

    def obtener_lista_voluntarios(self):
        return [habilidad.voluntario for habilidad in self.lista_priorizada]
