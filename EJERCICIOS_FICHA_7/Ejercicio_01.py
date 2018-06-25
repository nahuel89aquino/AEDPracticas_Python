#La final de una carrera de ciclistas tiene n competidores (n se ingresa por
#teclado).
#Desarrollar un programa que permita cargar, por cada competidor,
#nombre y tiempo de carrera. Luego se pide:
#a) Determinar y mostrar el nombre del ganador de la carrera.
#b) Ingresar por teclado el tiempo record registrado para dicha carrera.
#Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
#c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

print("Ejercicio Nro 1 - Ciclistas")
print('='*30)

may_name = t_men = i = 0
j = 2
primero = True
tiempo = val = 0

n = int(input("Ingrese la cantidad de competidores: "))

for c in range(n):
    name = input("Ingrese el nombre del competidor ")
    t = input("Ingrese el tiempo realizado en formato hh:mm:ss") + ':'

    #conversion de tiempo
    for k in t:
        if primero:
            i = 1
            primero = False
        else:
            i = 0
        if k != ':':
            val += (int(k) * (10 ** i))
        else:
            tiempo += (val * (60 ** j))
            j -= 1
            val = 0
            primero = True
    j = 2
print(tiempo)
