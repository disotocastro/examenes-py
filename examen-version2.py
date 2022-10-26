# Parte 1 Evaluación
def Menu():
    # costoLitro = int(input("Ingrese el costo gasolina: "))
    # numeroRutas = int(input("Ingrese la cantidad de rutas de buses: "))
    costoLitro = 800
    global numeroRutas
    numeroRutas = 2

    menuBus(costoLitro)


# Parte 2 Evaluación
def menuBus(costoLitro):
    # distancia = int(input("Ingrese la distancia: "))
    # cantidadCarreras = int(input("Ingrese el numero de carreras: "))
    distancia = 10
    cantidadCarreras = 3

    pasajerosTotales = 0
    pasajerosSinEspacio = 0

    i = 1

    costoTotalCarreras = 0
    cola = 0

    pasajeros = 0
    pasajerosAbordadosCorrectamente = 0

    tipoBus = 1

    while i < cantidadCarreras+1:

        pasajeros += int(input("Ingrese el numero de pasajeros: "))

        while tipoBus < 3:
            pasajerosTotales += pasajeros-cola

            pasajerosEnBus = PasajerosAbordados(tipoBus, pasajeros)
            costoTotalCarreras += CostoCarrera(tipoBus,
                                               pasajerosEnBus, distancia, costoLitro)
            pasajerosAbordadosCorrectamente += pasajerosEnBus
            pasajerosSinEspacio = SinEspacio(pasajeros, pasajerosEnBus)

            if pasajerosSinEspacio > 0:
                cola += pasajerosSinEspacio
                pasajeros = cola
            else:
                pasajeros = 0

            tarifa = Tarifa(costoTotalCarreras,
                            pasajerosAbordadosCorrectamente)
            promedio = Promedio(pasajerosTotales,
                                (cantidadCarreras))
            ActualizarValores(
                tipoBus, costoTotalCarreras, tarifa, promedio)
        i += 1
    Imprimir(1)
    Imprimir(2)
    Imprimir(3)


def ActualizarValores(tipoBus, costoTotalCarreras, tarifa, promedio):
    global promedio_1, promedio_2, promedio_3
    global costoTotal_1, costoTotal_2, costoTotal_3
    global tarifa_1, tarifa_2, tarifa_3

    promedio_1 = 0
    promedio_2 = 0
    promedio_3 = 0

    costoTotal_1 = 0
    costoTotal_2 = 0
    costoTotal_3 = 0

    tarifa_1 = 0
    tarifa_2 = 0
    tarifa_3 = 0

    if tipoBus == 1:
        promedio_1 = promedio
        costoTotal_1 = costoTotalCarreras
        tarifa_1 = tarifa
    if tipoBus == 2:
        promedio_2 = promedio
        costoTotal_2 = costoTotalCarreras
        tarifa_2 = tarifa
    if tipoBus == 3:
        promedio_3 = promedio
        costoTotal_3 = costoTotalCarreras
        tarifa_3 = tarifa


def Imprimir(tipoBus):
    nombreBus = ''
    if tipoBus == 1:
        nombreBus = "Microbus"
        print(
            f"{nombreBus}: Pasajeros sin viajar: {0} - Promedio: {round(promedio_1)} - Costo Total: {round(costoTotal_1)} - Tarifa: {round(tarifa_1)}")
    if tipoBus == 2:
        nombreBus = "Autobus"
        print(
            f"{nombreBus}: Pasajeros sin viajar: {0} - Promedio: {round(promedio_2)} - Costo Total: {round(costoTotal_2)} - Tarifa: {round(tarifa_2)}")
    if tipoBus == 3:
        nombreBus = "Dos pisos"
        print(
            f"{nombreBus}: Pasajeros sin viajar: {0} - Promedio: {round(promedio_3)} - Costo Total: {round(costoTotal_3)} - Tarifa: {round(tarifa_3)}")


def SinEspacio(pasajerosTotales, pasajerosEnBus):
    return pasajerosTotales - pasajerosEnBus


def Promedio(pasajerosTotales, cantidadCarreras):
    return (pasajerosTotales/cantidadCarreras)


def CostoCarrera(tipoBus, pasajeros, distancia, costoLitro):
    costoCarrera = 0

    rendimientoVacio = RendimientoVacio(tipoBus)
    degradacion = Degradacion(tipoBus)

    costoCarrera = rendimientoVacio - (pasajeros * degradacion)

    consumo = distancia/costoCarrera
    costoCarrera = consumo * costoLitro

    return costoCarrera


def Tarifa(costoTotal, pasajerosEnBus):
    total = (costoTotal*10) / pasajerosEnBus
    return total


# Parte 3 Evaluación
def PasajerosAbordados(tipoBus, pasajeros):
    capacidad = 0
    if (tipoBus == 1):
        capacidad = 25
    if (tipoBus == 2):
        capacidad = 60
    if (tipoBus == 3):
        capacidad = 110

    if pasajeros == 0:
        return 0
    if capacidad <= pasajeros:
        return capacidad
    if capacidad >= pasajeros:
        return pasajeros


# Punto 4 evaluacion
def CupoPasajeros(tipoBus):
    capacidad = 0
    if (tipoBus == 1):
        capacidad = 25
    if (tipoBus == 2):
        capacidad = 60
    if (tipoBus == 3):
        capacidad = 110

    return capacidad


def RendimientoVacio(tipoBus):
    rendimientoVacio = 0
    if (tipoBus == 1):
        rendimientoVacio = 11
    if (tipoBus == 2):
        rendimientoVacio = 6.8
    if (tipoBus == 3):
        rendimientoVacio = 4.5

    return rendimientoVacio


def Degradacion(tipoBus):
    degradacion = 0
    if (tipoBus == 1):
        degradacion = 0.1
    if (tipoBus == 2):
        degradacion = 0.05
    if (tipoBus == 3):
        degradacion = 0.02

    return degradacion


def PasajerosSinEspacio(pasajerosTotales, abordadosCorrectamente):
    pasajerosSinEspacio = pasajerosTotales-abordadosCorrectamente

    if pasajerosSinEspacio < 0:
        pasajerosSinEspacio = pasajerosSinEspacio * -1

    return pasajerosSinEspacio


Menu()
