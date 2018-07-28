# Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado
# en un punto. En base al texto ingresado, determinar:
# a) Cual es la longitud de la palabra mas larga.
# b) Cuantas palabras tienen la 'a' como unica vocal
# c) Que porcentaje representan las que solo tienen la vocal 'a' sobre el total de palabras


def porcentaje(valor, total):
    porc = round(valor * 100 / total, 2)
    return porc


def vocales(n):
    return n in "aeiou"


def test():
    texto = "el agua clara salta por las piedras."
    mayor = None
    cletras = cpal = pal_solo_a = 0
    primera = vocal_not_a = False
    for i in texto:
        if not i == " " and not i == ".":
            cletras += 1
            if vocales(i):
                if i != "a":
                    vocal_not_a = True
        else:
            cpal += 1
            if not primera:
                mayor = cletras
                primera = True
            if cletras >= mayor:
                mayor = cletras
            if not vocal_not_a:
                pal_solo_a += 1
            cletras = 0
            vocal_not_a = False
    por100 = porcentaje(pal_solo_a, cpal)
    print("La longitud de la palabra mas larga es de ", mayor)
    print("Cantidad de palabras que tienen solo la 'a' como vocal: ", pal_solo_a)
    print("Porcentaje representado por las palabras que solo tiene 'a' sobre el total de palabras: ", por100, "%")


test()
