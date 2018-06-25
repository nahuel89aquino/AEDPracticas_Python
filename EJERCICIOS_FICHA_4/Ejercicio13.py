_author_ = 'NAHUEL AQUINO'

import random

GANA_MAQ = '\nGANA MAQUINA'
GANA_JUG = '\nGANA JUGADOR'

print("Ejercicio nro 13 - Juego de priedra, papel o tijera")
opc = 'piedra', 'papel', 'tijera'
#eleccion del jugador
eleccion = int(input("Elija las opciones:\n0.piedra\n1.papel\n2.tijera\n"))
jugador = opc[eleccion]
#eleccion de la maquina

maquina = random.choice(opc)
print("Su eleccion: ", jugador)
print("Eleccion del maquina: ",maquina)

#deciciones de ganador
gana_maquina = maquina == 'papel' and jugador == 'piedra' or\
               maquina == 'piedra' and jugador == 'tijera' or\
               maquina == 'tijera' and jugador == 'papel'

if maquina == jugador:
    print("\nEMPATE")
else:
    if gana_maquina:
        print(GANA_MAQ)
    else:
        print(GANA_JUG)

