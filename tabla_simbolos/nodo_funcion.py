

class NodoFuncion:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.parametros = []
        # self.simbolos_parametros = NodoTablaSimbolos()
        # self.simbolos_contenido = NodoTablaSimbolos()

    def to_string(self):
        str_param = ''
        for parametro in self.parametros:
            str_param = str_param + '\t' + parametro.to_string() + '\n'
        return 'Funcion: Nombre: ' + self.nombre + ' Tipo: ' + self.tipo + '\n\tParametros:\n' + str_param

