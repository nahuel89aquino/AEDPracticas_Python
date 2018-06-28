#a) Determinar cuantas palabras tiene exactamente 3 letras
#b) Determinar el porcentaje que las palabras del punto 1 representan en el total
#de palabras del texto
#c) Determinar cuantas palabras terminar en letra 's'
#d) Determinar cuantas palabras contuvieron al menos una ves la exprecion 'dre'

texto = "hoy es un lindo dia para comer un asado maddres.re"
texto += "."

hay_dre = tiened = tienedr = endS = False
print(texto)
cDre = cletras = cpalabras = len_tres = finS = 0
for i in texto:
    if i.isalpha():
        endS = False
        cletras += 1
        #comparador de tres letras
        if not tiened and i == "d":
            tiened = True
            #tienedr = False
        else:
            if not tienedr and i == "r":
                tienedr = True

            else:
                if tienedr and i == "e":
                    hay_dre = True


                tienedr = False
            tiened = False

        if i == "s":
            endS = True

    else:
        if endS:
            finS += 1
        if cletras == 3:
            len_tres += 1
        if hay_dre:
            cDre += 1
        cletras = 0
        tiened = tienedr = hay_dre = False
        cpalabras += 1
        if i == ".":
            break


porj = round(len_tres * 100 / cpalabras)
print("Cantidad de palabras con tres letras: ", len_tres)
print("Porcentaje de palabras con tres letras: %", porj)
print("Cantidad de palabras que terminan con 's': ", finS)
print("Cantidad de palabras que tiene 'dre': ", cDre)
