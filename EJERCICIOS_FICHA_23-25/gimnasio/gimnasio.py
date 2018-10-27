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


def buscar(m, num, fd):
    t = os.path.getsize(fd)

    fp_inicial = m.tell()  # guarda la posicion del file pointer
    m.seek(0, io.SEEK_SET)  # regresa el file pointer a 0, importante para comenzar la lectura desde el inicio
    pos = -1
    while m.tell() < t:
        fd = m.tell()  # lee la posicion del file pointer antes de la lectura
        socio = pickle.load(m)
        if socio.activo and socio.numero == num:
            pos = fd
            break

    m.seek(fp_inicial, io.SEEK_SET)  # regresa el file pointer a su posicion original
    return pos


def opcion2(fd):
    if not os.path.exists(fd):
        print("Archivo no encontrado...")
        return
    num = validar("Ingrese el numero de socio a buscar", 0, 99999)
    m = open(fd, 'r+b')
    pos = buscar(m, num, fd)
    if pos != -1:
        # lectura
        m.seek(pos, io.SEEK_SET)
        socio = pickle.load(m)
        print("Datos de socio numero {}:".format(str(num)))
        display(socio)
        socio.plan = validar("Ingrese el tipo de plan", inf=0, sup=3)
        socio.monto = float(input("Ingrese el monto: $"))
        # modificiacion de los datos
        m.seek(pos, io.SEEK_SET)
        pickle.dump(socio, m)
        print("Se grabaron los cambios...")
        print("Datos actualizados del socio numero {}".format(str(num)))
        m.seek(pos, io.SEEK_SET)
        socio = pickle.load(m)
        display(socio)
        m.close()
    else:
        print("Socio no encontrado.")


def opcion4(fd):
    m = open(fd, "rb")
    t = os.path.getsize(fd)

    print("Datos del archivo...")
    while m.tell() < t:
        socio = pickle.load(m)
        if socio.activo:
            display(socio)
    m.close()


def opcion3(fd):
    if not os.path.exists(fd):
        print("Archivo no encontrado...")
        return
    num = validar("Ingrese el numero de socio a dar de baja", 0, 99999)
    m = open(fd, 'r+b')
    pos = buscar(m, num, fd)
    if pos != -1:
        # lectura de registro
        m.seek(pos, io.SEEK_SET)
        socio = pickle.load(m)
        print("Datos del socio a dar de baja: ")
        display(socio)
        # modificacion del registro
        socio.activo = False
        m.seek(pos, io.SEEK_SET)
        pickle.dump(socio, m)
        print("Socio eliminado...")
    else:
        print("Socio no encontrado...")
    m.close()


def depuracion(fd):
    m = open(fd, "rb")
    s = open("temporal.dat", "wb")

    t = os.path.getsize(fd)
    while m.tell() < t:
        socio = pickle.load(m)
        if socio.activo:
            pickle.dump(socio, s)
    m.close()
    s.close()

    # eliminacion
    os.remove(fd)
    # renombrado
    os.rename("temporal.dat", fd)


def opcion6(fd):
    print("Depuracion del archivo...")
    depuracion(fd)
    print("Contenido del archivo despues de la compactacion...")
    mostrar_lista(fd)


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
            opcion3(fd)
        elif ops == 4:
            opcion4(fd)
        elif ops == 5:
            pass
        elif ops == 6:
            opcion6(fd)
        elif ops == 7:
            pass

























if __name__ == '__main__':
    main()
