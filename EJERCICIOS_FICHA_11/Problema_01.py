# a) Determinar la cantidad de palabras que comienzan con la expresion 'SI' (ok)
# b) Determinar la cantidad de palabras que terminan con vocal y tiene una cantidad impares de consonantes (ok)
# c) Determinar la cantidad de palabras que tienen solo una vocal (ok)
# d) Determinar la cantidad de palabras que comienzan y terminan con la misma letra(ok)
# e) Determinar la cantidad de palabras que contienen la expresion 'CC'
# f) Determinar el porcentaje que representa las palabras del punto b sobre el total de palabras
# g) Determinal la longitud de la palabra mas corta
# h) Determinar el promedio de letras por palabras

from EJERCICIOS_FICHA_11 import caracteres


def test():
    texto = "SI sistema Sillon ahsSIa es solos"
    texto += "."
    cletras = cpal = cSI = orden = j = cons = cont1 = cv = cont2 = cont3 = 0
    hayS = haySI = vocalF = pletra = False
    for i in texto:
        if not i == " " and not i == ".":
            vocalF = False
            if not pletra:
                inicia = i
                pletra = True
            final = i
            if caracteres.vocal(i.lower()):
                cv += 1
                vocalF = True
            if caracteres.consonante(i.lower()):
                cons += 1
            if not hayS and i == "S":
                orden = j
                hayS = True
            else:
                if hayS and i == "I":
                    haySI = True
                else:
                    hayS = False
            cletras += 1
            j += 1
        else:
            cpal += 1
            if inicia == final:
                cont3 += 1
            if cv == 1:
                cont2 += 1
            if vocalF and (cons % 2) != 0:
                cont1 += 1
            if haySI and orden == 0:
                cSI += 1
            haySI = hayS = vocalF = pletra = False
            cletras = orden = cons = cv = 0

    print("Cantidad de palabras que comienzan con la expresion 'SI': ", cSI)
    print("Cantidad de palabras que terminan con vocal y tiene numero impar de consonates: ", cont1)
    print("Cantidad de palabras que tienen solo una vocal: ", cont2)
    print("Cantidad de palabras que empiezan y terminan con la misma letra: ", cont3)


test()
