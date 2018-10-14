import pickle
import os.path

def validar(msj, errmsj, inf, sup):
    valor = int(input(msj))
    if inf <= valor <= sup:
        return valor
    print(errmsj)
    return -1


def section_sort(nros):
    n = len(nros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nros[i] > nros[j]:
                nros[j], nros[i] = nros[i], nros[j]


def cargar(nros,fd):
    m = open(fd, "wb")
    for i in nros:
        pickle.dump(i, m)
    print("Archivo creado...")
    m.close()


def mostrar(fd):
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    k = 0
    print("Mostrando numeros sorteados...")
    while m.tell() < t:
        nro = pickle.load(m)
        print('Numero nro {0} sorteado: {1}'.format(str(k + 1), str(nro)))
        k += 1


def main():
    fd = "extracto.dat"
    nros = list()
    ops = -1

    while ops != 3:
        print("0- Cargar valores")
        print("1- Guardar valores ")
        print("2- Mostrar valores")
        print("3- Salir")
        ops = int(input("Elija una opcion: "))
        if ops == 0:
            while len(nros) < 6:
                n = validar("Ingrese los numeros sorteados: ", "Error. Se pido un numero entre 0 y 36", inf=0, sup=36)
                if n == -1:
                    continue
                nros.append(n)
            section_sort(nros)
            print(nros)
            print()
        elif ops == 1:
            cargar(nros, fd)
            print()
        elif ops == 2:
            mostrar(fd)
            print()


if __name__ == '__main__':
    main()
