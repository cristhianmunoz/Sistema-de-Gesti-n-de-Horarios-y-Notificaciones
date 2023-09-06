# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de un voluntario a una emergencia médica
Como voluntario,
quiero confirmar mi asistencia a una emergencia médica
para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
Dado que soy un voluntario y se me han notificado '<num_emergencias>' emergencias
Cuando confirmo mi asistencia a una emergencia
Entonces mi estado cambia a '<estado>'

Ejemplos: Confirmar Asistencia Parcial
  |num_emergencias|estado|
  |       10      |   O  |
