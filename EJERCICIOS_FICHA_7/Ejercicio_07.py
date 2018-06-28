#La frase debe terminar con un punto(al aparecer el punto, la carga debe finalizar)
#El programa debe informar:
#a) Promedio de letras por palabra
#b) Cantidad de palabras que terminan con la letra 's' (minuscula)
#c) Cantidad de palabras que contienen a la silaba 'sa' (minuscula)


texto = "el verdadero signo de la inteligencia no es el conocimiento si no la imaginsacion sa"
texto += "."
print(texto)
#contadores
cletras = cS = cSA = total_letras = cpal = 0
#banderas
endS = tieneS = tieneSA = False
#inicio del ciclo
for i in texto:
    if i.isalpha() and i != ".":
        cletras += 1
        endS = False

        if i == "s":
            endS = True
            tieneS = True
        elif tieneS and i == "a":
            tieneSA = True
        else:
            tieneS = False

    else:
        total_letras += cletras
        cpal += 1
        if tieneSA:
            cSA += 1
        if endS:
            cS += 1
        cletras = 0
        endS = tieneSA = tieneS = False

#calculos
print("total de letras: ", total_letras, "total de palabras: ", cpal)
prom = round(total_letras/cpal,2)

#resultados
print("promedio de letras por palabra", prom)
print("Cantidad de palabras terminadas en 's' : ", cS)
print("Cantidad de palabras que contienen a la silaba 'sa' :", cSA)
