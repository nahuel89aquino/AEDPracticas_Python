import pickle
import os.path


class Alquiler():
    def __init__(self, dni, monto, cod):
        self.dni = dni
        self.monto = monto
        self.tipo = cod


def imprimir(reserva):
    print("-- DNI: {0} -- monto = $ {1} -- codigo de reserva: {2}".format(reserva.dni,
                                                                str(reserva.monto), str(reserva.tipo)))


def menu():
    print("1- Cargar reservas")
    print("2- Guardar reservas que superen un cierto monto")
    print("3- Mostrar monto recaudado por cada tipo de alquiler")
    print("4- Salir")


def ingresar(msj, errmsj, inf=0, sup=0):
    valor = int(input(msj))
    if sup != 0:
        while inf > valor or sup < valor:
            print(errmsj)
            valor = int(input(msj))
    else:
        while inf > valor:
            print(errmsj)
            valor = int(input(msj))
    return valor


def cargar():
    dni = input("Ingrese el DNI del titular de la reserva: ")
    monto = float(input("Ingrese el monto de la reserva: $ "))
    cod = ingresar("Ingrese el codigo de reserva: ", "Error: valor requerido entre 0 y 9", sup=9)
    return Alquiler(dni, monto, cod)


def item1(alquileres):
    cant_registros = ingresar("Ingrese la cantidad de reservas a cargar: ", "Error: debe ser un numero positivo", inf=0)

    for i in range(cant_registros):
        reserva = cargar()
        alquileres.append(reserva)
        imprimir(alquileres[i])
    print()


def item2(alquileres, fd):

    monto_x = float(input("Ingrese el limite inferior del monto: $"))
    m = open(fd, "wb")
    print("Guardando alquileres que superan el monto ${}... ".format(str(monto_x)))
    for i in alquileres:
        if i.monto > monto_x:
            pickle.dump(i, m)


def item3(fd):
    acum_monto = [0] * 10

    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        reserva = pickle.load(m)
        acum_monto[reserva.tipo] += reserva.monto
    for i in range(10):
        print("Montos del  tipo {0}: $ {1}".format(str(i), str(round(acum_monto[i], 2))))


def main():
    ops = -1
    alquileres = list()
    fd = "reservas.dat"
    while ops != 4:
        menu()
        ops = ingresar("Ingrese una opcion: ", "Error: valor entre 1 y 4", inf=1, sup=4)
        if ops == 1:
            item1(alquileres)
        elif ops == 2:
            item2(alquileres, fd)
        elif ops == 3:
            item3(fd)


if __name__ == '__main__':
    main()
