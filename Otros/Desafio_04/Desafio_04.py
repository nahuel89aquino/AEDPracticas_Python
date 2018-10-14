import pickle
import os.path
import math

class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def imprimir_punto(v):
    n = len(v)
    for i in range(n):
        print('Punto nro ' + str(i + 1) + ': ' + to_string(v[i]))


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))


def mayor_menor_distancia(v):
    n = len(v)
    mayor = 0
    menor = float(distance_between(v[0], v[1]))
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            dis = float(distance_between(v[i], v[j]))
            if dis < menor:
                menor = dis
            elif dis > mayor:
                mayor = dis
    return round(mayor), round(menor)


def test():
    k = 0
    v = [0] * 5000
    fd = "puntos.df4"
    m = open(fd, "rb")

    t = os.path.getsize(fd)
    print(t)
    while m.tell() < t:
        v[k] = pickle.load(m)
        k += 1
    m.close()
    imprimir_punto(v)
    dis_mayor, dis_menor = mayor_menor_distancia(v)
    print('La menor distancia es de : ', str(dis_menor))
    print('La mayor distancia es de : ', str(dis_mayor))


if __name__ == '__main__':
    test()
