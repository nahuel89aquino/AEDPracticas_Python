#Generar n numeros aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar
#el numero Hexadecimal

import random
MIN = 5000
MAX = 450000
valOk = False

#validacion del numero
while not valOk:
    n = int(input("Ingrese la cantidad de numeros aleatorio que decea convertir a hexadecimal: "))
    valOk = n >= 0
    if not valOk:
        print("Error: el valor ingresado no es un numero positivo")

for i in range(n):
    aleatorio = random.randint(MIN,MAX)
    print("Numero generado: ", aleatorio,"hexadecimal: ", hex(aleatorio), sep=" ")


