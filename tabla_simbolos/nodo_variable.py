class NodoVariable:
    def __init__(self, nombre, tipo, arreglo_si_no):
        self.nombre = nombre
        self.tipo = tipo
        self.arreglo_si_no = arreglo_si_no

    def to_string(self):
        if self.arreglo_si_no:
            return 'Declaracion: Nombre: ' + self.nombre + '[] Tipo: ' + self.tipo
        else:
            return 'Declaracion: Nombre: ' + self.nombre + ' Tipo: ' + self.tipo
