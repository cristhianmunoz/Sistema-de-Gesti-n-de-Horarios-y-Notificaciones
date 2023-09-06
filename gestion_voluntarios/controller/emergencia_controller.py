from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario
from django.shortcuts import redirect


def index(request):
    print("Dentro del index")
    context = {}
    # context.update(get_emergencia(request))
    return render(request, 'emergencia_view.html', context)


def registrar_emergencia(request):
    print("Dentro de crear emergencia")
    id_emergencia = ''
    # Obtener Parametros
    if request.method == 'POST':
        if "creacion" == request.POST.get('operacion'):
            titulo = request.POST.get('name')
            habilidad_requerida = request.POST.get('select')
            nume_voluntarios_requeridos = request.POST.get('num_voluntarios')
            descripcion = request.POST.get('descripcion')

        # Comunicarse con el modelo
        emergencia = Emergencia(
            num_voluntarios_necesarios=nume_voluntarios_requeridos,
            nombre=titulo,
            asunto=descripcion,
            activada=True,
            habilidad_requerida=habilidad_requerida
        )
        Emergencia.imprimir(request.POST.get('name'))
        emergencia.save()
        print("Emergencia guardada con exito")

        context = {'emergencia': emergencia}
    return render(request, 'emergencia_view.html', context)

    # Solicitar voluntarios


def cargar_emergencia(request):
    print("Dentro de crear emergencia")
    # Obtener Parametros
    if request.method == 'POST':
        if "solicitar" == request.POST.get('operacion'):
            id_emergencia = request.POST.get('id_emergencia')
            print('id: ', id_emergencia)
            emergencia = Emergencia.obtener_emergencia_por_id(id_emergencia)
            voluntariosRegistrados = Voluntario.get_voluntarios()
            voluntarios_seleccionados = solicitar_servicios_voluntarios(voluntariosRegistrados,
                                                                        emergencia)
            # si los voluntarios que cumplen con la habilidad requerido son mayores al número de voluntarios requeridos
            if len(voluntarios_seleccionados) >= emergencia.num_voluntarios_necesarios:
                num_voluntarios_seleccionado = enviar_notificaciones(voluntarios_seleccionados)
            else:
                num_voluntarios_seleccionado = enviar_notificaciones_exitosas(voluntarios_seleccionados)

            context = {"num_voluntarios_seleccionados": num_voluntarios_seleccionado,
                       "mensaje": "Solicitud existosa: el número de notificaciones enviadas es de ",
                       "emergencia": emergencia}
    return render(request, 'emergencia_view.html', context)


def obtener_nombres_voluntario(voluntarios_seleccionados):
    nombres_voluntarios_prueba = []
    for voluntario in voluntarios_seleccionados:
        nombres_voluntarios_prueba.append(voluntario.nombre)
    return nombres_voluntarios_prueba


def solicitar_servicios_voluntarios(voluntarios, emergencia):
    voluntario_seleccionado = []
    for voluntario in voluntarios:
        habilidades_voluntario = Habilidad.obtener_habilidades_por_id_voluntario(voluntario.id)
        for habilidad_voluntario in habilidades_voluntario:
            if emergencia.habilidad_requerida in habilidad_voluntario.titulo:
                voluntario = Voluntario.obtener_voluntario_por_id(voluntario.id)
                voluntario.emergencia_id = emergencia.id
                voluntario.editar_voluntario(voluntario)
                voluntario_seleccionado.append(voluntario)
                break
    return voluntario_seleccionado


def voluntarios_seleccionados(voluntarios_ordenados, numero_voluntarios_requeridos):
    voluntarios_seleccionados = []
    for i in range(numero_voluntarios_requeridos):
        voluntarios_seleccionados.append(voluntarios_ordenados)

    return voluntarios_seleccionados


def enviar_notificaciones(voluntarios_seleccionados):
    aux = 0
    for voluntario in voluntarios_seleccionados:
        aux += 1
    print('Numero de notificaciones exitosas enviadas fueron: ', aux)

    return aux


def seleccionar_voluntarios(habilidad_requerida):
    voluntarios_seleccionados = []
    for voluntario in Voluntario.get_voluntarios():
        for habilidad_voluntario in Habilidad.obtener_habilidades_por_id_voluntario(voluntario.id):
            if habilidad_voluntario.titulo == habilidad_requerida:
                voluntarios_seleccionados.append(voluntario)
                break
    return voluntarios_seleccionados


def verificar_numero_voluntarios_requeridos(tamanio_seleccionados, numero_requeridos):
    if tamanio_seleccionados == numero_requeridos:
        return tamanio_seleccionados
    elif tamanio_seleccionados <= numero_requeridos:
        return tamanio_seleccionados


def obtener_voluntarios_finales(voluntarios_seleccionados, voluntarios_requeridos):
    voluntarios_finales = []
    numero_voluntarios_seleccionados = verificar_numero_voluntarios_requeridos(len(voluntarios_seleccionados),
                                                                               int(voluntarios_requeridos))
    for voluntario in range(numero_voluntarios_seleccionados):
        voluntarios_finales.append(voluntarios_seleccionados[voluntario])
    return voluntarios_finales


def enviar_notificaciones_exitosas(voluntarios_seleccionados):
    aux = 0
    for voluntario in voluntarios_seleccionados:
        aux += 1
    print('No hay sufiecientes voluntarios. Numero de notificaciones exitosas enviadas fueron: ', aux)
    return aux
