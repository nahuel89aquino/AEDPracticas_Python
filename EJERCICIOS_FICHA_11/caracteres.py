def vocal(x):
    return x in "aeiou"


def consonante(x):
    return x not in "aeiou"


def mayusculas(x):
    return 'A' <= x <= 'Z'


def minusculas(x):
    return 'a' <= x <= 'z'


def numero(x):
    return '0' <= x <= '9'
