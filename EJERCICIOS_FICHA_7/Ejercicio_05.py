#el usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero.
#La frase finaliza con un punto, y las palabras estan separadas por espacios unicamente
#se debe mostrar:
#1) ver el porcentaje de vocales respecto del total de letras de la frase (ok)
#2) la longuitud promedio de las palabras(ok)
#3) la longuitud de la palabra mas larga del texto
#4) cantidad de palabras que comienzan con "ta"
vocal = ("a", "e", "i", "o", "u")
texto = "buen dia argentinaa mañana ganamos el partido tambien el mundial ata tta tata taza."
print("ingrese un texto, la frase finaliza con '.' :")
print(texto)
#texto = input()
cvocal = cletra = cpalabra = clpalabra = cltexto = cTA = 0
fpalabra = True
hayT = hayTA = False
for i in texto:
    #letra
    if i != " " and i != ".":
        if i in vocal:
            cvocal += 1
        if i.isalpha(): # si es un caracter alfanuemrico
            cletra += 1
        if cletra == 1 and i.upper() == 'T':
            hayT = True
        if hayT:
            if cletra == 2 and i.upper() == 'A':
                hayTA = True

    #palabra
    else:
        cpalabra += 1
        cltexto += cletra
        if hayTA:
            cTA += 1
        if fpalabra:
            may = cletra
            fpalabra = False
        if cletra > may:
            may = cletra
        cletra = 0
        hayTA = False
        hayT = False


#calculos
vocales_x100 = round(cvocal * 100 / cltexto, 2)
if cpalabra > 0:
    if cltexto > 0:
        prom = round(cltexto / cpalabra, 2)
    else:
        prom = 0
else:
    print("Error de inderterminacion division por '0' ", "\n")

print("cantidad de vocales: ", cvocal, "\n", "cantidad de letras: ", cltexto,sep="")
print("Porcentaje de vocales con respecto del total de letras: %", vocales_x100)
print("Longitud promedio de las palabras del texto:", prom)
print("Longitud de la palabra mas larga: ", may)
print("Cantida de letras que empiezan con 'ta' : ", cTA)
