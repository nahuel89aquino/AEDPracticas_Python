#1) Determinar cuantos de los numeros ingresados eran divisibles por 4
#2) Determinar el mayor de los numeros impares
#3) Determinar cuantas veces se ingreso el primero del los numeros (cuente al primero)
#4) Determinar cuantas veces se ingreso un 1, seguido de un 2 y seguido a su vez de un 3.

def impar(x):
    return x % 2 != 0
def divisible_4(x):
    return x % 4 == 0
def mayor(may, num):
    if num >= may:
        return num
    else:
        return may

def test():
    numdiv_4 = may = cont_prim = cont123 = 0
    primer_impar = fue_primero = hay_1 = hay_12 = hay_123 = False
    num = -1
    while num != 0:
        num = int(input("Ingrese un numero (con cero finaliza):"))
        if num == 0:
            break
        if divisible_4(num):
            numdiv_4 += 1
        if impar(num):
            if not primer_impar:
                may = num
                primer_impar = True
            may = mayor(may, num)
        if not fue_primero:
            ft_num = num
            fue_primero = True
        if ft_num == num:
            cont_prim += 1
        if not hay_1 and num == 1:
            hay_1 = True
            hay_12 = False
        else:
            if not hay_12 and num == 2:
                hay_12 = True
                hay_1 = False
            else:
                if hay_12 and num == 3:
                    hay_123 = True
                else:
                    hay_12 = False
                    hay_1 = False
        print(hay_1,hay_12,hay_123)
        if hay_123:
            cont123 += 1
            hay_123 = hay_12 = hay_1 = False



    print("Cantidad de numeros divisibles por '4': ", numdiv_4)
    print("Mayor numero impar ingresado: ", may)
    print("Cantidad de veces que se ingreso el primer numero: ", cont_prim)
    print("Cantidad de veces que se ingreso la secuencia 123: ", cont123)

test()
