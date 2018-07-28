# Desarrollar un programa controlado por menú de opciones, que permita:
# a) Tablas: ingresar por teclado un valor positivo entre 1 y 10 (validarlo).
# Mostrar la tabla de multiplicar correspondiente a dicho número.
# (Por ej: si se ingresa 3, mostrar 3x1=3, 3x2=6 etc.)
# b) Mayor y menor: ingresar por teclado una sucesión de números positivos (validar),
# que termina cuando se ingresa 0. Informar mayor y menor valor de la sucesión.
# c) Múltiplos: ingresar por teclado dos valores a y b, siendo a positivo y b mayor que a (validarlo).
# Sumar todos los múltiplos de a comprendidos en el intervalo [a,b]
# d) Texto: ingresar por teclado un texto terminado en un punto (validar esto),
# cuyas palabras se separan por un único espacio.
# Informar cuántas palabras terminan en vocal y qué porcentaje representan sobre el total
# de palabras del texto.


def tablas(n):
    for i in range(1, 10 + 1):
        tabla = str(i) + ' * ' + str(n)
        print(tabla + " = " + str(eval(tabla)))


def mayor_menor(n):
    may = n[0]
    men = n[0]
    for i in n:
        if i > may:
            may = i
        if i < men:
            men = i
    return may, men


def multiplos(a, b):
    mul = 0
    for i in range(a, b + 1):
        if (i % a) == 0:
            mul += i
    return mul


def vocal(k):
    return k in ("a", "e", "i", "o", "u")


def textos(tex):
    cletra = cvol = 0
    hay_vocal = False
    for i in tex:
        if not (i == " " or i == "."):
            cletra += 1
            hay_vocal = False
            if vocal(i):
                hay_vocal = True
        else:
            if hay_vocal:
                cvol += 1
            hay_vocal = False
    porc = round(cvol * 100 / cletra, 2)
    return cvol, porc


def test():
    opciones = "1234"
    k = -1
    numeros = tuple()
    print("1) Tablas")
    print("2) Mayor y menor")
    print("3) Multiplos")
    print("4) Texto")
    n = input()
    # validacion de opcion principal
    while n not in opciones:
        print(Error1)
        n = input("Elije una opcion nuevamente: ")
    if n == "1":
        num = int(input("ingrese un numero positivo: "))
        while not num > 0:
            print(Error2)
            num = int(input("ingrese un numero positivo: "))
        tablas(num)
    if n == "2":
        while k != 0:
            k = int(input("Ingrese un numero: "))
            if k <= 0:
                print(Error2)
                continue
            numeros += k,
        print(numeros)
        mayor, menor = mayor_menor(numeros)
        print("El mayor valor de la serie es: ", mayor)
        print("El menor valor de la serie es: ", menor)
    if n == "3":
        a = b = None
        val_a = False
        while not val_a:
            a = input("Ingrese el valor a: ")
            es_num = a.isnumeric()
            if es_num and int(a) > 0:
                val_a = True
            else:
                print(Error2)
        val_b = False
        while not val_b:
            b = input("Ingrese el valor b mayor que a: ")
            es_num = b.isnumeric()
            if es_num and int(b) > int(a):
                val_b = True
            else:
                print(Error2)
        mul = multiplos(int(a), int(b))
        print("La suma de los multiplos de 'a' comprendidios en el intervalo son: ", mul)

    if n == "4":
        texto = input("Ingrese un texto:")
        texto += "."
        t_voc, porc_voc = textos(texto)
        print("La cantidad de vocales del texto son", t_voc)
        print("El porcentaje de vocales que representan sobre el total de palabras es: %", porc_voc)


# texto = "hoy es un lindo dia para comer un asado"
Error1 = "Error: opcion no valida"
Error2 = "Error: valor invalido"
test()
