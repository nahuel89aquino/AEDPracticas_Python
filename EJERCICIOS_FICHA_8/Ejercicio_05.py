#1) Cantidad de palabras que comienzan con consonantes y terminan en vocales
#2) Cantidad  de palabras que poseen la secuencia 'li'a partir de la 
#tercera letra de la palabra
#3) Cantidad de palabras con menos de cuatro letras y porcentaje que dicha
#cantidad representa sobre el total del texto

texto = "hoy es un buen dia para comer una casado"
texto += "."

ft_cons = ft_letra= False
cpal = cCV = 0
def consonante(x):
    return x not in ("aeiou")
def vocal(x):
    return x in ("aeiou")

print(texto)
for i in texto:
    if i != " " and i != ".":
        last_char = False
        if not ft_letra:
            ft_cons = consonante(i)
            ft_letra = True
        
        end_vocal = vocal(i)
        
    else:
        cpal += 1
        if ft_cons and end_vocal:
            cCV += 1
        ft_letra = end_vocal = False

print("cantidad de palabras que empiezan en consonante y termina en vocal: ", cCV)
            
