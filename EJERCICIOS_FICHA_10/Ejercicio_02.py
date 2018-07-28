# Desarrollar un programa en phyton que permita cargar por teclado una secuencia de numeros, uno por uno.
# Siempre se supone que el usuario cargara un 0 (cero) para indicar el fin del proceso de carga.
# El cero no debe considerarse un dato a procesar. El programa debe.
# a) Determinar el porcentaje que cantidad de numeros pares representa en la cantidad total de numeros ingresados.
# b) Determinar cuantos de los numeros ingresados tenian su ultimo digito igual a 4 o igual a 5.
# c) Determinar el menor de los numeros ingresados que sea divisible por 3.
# d) Determinar si la secuencia estaba formada solo por numeros menores o iguales que 7.


def validado(n):
    es_num = True
    for i in n:
        if not ("0" <= i <= "9"):
                es_num = False
    return es_num


def es_par(n):
    return int(n) % 2 == 0


def finaliza(n):
    hay4_5 = False
    for i in n:
        hay4_5 = False
        if i == "5" or i == "4":
            hay4_5 = True

    return hay4_5


def divisor(n):
    return int(n) % 3 == 0


def test():
    num = -1
    primero = mayor_7 = False
    cont_num = cont_par = cont_final = menor = 0
    num = input("ingrese un numero: ")
    while num != "0":
        if not validado(num):
            print(ERROR1)
            continue
        cont_num += 1
        if es_par(num):
            cont_par += 1
        if finaliza(num):
            cont_final += 1
        if divisor(num):
            if not primero:
                menor = num
                primero = True
            if int(num) <= int(menor):
                menor = num
        if int(num) > 7:
            mayor_7 = True

        num = input("ingrese un numero: ")
    porc_pares = cont_par * 100 / cont_num
    print("El porcentaje de numeros pares es: %", porc_pares)
    print("La cantidad de numeros que finalizan con 4 o 5 son: ", cont_final)
    print("El menor de los numeros ingresados que es divisible por 3 es: ", menor)
    if not mayor_7:
        print("La secuencia ha sido conformada por numeros menores a 7")


ERROR1 = "Error: valor invalido"
test()
