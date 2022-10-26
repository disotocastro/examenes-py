# Se pregunta la cantidad de vueltas y duración de cambio de llantas.
total_equipo_ganador = 0
nombre_equipo_ganador = ""

cantidadVueltas = int(input("Cantidad de vueltas: "))
duracionCambioLlantas = int(input("Duración cambio de llantas (s): "))


def menu():
    print("\n1. Equipo")
    print("2. Ganador")
    print("0. Salir\n")

    opcion = input("Ingrese la opción a realizar: ")
    return opcion


def FuncionEquipo():
    continuarEquipo = True
    while (continuarEquipo):
        try:
            nombre_equipo = input("Nombre del equipo: ")
            juegos_llantas = int(input("Cantidad de juegos de llantas: "))

            total_Equipo = (juegos_llantas-1)*duracionCambioLlantas

            i = 1
            while i < juegos_llantas+1:
                tipo_llantas = input(f"Juego {i} tipo de llanta: ")
                cantidad_vueltas = int(
                    input(f"Juego {i} cantidad de vueltas: "))
                total_Equipo += calculoRuedas(tipo_llantas, cantidad_vueltas)
                tipo_llantas = 0
                cantidad_vueltas = 0
                i += 1

            print(
                f"Equipo: {nombre_equipo} ganaría la carrera en: {total_Equipo}")
            global total_equipo_ganador
            global nombre_equipo_ganador

            if (total_equipo_ganador == 0):
                total_equipo_ganador = total_Equipo
                nombre_equipo_ganador = nombre_equipo
                total_Equipo = 0
                nombre_equipo = ""
            elif (total_equipo_ganador != 0):
                if (total_Equipo < total_equipo_ganador):
                    total_equipo_ganador = total_Equipo
                    nombre_equipo_ganador = nombre_equipo

            continuarEquipo = False
        except ValueError:
            print(f"Equipo {nombre_equipo} Descalificado")


def EquipoGanador():
    if total_equipo_ganador > 0:
        print(
            f"El equipo {nombre_equipo_ganador} ganaría la carrera en {total_equipo_ganador}")
    else:
        print("No hay equipos ganadores")


def calculoRuedas(tipo_llantas, cantidad_vueltas):
    vuelta_S = 78.80
    vuelta_M = 80
    vuelta_H = 82

    acumulacion_M = 0
    acumulacion_S = 0
    acumulacion_H = 0

    total = 0

    i = 1
    if tipo_llantas == "S" or tipo_llantas == "s":
        while i < cantidad_vueltas:
            acumulacion_S += (78.80 + (0.15*i))
            i += 1
        vuelta_S += acumulacion_S
        total += vuelta_S
        i = 1
        return total
    elif tipo_llantas == "M" or tipo_llantas == "m":
        while i < cantidad_vueltas:
            acumulacion_M += (80 + (0.10*i))
            i += 1
        vuelta_M += acumulacion_M
        total += vuelta_M
        i = 1
        return total
    elif tipo_llantas == 'H' or tipo_llantas == "h":
        while i < cantidad_vueltas:
            acumulacion_H += (82.00 + (0.04*i))
            i += 1

        vuelta_H += acumulacion_H
        total += vuelta_H
        i = 1
        return total
    else:
        print("Ha ocurrido un error")


def main():
    continuar = True
    while continuar:
        opcion = menu()
        if opcion == "1":
            FuncionEquipo()
        elif opcion == "2":
            EquipoGanador()
        elif opcion == "0":
            continuar = False
        else:
            print("Ingresar una opción válida \n")


main()
