_author_ = 'AQUINO NAHUEL'

#Desarrolle un programa que permita procesar funciones en un complejo de cines
#por cada funcion se conoce: cantidad de espectadores y descuento.la carga
#termina cuando la cantidad de espectadores sea igual a 0 (cero)
#El programa debera: a) calcular la recaudacion total del complejo,
#considerando que el valor de la entrada es de $50 en los dias de descuento y
#$75 en los dias sin descuento
#b) determinar cuantas funciones con descuento se efectuaron y que porcentaje
# representan sobre el total de funciones


VAL_DES = 50
VAL_SDES = 75
total_des, total_sdes, cant, rec,total_esp = 0, 0, 0, 0, 0

print("Ejercicio nro 1-Carga de espectadores")

nf = True
while nf:
    nro_esp = int(input("Ingrese la cantidad\
    total de espectadores en la sala: "))
    esp = 0
    total_esp = total_esp + nro_esp
    while nro_esp:
        print("espectador nro: ",esp + 1)
        des = input("Tiene descuento: S/N\t")
        if des == 'S'or des == 's':
            total_des = total_des + VAL_DES
            cant+=1
            print(total_des)
        else:
            total_sdes = total_sdes + VAL_SDES
            print(total_sdes)
        esp+=1
        nro_esp-=1
    rec = rec + (total_des + total_sdes)
    print("recaudacion parcial", rec)
    nf = int(input("Ingresar una nueva funcion?:\n\
    .1 'si' \n.0 'no' "))
print("Total de recaudacion: $",rec)
porc = cant * 100 / total_esp
print("Porcentaje de funciones con descuento: %", round(porc,2))
