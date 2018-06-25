_author_ = 'JORGE NAHUEL AQUINO'

#titulo general y carga de datos
print("Ejercicio nro 2 - Fecha como cadena")
date = input("Ingrese una fecha con formato 'dd/mm/aaaa' : ")

#procesos..

dia = date[0] + date[1]
mes = date[3] + date[4]
anio = date[6] + date[7] + date[8] + date[9]

#visualizacion de resultados..

print("Dia: ", dia ," - Mes: ", mes, " - Año: ",anio)
