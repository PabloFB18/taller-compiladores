
import nodo_variable


class NodoTablaSimbolos:
    def __init__(self):
        self.declaraciones = []
        self.hijos = []
        self.padre = None

    def check_repetido(self, nombre):
        for declaracion in self.declaraciones:
            if declaracion.nombre == nombre:
                return declaracion
        return None

    def check_declarado(self, nombre):
        if self.padre is None:
            return None
        if self.check_repetido(nombre) is None:
            return self.padre.check_declarado(nombre)
        return self.check_repetido(nombre)

    def new_entry(self, nombre, tipo, arreglo_si_no):
        declaracion = nodo_variable.NodoVariable(nombre, tipo, arreglo_si_no)
        self.declaraciones.append(declaracion)

    def to_string(self):
        str_declaraciones = ''
        for declaracion in self.declaraciones:
            str_declaraciones = str_declaraciones + '\t' + declaracion.to_string() + '\n'
        str_nodo = 'Nodo: Declaraciones:\n' + str_declaraciones + '\n'
        for hijo in self.hijos:
            str_nodo = str_nodo + hijo.to_string()
        return str_nodo

