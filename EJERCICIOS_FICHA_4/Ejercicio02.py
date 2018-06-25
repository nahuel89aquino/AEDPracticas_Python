_author_ = 'NAHUEL AQUINO'

#ingreso de datos y presentacion del programa
print("Ejercicio nro 2 - Impuesto Automotor")

anio = int(input("Ingrese el modelo del vehiculo: "))
mod = 2018 - anio

tipo = input("Ingrese el tipo de vehiculo\nP: para particular\n"
             "T: para taxis\nR: para remis\n")

#vehiculos particulares
if tipo == 'P' or tipo == 'p' or tipo == 'T' or tipo == 't':
    if mod < 10:
        imp = 200
    elif mod <= 20:
        imp = 150
    else:
        imp = 0
    if tipo == 'T' or tipo == 't':
        imp = imp + 150

else:
    imp = 100 * mod

print("El modelo ", mod, "del tipo '", tipo,"' paga un impuesto de: $",imp)





