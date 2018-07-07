#1) Determinar cuantos de los nuemeros ingresados eran mayores que n1 y menores que n2
#(cargar previamente por teclado los numero n1 y n2)
#2) Determinar el porcentaje de que el total de numeros calculdo en el punto 1 representa en el total
# de numeros cargados
#3) Determinar si se ingreso un numero impar seguido inmediatamente de uno par. No importa cuantas
# veces ocurrio, solo indicar si alguna vez paso
#4) Determinar cuantas veces se ingreso un 5 seguido de otro 5.
def par(x):
    return x % 2 == 0

def porcentaje(suma, total):
    if total != 0:
        porc = round(suma / total, 2)
    else:
        porc = -1
    return porc

def test():
    numeros = (1, 3, 5, 5, 5, 2, 6, 4, 2, 4, 6, 3, 3, 5, 5, 5, 5, 9, 7, 0)
    hay_inpar = hay_5 = hay_55 = par_inpar = False
    num = -1
    i = n1_n2_cont = cont_55 = 0
    n1 = int(input("Ingrese el numero limite inferior del intervalo: "))
    n2 = int(input("Ingrese el numero limite superior del intervalo: "))


    while num != 0:
        num = numeros[i] #simula carga de numeros por teclado
        i += 1
        print(num, end=" ")

        # 1)
        if n1 < num < n2:
            n1_n2_cont += 1
        #3)
        if par(num) and not hay_inpar:
            hay_inpar = True

        else:
            if hay_inpar and not par(num):
                par_inpar = True
            else:
                hay_inpar = False
        #4)
        if not hay_5 and num == 5:
            hay_5 = True
        else:
            if not hay_55 and num == 5:
                hay_55 = True
            else:
                hay_5 = False
        if hay_5 and hay_55:
            cont_55 += 1
            hay_55 = hay_5 = False
    #2)
    porc = porcentaje(n1_n2_cont, i)
    if porc == -1:
        porc = "Error: division por cero"

    print("\n")
    print("Cantidad de numero en el intervalo: ", n1_n2_cont)
    print("Porcentaje de numeros pertenecientes al intervalo: ", porc)
    if par_inpar:
        print("Se han ingresado numeros inpares seguido de un numero par")
    else:
        print("No se han ingresado numeros inpares seguido de un numero par")
    print("Cantidad de vecese que se ha ingresado la secuencia '55': ",cont_55)



test()
