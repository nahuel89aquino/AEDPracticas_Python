# Desarrollar un programa que permita crear un arreglo de n elementos, a partir del arreglo:
# 1- Generar un vector con todos aquellos numeros primos
# 2- Determinar el promedio del vector generado en el punto 1


from AEDPracticas_Python.EJERCICIOS_FICHA_12.Ejercicio_03 import funciones

def test():
    primos = list()
    print("Ejercicio nro 3 - Busqueda de primos")
    n = int(input("Elija el tamaño del arreglo: "))
    max = int(input("Eleija el maximo valor del arreglo: "))
    vector = funciones.crear(n, max)
    print(vector)
    for k in vector:
        if funciones.primo(k):
            primos.append(k)
    prom = funciones.promedio(vector)
    print("Vector de numeros primos: ")
    print(primos)
    print("Valor promedio de dicho vector: ", prom)
if __name__ == "__main__":
    test()
