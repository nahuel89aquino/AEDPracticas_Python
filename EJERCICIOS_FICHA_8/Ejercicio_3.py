#a) cantidad de palabras que comienzan y terminan con vocal
#b) cantidad de palabras que comienzan con la misma letra
#que termino la palabra anterior
#c) el porcentaje

vocal = "aeiou"
texto = "hoy yes una lindo dia para comer un asado maddres.re"
texto += "."

fue_prLetra = end_vocal = ft_vocal= ft_ant = end_letra = False
anterior = ""
print(texto)
cft_end = cpal = cft_ant = 0
for i in texto:
    if i.isalpha():
        if end_letra:
            if ft_char == anterior:
                ft_ant = True
        end_letra = False
        if not fue_prLetra:
            ft_char = i
            ft_vocal = i in vocal
            fue_prLetra = True


        end_vocal = i in vocal
        end_char = i
        end_letra = True

    else:
        cpal += 1
        if cpal > 1:
            print(anterior,ft_char)
            if ft_ant:
                cft_ant =+ 1

        #print(ft_letra in vocal)
        if ft_vocal and end_vocal:
            cft_end += 1
        anterior = end_char
        fue_prLetra = end_vocal = ft_vocal = ft_ant = False


print("Cantidad de palabras que empiezan y terminan con vocal", cft_end)
print("Cantidad de palabras que comienzan con la ultima letra de la palabra anterios: ", cft_ant)
