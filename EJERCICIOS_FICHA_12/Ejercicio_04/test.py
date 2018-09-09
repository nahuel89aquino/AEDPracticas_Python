# Cargar por teclado dos vectores del mismo tamaño n y, a partir de ellows, generar un tercer vector que contenga
# para cada componente, el mayor valor entre la componentes homologas (mismo indice) de los otros dos vectores


from AEDPracticas_Python.EJERCICIOS_FICHA_12.Ejercicio_04 import funciones

def test():
    print("Ejercicio 4 - Mayores con el mismo indice")
    n = int(input("Elija el tamaño de ambos vectores: "))
    tam = int(input("Elija el rango maximo de cada vector a generar"))
    v1 = funciones.crear(tam, n)
    v2 = funciones.crear(tam, n)
    print(v1)
    print(v2)
    mayor = funciones.vector_mayor(v1, v2)
    print("El vector conformado por los valores mayores de componentes homologas es:")
    print(mayor)
    pass


if __name__ == '__main__':
    test()
