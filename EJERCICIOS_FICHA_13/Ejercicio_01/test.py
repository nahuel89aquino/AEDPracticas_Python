# Se pide un programa que cargue n elementos numericos aleatorios entre 1 y 100 inclusive (pueden existir
# duplicados). A partir de ese arrglo:
# 1- Ordenarlo de forma ascendente y mostrarlo
# 2- Buscar un elemento x dentro del arreglo(x se ingresa por teclado).Si no existe, informarlo. Si existe,
# determinar cuantos valores impares mayores a x encontron en el arreglo.


from AEDPracticas_Python.EJERCICIOS_FICHA_13.Ejercicio_01 import funciones


def test():
    print("Ejercicio 1 Ficha 13 - Ordenar y buscar")
    n = int(input("Ingrese el tamaño del vector a generar: "))
    vector = funciones.crear(n, min=1)
    print(vector)
    funciones.selector_sort(vector)
    print(vector)
    print("Introduzca un numero a buscar en el vector: ")
    x = int(input())
    if funciones.binary_search(vector, x):
        v_imp = funciones.impar_may_x(vector, x)
        print("Los numeros mayores a x son: ")
        print(v_imp)
    else:
        print("No se encuentra elemento")


if __name__ == '__main__':
    test()
