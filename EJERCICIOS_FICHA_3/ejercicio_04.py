_author_ = 'JORGE NAHUEL AQUINO'

#constantes del programa

TRASLADO = 45

#titulo general y carga de datos

print("Ejercicio nro 4 - Duracion de un vuelo")
start = input("Ingrese horario de partida del vuelo en formato 'hh:mm' : ")
end = input("Ingrese horario de llegada del vuelo en formato 'hh:mm' : ")

#procesos..
#convercion de horas a minutos
inicio = int( start[0]+ start[1]) * 60 + int( start[3] + start[4])
fin = int( end[0]+ end[1]) * 60 + int( end[3] + end[4])

duracion = fin - inicio

travel_end = duracion + TRASLADO

#visualizacion de resultados
print("Horario de partida : ", start, "hs")
print("Horario de partida : ", end, "hs")
print("La duración del viaje será de ",duracion," min", "\nEl tiempo total hasta el "
    "hotel sera de ",travel_end," min")
