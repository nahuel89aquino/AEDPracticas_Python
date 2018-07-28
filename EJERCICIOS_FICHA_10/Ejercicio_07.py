# a) Determinar la cantidad de palabras que tuvieron exactamente 3 vocales
# b) Determinar el porcentaje de palbras que tuvieron algun digito ('0' al '9')  y mas de 4 letras
# c) Determinar el orden de la menor palabra que termina con la primera letra del texto
# d) Determinar la cantidad de palabras que contienen 'men' en la primera mitad de la palabra


def porcentaje(valor, total):
    porc = round(valor * 100 / total, 2)
    return porc


def vocal(k):
    return k in "aeiou"


def test():
    texto = "solos casa tres amigos caracteristica a los permita 12lalalssd 12asd mentirosos menospresiado"
    texto += "."
    menor = ultima = posicion_n = None
    hay_dig = primera = hay_m = hay_me = hay_men = False
    ft_letra = texto[0]
    cletras = cpal = cvocal = cant_palabras_3vocales = cont_alnum = orden = cont_men = 0

    for i in texto:
        if i.isalnum():
            cletras += 1
            if vocal(i):
                cvocal += 1
            if "0" <= i <= "9":
                hay_dig = True
            ultima = i
            if not hay_m and i == "m":
                hay_m = True
            else:
                if hay_m and i == "e":
                    hay_me = True
                    hay_m = False
                else:
                    if hay_me and i == "n":
                        hay_men = True
                        posicion_n = cletras
                    else:
                        hay_m = hay_me = False
        else:
            cpal += 1
            if hay_men and posicion_n < (cletras // 2):
                cont_men += 1
            if ultima == ft_letra:
                if not primera:
                    menor = cletras
                    orden = cpal
                    primera = True
                if cletras < menor:
                    menor = cletras
                    orden = cpal

            if cvocal == 3:
                cant_palabras_3vocales += 1
            if hay_dig and cletras > 4:
                cont_alnum += 1
            cletras = cvocal = 0
            hay_dig = False
    por100 = porcentaje(cont_alnum, cpal)
    print("Cantidad de palabras con exactamente 3 vocales: ", cant_palabras_3vocales)
    print("Porncentaje de palabras que tuvieron algun digito y mas de 4 letras: ", por100, "%")
    print("Orden le la menor palabra que termina con la primera letra del texto: ", orden)
    print("Cantidad de palabras que contienen 'men' en la primera mitad de la palabra: ", cont_men)


test()
