# Created by Cris at 3/11/2023
# language: es
  Característica: Visualización de emergencias
    Como voluntario,
    quiero observar todas las emergencias que me han enviado,
    para atender cualquiera de ellas.

    Esquema del escenario: Visualizar emergencias
      Dado que soy un voluntario que aún no ha atendido una emergencia
      Cuando deseo observar cuántas emergencias se me han enviado
      Entonces el número de emergencias que visualizo es "<numero_emergencias_recibidas>"

      Ejemplos: Asignaciones
      | numero_emergencias_recibidas |
      |             9                |