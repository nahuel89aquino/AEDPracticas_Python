class Mudanzas():
    def __init__(self, ident, dest, cod_vehiculo, tarifa, tipo):
        self.ident = ident
        self.destino = dest
        self.codigo = cod_vehiculo
        self.tarifa = tarifa
        self.tipo = tipo


def display(reg):
    print("Numero de identificacion: ", reg.ident)
    print("Direccion de destino: ", reg.destino)
    print("Codigo de vehiculo: ", reg.codigo)
    print("Tarifa de traslado: $", reg.tarifa)
    print("Tipo de carga que se transporta: ", reg.tipo)


def validar_inter(msj, inf=0, sup=0):
    valor = int(input(msj))
    while valor not in range(inf, sup):
        print("Error. El valor solicitado debe se entre {} y {}".format(str(inf), str(sup)))
        valor = int(input(msj))
    return valor


