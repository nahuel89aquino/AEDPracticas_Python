#a) cantidad de vocales en la frase
#b) cuantas letras en total existen en la frase
#c) porcentaje de vocales respecto al total de letras

texto = "hoy es un lindo dia para comer un asado"
texto += "."

cvocal = cletras = 0

print(texto)

for i in texto:
    if i.isalpha():
        if i in ("a", "e", "i", "o", "u"):
            cvocal += 1
        cletras += 1
porc = round(cvocal * 100 / cletras, 2)
print("Cantidad de vocales: ", cvocal)
print("Cantidad de letras en la frase: ", cletras)
print("promedio de vocales en la frase: %", porc)
