_author_ = 'JORGE NAHUEL AQUINO'

#valores constantes
MENSAJE = 'EL PRESUPUESTO PARA CADA AREA SERÁ\n'
CAMPO1 = 'URGENCIAS: '
CAMPO2 = 'PEDIATRIA: '
CAMPO3 = 'TRAUMATOLOGIA: '

pres_ped = 0.42
pres_urg = 0.37
pres_tra = 0.21

#titulo y carga de datos
print("Ejercicio nro 7 - Cálculo de presupuesto")
pres_anual = int(input("Ingrese el presupuesto total anual del hospital: "))

#procesos...
ped = pres_anual * pres_ped
urg = pres_anual * pres_urg
tra = pres_anual * pres_tra

#visualizacion de resultados
print(MENSAJE+CAMPO1+str(urg)+'\n'+CAMPO2+str(ped)+'\n'+CAMPO3+str(tra))
