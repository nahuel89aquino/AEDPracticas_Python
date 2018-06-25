_author_ = 'JORGE NAHUEL AQUINO'

#titulo y carga de datos

print("Ejercicio nro 11 - Palabra enmascarada")
palabra = input("Ingrese una palabra: ")

#procesos..
tam = len(palabra)

#visualizacion de resultados

print(palabra[0]+'X'*(tam - 2)+palabra[tam-1])

