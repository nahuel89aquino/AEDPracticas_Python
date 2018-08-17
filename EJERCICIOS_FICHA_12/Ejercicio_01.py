# Pluviometro
# Se ha solicictado un programa que permita cargar las precipitaciones promedio en cada mes del pais,
# en base a estos datos armar un menu de opciones que permita:
# 1- Determinar el promedio anual de lluvias
# 2- Determinar el promedio de lluvias para un determinado trimestre
# 3- Determinar el mes mas seco del año


import random


def validar(val=-1):
    check = False
    while not check:
        val = input()
        if val < "1" or val > "4":
            print("Error: el valor ingresado no es valido")
            print("Se solicita un numero entre 1 y 4")
        else:
            check = True
    return int(val)


def promedio(v, cant):
    suma = 0
    for i in v:
        suma += i
    prom = round(suma / cant, 2)
    return prom


def menu():
    salir = False
    # generacion aleatoria de precipitaciones
    mes = list()
    for i in range(12):
        mes.append(random.randint(40, 180))
    while not salir:
        print("Ejercicio Ficha 12 - Pluviometro")
        print("1- Determinar el promedio anual de lluvias")
        print("2- Determinar el promedio de lluvias para un determinado trimestre")
        print("3- Determinar el mes mas seco")
        print("4- Salir")
        opc = validar()
        if opc == 1:
            prom_anual = promedio(mes, len(mes))
            print("Promedio anual de lluvias: ", prom_anual, "mm")
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        else:
            salir = True


menu()
