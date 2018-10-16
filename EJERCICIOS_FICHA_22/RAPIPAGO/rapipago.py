import pickle
import os.path


class Cobro():
    def __init__(self, fecha, tipo, monto, nro_cuenta):
        self.fecha = fecha
        self.tipo = tipo
        self.monto = monto
        self.cuenta = nro_cuenta


class Fecha():
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio


def mostrar_fecha(f):
    print(f.dia + "/" + f.mes + "/" + f.anio)


def display(x):
    print("-" * 50)
    print("Fecha: ", end=" ")
    mostrar_fecha(x.fecha)
    print("-- Tipo de servicio: ", x.tipo)
    print("-- Monto pagado: $ ", x.monto)
    print("-- Numero de cuenta: ", x.cuenta)
    print("-" * 50)


def menu():
    print()
    print("1- Agregar un nuevo cobro al archivo de cobros.")
    print("2- Determinar el monto total para un número de cuenta X pasado por parámetro")
    print("3- Indicar el monto total acumulado para cada servicio, en el día del mes que se lo cobro.")
    print("4- Indicar, a partir de la matriz, el día con mayor monto cobrado")
    print("5- Indicar, a partir de la matriz, el promedio cobrado para el servicio X pasado por parámetro")
    print()


def ingresar(msj, errmsj, inf=0, sup=0):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print(errmsj)
        valor = int(input(msj))
    return valor


def ingresarfecha():
    ok = False
    dia = mes = anio = div = ""
    while not ok:
        f = input("Ingrese fecha: ")
        for i in f:
            if i != "/":
                if div == "":
                    dia += i
                elif div == "/":
                    mes += i
                elif div == "//":
                    anio += i
            else:
                div += i
        ok = (1 <= int(dia) <= 31) and (1 <= int(mes) <= 12) and (int(anio) > 1900)
        if not ok:
            print("Error de ingreso de fecha")
            dia = mes = anio = div = ""
    fecha = Fecha(dia, mes, anio)
    return fecha


def guardar(reg, fd):
    m = open(fd, "ab")
    pickle.dump(reg, m)
    m.close()


def cargar(fd):
    fecha = ingresarfecha()
    tipo = ingresar("Ingrese tipo de servicio: ", "Error. Valor entre 1 y 15", inf=1, sup=15)
    monto = float(input("Ingrese el monto : $"))
    cuenta = int(input("Ingrese el numero de cuenta: "))
    cobro = Cobro(fecha, tipo, monto, cuenta)
    guardar(cobro, fd)
    print("Guardado...")


def buscarmonto(fd):
    monto = None
    cuenta = int(input("Ingrese el numero de cuenta a buscar: "))
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        cobro = pickle.load(m)
        if cuenta == cobro.cuenta:
            monto = cobro.monto
    m.close()
    if monto is None:
        print("No se encontro cuenta.")
    else:
        print("El monto de la cuenta Nro: {0} es de : $ {1}".format(cuenta, monto))


def mostrar_matriz(montos):
    for f in range(len(montos)):
        for c in range(len(montos[0])):
            print("{0:>5}".format(str(montos[f][c])), end="")
        print()


def montosxservicios(fd):
    montos = [[0] * 30 for f in range(15)]
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        cobro = pickle.load(m)
        display(cobro)
        fecha = cobro.fecha
        tipo = cobro.tipo
        montos[tipo - 1][int(fecha.dia) - 1] += 1
    mostrar_matriz(montos)


def main():
    fd = "cobros.dat"
    ops = -1
    while ops != 6:
        menu()
        ops = ingresar("Seleccione opcion: ", "Error: se solicita un numero entre 1 y 6", inf=1, sup=6)
        if ops == 1:
            cargar(fd)
        elif ops == 2:
            buscarmonto(fd)
        elif ops == 3:
            montosxservicios(fd)
        elif ops == 4:
            pass
        elif ops == 5:
            pass


if __name__ == '__main__':
    main()
