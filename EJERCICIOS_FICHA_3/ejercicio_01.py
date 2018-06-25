_author_ = 'AQUINO JORGE NAHUEL'

#DECLARACIÓN DE CONSTANTES DEL PROGRAMA
COMISION = 20
INTERES = 2.3

#TITULO GENERAL Y CARGA DE DATOS
print("Ejercicio nro 1 - Plazo Fijo\n")
deposito = float(input("Ingrese el monto a depositar en "
                       "su cuenta de plazo fijo: "))

#PROCESOS..
valor_neto = deposito - COMISION
saldo = round(valor_neto + (valor_neto * INTERES / 100),2)

#visualizacion de resultados..
print("Saldo que tendra la cuenta al vencimento del plazo fijo ser: ", saldo)


