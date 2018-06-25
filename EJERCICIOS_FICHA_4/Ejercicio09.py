_author_ = 'NAHUEL AQUINO'

ANIO_ACTUAL = 2018

print("Ejercicio nro 9 - Galeria de arte:")

cuad1 = int(input("Ingrese años del cuadro:"))
cuad2 = int(input("Ingrese años del cuadro:"))
cuad3 = int(input("Ingrese años del cuadro:"))

antig1 = ANIO_ACTUAL - cuad1
antig2 = ANIO_ACTUAL - cuad2
antig3 = ANIO_ACTUAL - cuad3

if cuad1 <= 2000 and cuad2 <= 2000 and cuad3 <= 2000:
    if cuad1 > 1900 and cuad2 > 1900 and cuad3 > 1900:
        print("Todos los cuadros son del siglo XX\n")
else:
    print("Alguno cuadros no son del siglo XX\n")

if antig1 > 10 and antig2 > 10 and antig3 > 10:
    print('Renovar stock')

