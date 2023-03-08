from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario
from django.shortcuts import redirect

def index(request):
    print("Dentro del index")
    context = {}
    #context.update(get_emergencia(request))
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
            habilidad_requerida=habilidad_requerida
        )
        Emergencia.imprimir(request.POST.get('name'))
        emergencia.save()
        print("Emergencia guardada con exito")

        context = {'emergencia': emergencia}
    return render(request, 'emergencia_view.html', context)
    #return redirect(f'/gestion_voluntarios/emergencia?id_emergencia={emergencia.id}')


    # Solicitar voluntarios

def cargar_emergencia(request):
    print("Dentro de crear emergencia")
    emergencia = Emergencia()
    voluntarios_seleccionados = []
    # Obtener Parametros
    if request.method == 'POST':
        if "solicitar" == request.POST.get('operacion'):
            id_emergencia = request.POST.get('id_emergencia')
            print('id: ',id_emergencia)
            emergencia = Emergencia.obtener_emergencia_por_id(id_emergencia)
            voluntariosRegistrados = Voluntario.get_voluntarios()
            voluntarios_seleccionados = solicitar_servicios_voluntarios(voluntariosRegistrados,
                                                                        emergencia.habilidad_requerida)
            # si los voluntarios que cumplen con la habilidad requerido son mayores al número de voluntarios requeridos
            if len(voluntarios_seleccionados) >= emergencia.num_voluntarios_necesarios:
                enviar_notificaciones(voluntarios_seleccionados)
            else:
                enviar_notificaciones_exitosas(voluntarios_seleccionados)

    return redirect(request, 'voluntario_notificacion_controller.py', emergencia, voluntarios_seleccionados)



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
                #Voluntario.objects.get(id=emergencia.id)
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


def verificar_habilidades_requeridas(voluntario, habilidades_requeridas):
    # Ampliar más la logica para ver que sucede con las habilidades
    # Obtener la lista de habilidades requeridas y comparar con las habilidades del voluntario
    habilidad_requerida_usuario = []
    # Estas listas son con fines de prueba con base a lo que llegue en el feature
    habilidades_voluntarios = [Habilidad("Saturacion"), Habilidad("RCP"), Habilidad("Respiracion")]
    habilidades_requeridas = [Habilidad("Saturacion"), Habilidad("RCP")]

    # Voluntario seleccionados de prueba
    carlos = Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    juan = Voluntario("Juan", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    andres = Voluntario("Andres", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    # LINEA IMPORTANTE
    # habilidades_voluntarios = voluntario.habilidades

    # Caso cuando las habilidades son exactamente las mismas
    if habilidades_requeridas == habilidades_voluntarios:

        return "si"
    else:
        # Caso cuando las habilidades de los voluntarios son mayores
        # Se compara la lista de habilidades requeridas con base en la lista de habilidades voluntario
        for habilidad_requerida in habilidades_requeridas:
            for habilidad_voluntario in habilidades_voluntarios:
                if habilidad_requerida.descripcion_habilidad == habilidad_voluntario.descripcion_habilidad:
                    habilidad_requerida_usuario.append(habilidad_requerida)
                    return "si"
                else:
                    return "no"


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
    print('Lo siento no existen voluntarios suficientes. Numero de notificaciones exitosas enviadas fueron: ', aux)
    return aux
