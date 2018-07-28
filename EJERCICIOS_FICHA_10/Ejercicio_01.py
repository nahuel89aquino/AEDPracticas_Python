# a) Determinar cuantas palabras tienen al menos un caracter que era en realidad un digito
# (un caracter entre '0' y '9'
# b) Determinar cuantas palabras tiene 3 o menos letras, cuantas tiene 4 y hasta 6 letras, y cuantas tienen
# mas de 6 letras
# c) Determinar la longitud de la palabra mas larga del texto
# d) Determinar cuantas palabras contuvieron la expresion 'de', pero en la primera mitad de la palabra


def es_texto(k):
    valido = not (k == " ") and not (k == ".")
    return valido


def es_num(k):
    return "0" <= k <= "9"


def test():
    texto = "hoy es el dia 28 del mes de julio diariamente" \
        " nos levantamos temprano para ir a trabajar a las 8am despues vamos a la facultad."
    print(texto)
    cnum = cletra = cpal = entre_0a3 = entre_4a6 = mas_de6 = mayor = posic = cont_de = 0
    primera_pal = hay_num = hay_d = hay_de = False
    for i in texto:
        if es_texto(i):
            cletra += 1
            # punto 'a'
            if es_num(i):
                hay_num = True
            if not hay_d and i == "d":
                hay_d = True
            else:
                if hay_d and i == "e":
                    hay_de = True
                    posic = cletra
                else:
                    hay_d = False
        else:
            cpal += 1
            # punto 'a'
            if hay_num:
                cnum += 1
                hay_num = False
            # punto 'b'
            if cletra <= 3:
                entre_0a3 += 1
            elif cletra <= 6:
                entre_4a6 += 1
            else:
                mas_de6 += 1
            # punto 'c'
            if not primera_pal:
                mayor = cletra
                primera_pal = True
            if cletra >= mayor:
                mayor = cletra
            if hay_de and posic <= (cletra // 2):
                cont_de += 1
            hay_de = hay_d = False
            cletra = 0

    print("Cantidad de palabras tenian al menos un caracter: ", cnum)
    print("Cantidad de palabras que tienen 3 o menos letras: ", entre_0a3)
    print("Cantidad de palabras que tienen 4 a 6 letras: ", entre_4a6)
    print("Cantidad de palabras que tienen 6 o mas letras: ", mas_de6)
    print("La palabra mas larga del texto tiene ", mayor, " letras")
    print("Cantidad de palabras que contienen 'de' en la primera mitad: ", cont_de)


test()
