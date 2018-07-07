#1) Determinar cuantos números se encuentran en el rango definido por 2 números p y q previamente
# ingresados (validar que los números que definen el rango son mayores a cero)
#2) Determinar la cantidad de veces que se ingresaron 2 números contiguos pares
#3) Determinar la cantidad de números que son múltiplos del primer numero de la secuencia
#4) Determinar el porcentaje que representa la cantidad del primer
# punto sobre el total de números de la secuencia
def par(x):
    return x % 2 == 0
def porcentaje(suma, total):
    if total != 0:
        porc = round(suma / total, 2)
    else:
        porc = -1
    return porc

def test():
    numeros = (3, 3, 5, 5, 5, 2, 6, 4, 2, 4, 6, 3, 3, 5, 5, 5, 5, 9, 7, 0)
    p = int(input("Ingrese el numero limite inferior del intervalo: "))
    q = int(input("Ingrese el numero limite superior del intervalo: "))
    num = -1
    primero = numeros[0]
    hay_par = hay_2par = False
    i = pq_cont = cont2par = cont_mul = 0
    while num != 0:
        num = numeros[i] #simula carga de numeros por teclado
        i += 1
        print(num, end=" ")
        #1)
        if p < num < q:
            pq_cont += 1
        #2)
        if not hay_par and par(num):
            hay_par = True
        else:
            if not hay_2par and par(num):
                hay_2par = True
            else:
                hay_par = False
        if hay_par and hay_2par:
            cont2par += 1
            hay_2par = hay_par = False
        if num % primero == 0:
            cont_mul += 1
    porc = porcentaje(pq_cont, i)
    if porc == -1:
        porc = "Error: division por cero"
    print()
    print("Cantidad de numeros en el intervalo de p y q: ", pq_cont)
    print("Cantidad de veces que se ingresaron dos numeros pares contiguos: ", cont2par)
    print("Cantidad de numeros que son multiplos del primer numero", cont_mul)
    print("Porcentaje que la cantidad de numero del primer punto representa sobre el total: ", porc)


test()
