class Proyecto:
    def __init__(self, id, cliente, honorario, cod):
        self.nro_id = id
        self.cliente = cliente
        self.honorario = honorario
        self.codigo = cod


def validate(mensaje, menj_err, inf=0, sup=0):
    """Realiza una validacion del numero entero ingresado por consola
    :param mensaje: Recibe un mensaje de instruccion para el ususario
    :param: menj_err: Mensaje de error a mostrar en pantalla en caso de validacion igual a False
    :param inf: Establece la cota inferior de validacion
    :param sup: Establece la cota superior de validacion
    :return val: Valor entero validado
    """
    val = int(input(mensaje))
    if sup != 0:
        while val not in range(inf, sup + 1):
            print(menj_err)
            val = int(input(mensaje))
    else:
        while val < inf:
            print(menj_err)
            val = int(input(mensaje))
    return val


def menu():
    """Muestra un menu de opciones en pantalla"""

    print("1. Cargar areglo")
    print("2. Mostrar arreglo")
    print("3. Determinar el monto de honorarios")  # vector acum por tipo de constuccion
    print("4. Mostrar proyectos cuyo codigo sea diferente a 4")  # ordenar vector de menor a mayor
    print("5. Buscar cliente y devolver proyecto")
    print("6. Salir")


def load(i):
    """ Carga un registro con los valores ingresados por consola
    :param i: registo a cargar
    """
    nro_proyecto = i
    nombre = input('Ingrese nombre del cliente: ')
    monto = float(input('Ingrese los honorarios: '))
    cod = validate('Ingrese codigo: ', 'Error. codigo entre 0 y 14', inf=0, sup=14)
    return Proyecto(nro_proyecto, nombre, monto, cod)


def mostar(i):
    """ Realiza una impresion en pantalla del registro
    :param i:registro a imprimir
    """
    print("Numero de indentificacion: ", i.nro_id)
    print("Nombre del client: ", i.cliente)
    print("Monto de honorarios", i.honorario)
    print("Codigo: ", i.codigo)


def honorarios(v):
    """ Acumula totales de honorarios segun su tipo
    :param v: vector de registros
    :return acum: vector de acumuladores
    """
    n = len(v)
    acum = [0] * (n)
    for i in range(n):
        acum[v[i].codigo] += v[i].honorario
    return acum


def main():
    salir = False
    while not salir:
        menu()
        ops = validate('Ingrese una opcion: ', 'Error. valor entre 1 y 6', inf=1, sup=6)
        if ops == 1:
            mensaje = 'Ingrese la cantidad de proyectos: '
            menj_err = 'Error. Debe ingresar un numero entero positivo'
            n = validate(mensaje, menj_err, inf=0)
            vector = [None] * n
            for i in range(len(vector)):
                vector[i] = load(i + 1)
        if ops == 2:
            for i in vector:
                mostar(i)
        if ops == 3:
            vec_acum = honorarios(vector)
            for i in range(len(vec_acum)):
                print("codigo {} : ${} ".format(i, vec_acum[i]), end="--")
            print()


if __name__ == '__main__':
    main()
