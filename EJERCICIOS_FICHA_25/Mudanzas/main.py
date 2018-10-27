import pickle
import os.path
import io
from AEDPracticas_Python.EJERCICIOS_FICHA_25.Mudanzas import registro


def menu():
    print("1. Cargar registros en el archivo de mudanzas")
    print("2. Mostrar el archivo creado")
    print("3. Mudanzas  cuya tarifa sea mayor a la tarifa promedio")
    print("4. Mostrar el arreglo creado")
    print("5. Cantidad de mudanzas realizadas con cada posible tipo de vehículo para cada uno de los posibles tipos de carga")
    print("6. Salir")


def alta(fd, reg):
    m = open(fd, 'ab')
    pickle.dump(reg, m)
    m.close()


def opcion1(fd):
    print("Cargando un registro de mudanzas...")
    print()
    ident = int(input("Ingrese el numero de identificacion: "))
    destino = input("Ingrese la direccion de destino: ")
    codigo = registro.validar_inter("Ingrese el codigo de vehiculo: ", sup=4)
    tarifa = float(input("Ingrese la tarifa del traslado: "))
    tipo = registro.validar_inter("Ingrese el tipo de carga que transporta: ", sup=9)
    mudanza = registro.Mudanzas(ident, destino, codigo, tarifa, tipo)
    # gurdando registro
    alta(fd, mudanza)
    #  mostrando registro
    print()
    registro.display(mudanza)


def mostrar(fd):
    if not os.path.exists(fd):
        print("Archivo no encontrado..")
        return
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        reg = pickle.load(m)
        print()
        registro.display(reg)
    m.close()


def opcion2(fd):
    print("Mostrando contenido del archivo")
    mostrar(fd)


def add_in_order(vector, reg):
    n = len(vector)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].ident == reg.ident:
            pos = c
            break
        if vector[c].ident < reg.ident:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq

    vector[pos:pos] = [reg]


def opcion3(fd, vector):
    ac, c = 0, 0
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        mudanza = pickle.load(m)
        ac += mudanza.tarifa
        c += 1
    prom = round(ac / c, 2)
    m.seek(0, io.SEEK_SET)
    print("Seleccionando Mudanzas con tarifa mayor al promedio...")
    while m.tell() < t:
        mudanza = pickle.load(m)
        if mudanza.tarifa >= prom:
            add_in_order(vector, mudanza)
    m.close()
    print(prom)
    print("Terminado...")


def opcion4(vector):
    for i in vector:
        print()
        registro.display(i)


def contar(fd, matriz):
    if not os.path.exists(fd):
        print("Archivo no encontrado...")
        return
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        mudanza = pickle.load(m)
        fila = mudanza.codigo
        colu = mudanza.tipo
        matriz[fila][colu] += 1
    m.close()


def mostrar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] != 0:
                print("Cantidad de mudanzas del tipo de vehiculo {} y del tipo de carga {} es de : {}".format(str(f), str(c), str(matriz[f][c])))


def opcion5(fd):
    tipos_vehiculos = 5
    tipo_carga = 10
    matriz = [[0] * tipo_carga for f in range(tipos_vehiculos)]
    contar(fd, matriz)
    mostrar_matriz(matriz)


def main():
    fd = 'mudanzas.dat'
    opc = -1
    vector = []
    while opc != 6:
        menu()
        opc = registro.validar_inter("Ingrese una opcion: ", inf=1, sup=6)
        if opc == 1:
            opcion1(fd)
        elif opc == 2:
            opcion2(fd)
        elif opc == 3:
            opcion3(fd, vector)
        elif opc == 4:
            opcion4(vector)
        elif opc == 5:
            opcion5(fd)
        elif opc == 6:
            pass


if __name__ == '__main__':
    main()
