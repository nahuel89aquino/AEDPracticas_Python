# Desarrollar un programa que permita cargar por teclado un vector de 'n' elementos y luego:
# 1- Informe cuantas veces se repite el valor del ultimo numero ingresado
# 2- Genere un nuevo vector, conteniendo solo los elementos menores al primer valor ingresado


def valido():
    val = input()
    ok = False
    while not ok:
        if val.isnumeric():
            ok = True
        else:
            print("Valor invalido: no es un numero")
            val = input()
    return int(val)


def contador(valor, v):
    c = 0
    for i in range(len(v)):
        if valor == v[i]:
            c += 1
    return c


def menor(valor, v):
    k = []
    for i in range(len(v)):
        if valor > v[i]:
            k.append(v[i])
    return k[:]


def test():
    v = []
    salir = False
    print("Ejercicio nro 2 - Primero y ultimo")
    print("Ingrese la cantidad de elementos del vector:")
    n = valido()
    print("Ingrese los valores del vector")
    for i in range(n):
        print("Valor nro", i + 1, ":", end=" ")
        v.append(valido())
    print(v)
    while not salir:
        print("Elija una opcion")
        print("1- Cantidad de veces que se repite el ultimo numero ingresado")
        print("2- Elementos menor al primer valor ingresado")
        print("3- salir")
        opc = valido()
        if opc == 1:
            cant = contador(v[-1], v)
            print("Cantidad de veces que se repite el ultimo valor: ", cant)
        if opc == 2:
            menores = menor(v[0], v)
            print(menores)

if __name__ == "__main__":
    test()
