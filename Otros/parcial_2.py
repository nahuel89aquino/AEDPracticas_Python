
texto = "La vida en esta vivienda es inviable."
texto += "."

vocales = "aeiou"
cletra = cpal = cS = cvi = cns =cv_cons = cvocal = 0
tiene_s = endS = hay_n = hay_e = hay_3_vocal = ft_cons = tiene_v =tiene_vi = False
print(texto)

def promedio(suma, total):
    if total != 0:
        media = round(suma / total, 2)
    else:
        media = -1

    return media
def vocal(x):
    return x in vocales
def consonante(x):

    return x not in vocales

for c in texto:
    if c != " " and c != ".":
        cletra += 1
        endS = False
        if not tiene_v and c == "v":
            tiene_v = True
            print(tiene_v)
        else:
            if tiene_v and c == "i":
                tiene_vi = True
            else:
                tiene_v = False


        if not ft_cons:
            hay_cons = consonante(c)
            ft_cons = True
        if vocal(c):
            cvocal += 1

            if cvocal == 3:
                hay_3_vocal = True
        if c == "n" and cletra == 3:
            hay_n = True
        if c == "e":
            hay_e = True
        if c == "s":
            endS = True
    else:
        cpal += 1
        #print(tiene_vi)
        if tiene_vi and cletra > 4:
            cvi += 1
        if hay_3_vocal and hay_cons:
            cv_cons += 1
        if hay_n and hay_e:
            cns += 1
        if endS and cletra % 2 != 0:
            cS += 1
        cletra = cvocal = 0
        endS = hay_e = hay_n = ft_cons = hay_3_vocal = hay_cons = tiene_vi = tiene_v = False
prom = promedio(cpal, cns)
if prom == -1:
    prom = "Error: division por cero"

print("Cantidad de palabras que terminan en 's' y tienen numero impar de letras: ", cS)
print("Cantidad promedio de palabre que tiene 'n' en la tercera letra y 'e' :", prom)
print("Cantidad de palabras que tiene tres vocales y empiezan con consonante: ", cv_cons)
print("Cantidad de palabras que tiene 'vi' y cantidad de letras mayor a 4: ", cvi)
