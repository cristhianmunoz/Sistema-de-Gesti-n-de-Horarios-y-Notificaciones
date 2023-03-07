import django
from django.db import models

from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo

django.setup()


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    def comprobar_disponibilidad(self, periodo_a_comprobar):
        periodos = Periodo.obtener_periodos_por_id_horario(Horario.obtener_horario_por_id_voluntario(self.id).id)
        periodo_a_comprobar_aux = Periodo.obtener_periodo_por_id(periodo_a_comprobar.id)

        # Comprobando la disponibilidad por etapas
        for periodo in periodos:
            if periodo.dia_semana != periodo_a_comprobar_aux.dia_semana:
                continue
            if periodo.hora_inicio > periodo_a_comprobar_aux.hora_inicio:
                continue
            if periodo.hora_fin < periodo_a_comprobar_aux.hora_fin:
                continue
            return True

        return False

    @staticmethod
    def obtener_voluntario_por_id(id_voluntario):
        try:
            voluntario = Voluntario.objects.get(id=id_voluntario)
            return voluntario
        except Voluntario.DoesNotExist:
            return None
