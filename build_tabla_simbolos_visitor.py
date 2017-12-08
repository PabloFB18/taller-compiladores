from tabla_simbolos.nodo_funcion import NodoFuncion
from tabla_simbolos.nodo_tabla_simbolos import NodoTablaSimbolos
from tabla_simbolos.tabla_simbolos import TablaSimbolos


class BuildTablaSimbolosVisitor(object):
    def __init__(self):
        # La tabla de simbolos.
        self.tabla_simbolos = TablaSimbolos()
        # Lista de las funciones.
        self.funciones = []
        # Nodo que se encuentra siendo modificado, se va cambiando cuando se crea otro.
        self.nodo = None

    def visit_program(self, program):

        self.nodo = NodoTablaSimbolos()
        self.tabla_simbolos.root = self.nodo
        for declaration in program.declarations_p:
            declaration.accept(self)

    def visit_var_declaration(self, var_declaration):
        error_var = self.nodo.check_repetido(var_declaration.id_t, var_declaration.type_specifier_t)
        if error_var is None:
            self.nodo.new_entry(var_declaration.id_t, var_declaration.type_specifier_t)
        else:
            print 'error en declaracion de variable: ' + error_var

    def visit_fun_declaration(self, fun_declaration):
        error_fun = self.funciones.check_repetido(fun_declaration.id_t, fun_declaration.type_specifier_t)
        fun = NodoFuncion(fun_declaration.id_t, fun_declaration.type_specifier_t)
        # Crear nuevo nodo de la tabla de simbolos.
        new_nodo = NodoTablaSimbolos
        # Agregar el nuevo nodo al nodo padre.
        self.nodo.hijos.append(new_nodo)
        self.nodo = new_nodo
        for param in fun_declaration.params_p:
            param.accept(self)
        if error_fun is None:
            self.funciones.append(fun)
        fun_declaration.compound_stmt_p.accept(self)

    def visit_param(self, param):
        error_param = self.nodo.check_repetido(param.id_t, param.type_specifier_t)
        if error_param is None:
            self.nodo.new_entry(param.id_t, param.type_specifier_t)
        else:
            print 'error en parametro: ' + error_param

    def visit_compound_stmt(self, compound_stmt):
        pass

    def visit_selection_stmt(self, selection_stmt):
        pass

    def visit_iteration_stmt(self, iteration_stmt):
        pass

    def visit_return_stmt(self, return_stmt):
        pass

    def visit_expression(self, expression):
        pass

    def visit_var(self, var):
        pass

    def visit_simple_expression(self, simple_expresion):
        pass

    def visit_additive_expression(self, additive_expresion):
        pass

    def visit_term(self, term):
        pass

    def visit_num(self, num):
        pass

    def visit_call(self, call):
        pass
