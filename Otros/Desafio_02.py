# Sucesion de Collatz


def par(n):
    return n % 2 == 0


def promedio(v):
    sm = 0
    n = len(v)
    for i in range(n):
        sm += v[i]
    prom = round(sm / n, 1)
    return prom


def mayor_val(v):
    mayor = 0
    n = len(v)
    for i in range(n):
        if v[i] > v[mayor]:
            mayor = i
    return mayor


def test():
    v = []
    salida = False

    i = 0
    x = int(input("Ingrese el valor 'n' de la succesion de Collatz: "))
    v.append(x)

    while not salida:

        if par(int(v[i])):
            val = round(v[i] / 2)
            v.append(val)
        else:
            val = round(3 * v[i] + 1, 2)
            v.append(val)

        if v[i + 1] == 1:
            salida = True
        i += 1
    # calculo del promedio

    prom = promedio(v)

    # calculo del mayor
    mayor = mayor_val(v)

    print("Orbita de n = " + str(x) + " : ")
    print(v)
    print("Longitud de la orbita: ", len(v))
    print("El promedio de los valores de la sucesion es: ", prom)
    print("El mayor numero en esa orbita: ", v[mayor])


test()
