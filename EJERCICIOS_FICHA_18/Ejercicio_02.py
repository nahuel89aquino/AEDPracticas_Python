# analizando temperaturas


class Datos:
    def __init__(self, region, mes, t_max, t_min):
        self.region = region
        self.mes = mes  # valor del 1 al 12
        self.temp_max = t_max
        self.temp_min = t_min


def write(dato):
    print("Region: ", dato.region)
    print("Mes: ", dato.mes)
    print("Temperatura maxima: ", dato.temp_max)
    print("Temperatura minima: ", dato.temp_min)


def menu():
    print('1. Cargar analisis termicos.')
    print('2. Temperatura maxima en el primer semestre')
    print('3. Informar region y el mes en el que se registro la menor minima del año')
    print('4. Salir')


def validar():
    valor = int(input('Ingrese un valor entre 1 y 12: '))
    while not (1 <= valor <= 12):
        print('Error. valor fuera del rango')
        valor = int(input('Ingrese un valor entre 1 y 12: '))
    return valor


def menor_minima(v_datos):
    n = len(v_datos)
    menor = 0
    for i in range(n):
        if i == 0:
            menor = v_datos[i].temp_min
            mes = v_datos[i].mes
            region = v_datos[i].region

        if menor > v_datos[i].temp_min:
            menor = v_datos[i].temp_min
            mes = v_datos[i].mes
            region = v_datos[i].region
    return int(mes), region


def main():
    salir = creado = False
    meses = ("Enero", "Febrero", "Marzo", " Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre",
             "Diciembre")
    print('Analizando Temperaturas - Ejercicio 2 Ficha 18')
    while not salir:
        menu()
        acum = cont = 0
        ops = int(input("Elija una opcion: "))
        if ops == 1:
            creado = True
            n = validar()
            v_datos = [None] * n
            for i in range(len(v_datos)):
                region = input("Ingrese la region: ")
                mes = input('Ingrese el mes: ')
                t_max = float(input("Ingrese la temperatura maxima: "))
                t_min = float(input("Ingrese la temperatura minima: "))
                v_datos[i] = Datos(region, mes, t_max, t_min)
        if ops == 2:
            if creado:
                for i in range(n):
                    if 1 <= int(v_datos[i].mes) <= 6:
                        cont += 1
                        acum += v_datos[i].temp_max
                prom = round(acum / cont, 2)
                print('Promedio de la temperatura maxima en el primer trimestre', prom)
            else:
                print('Debe ingresar datos')
                print()
        if ops == 3:
            if creado:
                mes, reg = menor_minima(v_datos)
                print("La menor minima fue registrada en el mes de {0} y fue en la region {1}".format(meses[mes - 1], reg))

            else:
                print('Debe ingresar datos')
                print()
        if ops == 4:
            salir = True


if __name__ == '__main__':
    main()
