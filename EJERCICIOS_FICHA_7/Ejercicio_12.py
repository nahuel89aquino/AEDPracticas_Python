#Se debe establecer cuantas palabras de la frase estan antecedidas por otra palabra de menor o igual
#longitud( la primer palabra de la frase nunca podra ser contabilizada ya que no posee palabra
#antecesora)
texto = "hoy es un lindo dia para comer un asado"
texto += "."
print(texto)
primera_p = False
cletras = letras_men = 0
for i in texto:
    #contador de letras
    if i.isalpha():
        cletras += 1

    else:
        if primera_p:
            if cletras >= len_anterior:
                letras_men += 1
                print(letras_men, end=" ")

        else:
            primera_p = True
        len_anterior = cletras

        cletras = 0

print("\nLa cantidad de palabra que son antecedidas por otra palabra menor o igual: ", letras_men)
