_author_ = 'JORGE NAHUEL AQUINO'

#titulo y carga de datos
print("Ejercicio nro 5 - Control electoral")
apellido = input("Ingrese el apellido del candidato: ")
nombre = input("Ingrese el nombre del candidato: ")
votos = int(input("Ingrese cantidad de votos: "))

#procesos
#Convertir las minúsculas en mayúsculas se logra cambiando .lower() por upper()
mensaje = apellido[0]+nombre[0]+"\n\t\t"+'X'*votos
mensajeA = mensaje.upper()
#visualizacion de datos..
print("candidato:\n\t\t",mensajeA)
