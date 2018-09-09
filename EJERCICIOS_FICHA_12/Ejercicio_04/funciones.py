import random
import math


def vector_mayor(c1, c2):
    may = []
    for i in range(len(c1)):
        if c1[i] > c2[2]:
            may.append(c1[i])
        else:
            may.append(c2[i])
    return may


def crear(tam, m):
    v = list()
    for i in range(tam):
        v.append(random.randint(0, m + 1))
    return v


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
