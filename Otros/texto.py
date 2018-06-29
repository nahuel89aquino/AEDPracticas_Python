#cantidad de palabras que man en la primera mitad.
#
texto = "hoy es un buen dia para comer un asado es amen amense meenootira"
texto += "."
print(texto)
tiene_m = tiene_me = hay_men = False
cletra = cpalab = cmen = 0

for i in texto:
    if i.isalpha():
        cletra += 1
        if not tiene_m and i == "m":
            tiene_m = True
        else:
            if tiene_m and i == "e":
                tiene_me = True
                tiene_m = False
            else:
                if tiene_me and i == "n":
                    hay_men = True
                    pos_n = cletra
                tiene_m = False
                tiene_me = False

    else:
        cpalab += 1
        mitad = cletra // 2
        if hay_men:
            if pos_n <= mitad:
                cmen += 1
        hay_men = tiene_me = tiene_m = False
        cletra = 0
print("cantidad de palabras que tiene 'men' en la primera mitad de la palabra: ", cmen)
