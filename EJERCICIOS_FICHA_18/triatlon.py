import random

class Atleta:
    def __init__(self, nom, t_nat, t_cicl, t_run):
        self.nombre = nom
        self.tiempo_natacion = t_nat
        self.tiempo_ciclismo = t_cicl
        self.tiempo_corriendo = t_run


def write(v):
    for i in range(len(v)):
        print("nombre del atleta: ",v[i].nombre)
        print("tiempo de natacion: ", v[i].tiempo_natacion)
        print("tiempo de ciclismo: ", v[i].tiempo_ciclismo)
        print("tiempo de corriendo: ", v[i].tiempo_corriendo)


def promedio(competidor):
    t1 = competidor.tiempo_natacion
    t2 = competidor.tiempo_ciclismo
    t3 = competidor.tiempo_corriendo

    return round((t1 + t2 + t3) / 3, 2)


def selection_sort(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(1, n):
            if v[i].promedio > v[j].promedio:
                v[i], v[j] = v[j], v[i]


v = [None] * 3
for i in range(3):
    nombre = input("ingrese nombre: ")
    t1 = random.randint(0, 150)
    t2 = random.randint(0, 150)
    t3 = random.randint(0, 150)
    v[i] = Atleta(nombre, t1, t2, t3)

for i in range(len(v)):
    prom = promedio(v[i])
    v[i].promedio = prom
    print("El promedio de tiempo del competidor {} es de : {}".format(i + 1, prom))

selection_sort(v)
print('Primer puesto:', v[0].nombre)
print('Segundo puesto:', v[1].nombre)
print('Tercer puesto:', v[2].nombre)
