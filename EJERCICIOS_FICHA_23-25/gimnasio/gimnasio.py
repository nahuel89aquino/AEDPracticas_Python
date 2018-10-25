import pickle
import os.path
import io

class Socios():
    def __init__(self, num, nombre, plan, monto):
        self.numero = num
        self.nombre = nombre
        self.plan = plan
        self. monto = monto
        self.activo = True


def display(x):
    print("Numero de socio: {} - Nombre: {}\nPlan: {} - Monto: ${} ".format(x.numero, x.nombre,
                                                                            x.plan, x.monto))


def menu():
    print("1- Realizar el alta de un nuevo socio, cargando todos los datos")
    print("2- Modificar un usuario, actualizando su plan y el monto mensual que abona")
    print("3- Realizar la baja lógica de un socio")
    print("4- Mostrar el contenido del archivo")
    print("5- Determinar el monto total que se ha cobrado por cada tipo de plan")
    print("6- Realizar la compactación del archivo, eliminando físicamente del archivo los socios dados de baja")
    print("7- Salir")


def planes():
    return "Completo", "Gimnasio", "Natatorio", "Pilates"


def validar(msj, inf, sup):
    valor = int(input(msj))
    while not (inf <= valor <= sup):
        print("Valor no valido...Ingrese nuevamente un valor entre {} y {}".format(str(inf), str(sup)))
        valor = int(input(msj))
    return valor


def alta(file):
    print("Nuevo socio..")
    m = open(file, "a+b")
    num = validar("Ingrese un numero", inf=0, sup=99999)
    nombre = input("Nombre: ")
    plan = validar("Ingres el tipo de plan", inf=0, sup=3)
    monto = float(input("Ingrese el monto: $"))
    socio = Socios(num, nombre.ljust(40, " "), plan, monto)
    pickle.dump(socio, m)
    m.close()


def mostrar_lista(fd):
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        socio = pickle.load(m)
        display(socio)
    m.close()


def opcion1(fd):
    alta(fd)
    print()
    mostrar_lista(fd)


def buscar(m, num):
    global fd
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)
    pos = -1
    while m.tell() < t:
        fd = m.tell()
        socio = pickle.load(m)
        if socio.activo and socio.numero == num:
            pos = fd
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return pos


def opcion2(fd):
    if not os.path.exists(fd):
        print("Archivo no encontrado...")
        return
    num = validar("Ingrese el numero de socio a buscar", 0, 99999)
    m = open(fd, 'r+b')
    pos = buscar(m, num)


def main():
    fd = "socios.dat"
    ops = -1
    while ops != 7:
        menu()
        ops = int(input("Ingrese una opcion: "))
        if ops == 1:
            opcion1(fd)
        elif ops == 2:
            opcion2(fd)
        elif ops == 3:
            pass
        elif ops == 4:
            pass
        elif ops == 5:
            pass
        elif ops == 6:
            pass
        elif ops == 7:
            pass

























if __name__ == '__main__':
    main()
