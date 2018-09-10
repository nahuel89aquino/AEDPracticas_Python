import random
import math


def impar_may_x(v, x):
    imp = []
    for i in v:
        if i > x and i % 2 != 0:
            imp.append(i)
    return imp


def selector_sort(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[j], v[i] = v[i], v[j]

def crear(tam, min=0, max=100):
    v = list()
    for i in range(tam):
        v.append(random.randint(min, max))
    return v


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c] == x:
            return True
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return False


def primo(valor):
    es_primo = True
    if valor % 2 == 0:
        es_primo = False
    else:
        tope = math.ceil(math.sqrt(valor))
        for i in range(3, tope):
            if valor % i == 0:
                es_primo = False
                break
    return es_primo


def promedio(v):
    suma = 0
    for i in range(len(v)):
        suma += v[i]
    return round(suma / len(v), 2)



