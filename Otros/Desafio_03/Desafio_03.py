# Desafio nro 3


from AEDPracticas_Python.Otros.Desafio_03 import Soporte


def posicion(num, x):
    for k in range(len(num)):
        if x == num[k]:
            return k

    return -1


def modal(num, cont):
    pass


def contar(v, num, cont):
    ft = False
    for i in v:
        if not ft:
            num.append(i)
            cont.append(1)
            ft = True
            continue
        pos = posicion(num, i)
        if pos == -1:
            num.append(i)
            cont.append(1)
        else:
            cont[pos] += 1
    modal(num, cont)

def test():
    v = Soporte.vector_unknown_range(300000)
    num = []
    cont = []
    c = 0

    contar(v, num, cont)
    for i in v:
        if i == 525:
            c += 1

    print(num)
    print(cont)
    print(c)
    print(len(num))
    print(len(cont))


if __name__ == '__main__':
    test()
