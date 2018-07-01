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
    numdiv_4 = may = cont_prim = 0
    primer_impar = fue_primero = False
    num = -1
    while num != 0:
        num = int(input("Ingrese un numero:"))
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


    print("Cantidad de numeros divisibles por '4': ", numdiv_4)
    print("Mayor numero impar ingresado: ", may)
    print("Cantidad de veces que se ingreso el primer numero: ", cont_prim)

test()
