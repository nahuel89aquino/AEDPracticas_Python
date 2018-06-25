_author_ = 'NAHUEL AQUINO'

#ingreso de variables y presentacion del ejercicio
print("Ejercicio nro 1 - Suma, division y potencia\n")
a = int(input("Ingrese un numero:"))
b = int(input("Ingrese un numero:"))
c = int(input("Ingrese un numero:"))

#procesos
suma = a + b + c

if suma > 10:
    print("La suma se divide por 2, el resultado es:", suma // 2)

else:
    print("La suma se eleva al cuadrado, el resultado es:", suma ** 2)
