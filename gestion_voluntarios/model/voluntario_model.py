import django
from django.db import models

from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.emergencia_model import Emergencia
from django.core.exceptions import ValidationError

django.setup()


class Voluntario(models.Model):
    # Campos de la clase Voluntario
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)
    estado = models.CharField(max_length=1, default="D")
    es_asignado = models.BooleanField(default=False)
    tiene_emergencia = models.BooleanField(default=False)
    """emergencia = models.ForeignKey(Emergencia,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True,
                                   related_name='voluntarios'
                                   )"""
    emergencias = models.ManyToManyField('Emergencia')

    def asignar_emergencia(self, emergencia):
        self.emergencias.add(emergencia)
        emergencia.es_enviada = True
        emergencia.save()
        self.save()

    def get_tiene_emergencia(self):
        return self.tiene_emergencia

    def get_emergencias(self):
        return self.emergencias.all()

    def agregar_emergencia(self, emergencia):
        self.tiene_emergencia = True
        self.emergencias.add(emergencia)

    def get_es_asignado(self):
        return self.es_asignado

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

    def to_string(self):
        return self.nombre + " " + self.apellido

    def confirmar_asistencia(self):
        self.estado = 'O'

    @staticmethod
    def get_voluntarios():
        return Voluntario.objects.all()

    @staticmethod
    def editar_voluntario(voluntario):
        try:
            Voluntario.objects.filter(id=voluntario.id).update(
                nombre=voluntario.nombre,
                apellido=voluntario.apellido,
                edad=voluntario.edad,
                estado=voluntario.estado,
                es_asignado=voluntario.es_asignado,
                emergencia_id=voluntario.emergencia_id
            )
            return True

        except ValidationError:
            return False

    def horas_experiencia_habilidad(self, habilidad_requerida):
        from gestion_voluntarios.model.habilidad_model import Habilidad
        habilidad = Habilidad.objects.filter(voluntario=self)
        habilidades_habilidad_requerida = [h for h in habilidad if h.titulo == habilidad_requerida]
        if not habilidades_habilidad_requerida:
            return max(habilidad, key=lambda x: x.horas_experiencia, default=None)
        return max(habilidades_habilidad_requerida, key=lambda x: x.horas_experiencia)
