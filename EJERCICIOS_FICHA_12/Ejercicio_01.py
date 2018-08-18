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


def menor(mes):
    men = mes[0]
    pos = 0
    for i in range(len(mes)):
        if men >= mes[i]:
            men = mes[i]
            pos = i
    return pos


def menu():
    meses = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO",
             "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")
    prom_trim = -1
    salir = False
    periodo = None
    # generacion aleatoria de precipitaciones
    mes = list()
    for i in range(12):
        mes.append(random.randint(40, 180))
    while not salir:
        print(mes)
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
            print("Seleccione el trimestre", "1 - 2 - 3 - 4")
            trimestre = validar()
            if trimestre == 1:
                print(mes[1:3])
                prom_trim = promedio(mes[1:3], 3)
                periodo = "primer"
            if trimestre == 2:
                print(mes[3:6])
                prom_trim = promedio(mes[3:6], 3)
                periodo = "segundo"
            if trimestre == 3:
                print(mes[6:9])
                prom_trim = promedio(mes[6:9], 3)
                periodo = "tercer"
            if trimestre == 4:
                print(mes[9:12])
                prom_trim = promedio(mes[9:12], 3)
                periodo = "cuarto"
            print("El promedio de lluvias para el", periodo, "trimestre es: ", prom_trim)
        elif opc == 3:
            men = menor(mes)
            print("El mes mas seco fue: ", meses[men])
        else:
            salir = True


if __name__ == '__main__':
    menu()
