#CARGAR POR TECLADO DOS NUMEROS , E IMPRIMIR LOS NUMEROS IMPARES QUE SE ENCUENTREN COMPRENDIDOS ENTRE ELLOS
#, EN FORMA ASCENDENTE Y DESCENDENTE
validado = check1 = check2 = False
#carga de numeros
while not validado:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    if num1 >= 0:
        check1 = True
    print(check1)
    if num2 >= 0:
        check2 = True
    print(check2)
    validado = check1 and check2
    if not validado:
        print("error: algunos de los valores ingresados no son numero")

#determinar orden de los numeros
if num1 >= num2:
    may = num1
    men = num2
else:
    may = num2
    men = num1
#forma ascendente
for asc in range(men, may + 1, 1):
    if asc % 2 != 0:
        print(asc, end=" ")
print("\n")
#forma descendente
for desc in range(may, men - 1, -1):
    if desc % 2 != 0:
        print(desc, end=" ")

print("\n")


