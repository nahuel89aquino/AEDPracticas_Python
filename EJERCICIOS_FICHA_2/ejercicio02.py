monto_inical=float(input('Ingrese el monto actual del medicamento: '))
Desc=monto_inical*0.35
monto_final=monto_inical-Desc
print("El monto inicial del medicamento es: $",monto_inical,"\nEl descuento del 35% es: $ ",round(Desc,2),"\nEl monto final a pagar es: $",round(monto_final,2))
