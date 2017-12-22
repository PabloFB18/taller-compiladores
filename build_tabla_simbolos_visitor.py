# coding=utf-8
from string import lower

from tabla_simbolos.nodo_funcion import NodoFuncion
from tabla_simbolos.nodo_tabla_simbolos import NodoTablaSimbolos
from tabla_simbolos.nodo_variable import NodoVariable
from tabla_simbolos.tabla_simbolos import TablaSimbolos


class BuildTablaSimbolosVisitor(object):
    def __init__(self, archivo):
        # La tabla de simbolos.
        self.tabla_simbolos = TablaSimbolos()
        # Lista de las funciones.
        self.funciones = []
        # Nodo que se encuentra siendo modificado, se va cambiando cuando se crea otro.
        self.nodo = NodoTablaSimbolos()
        self.errors_tabla_simbolos = archivo

        fun_output = NodoFuncion('output', 'void')
        param = NodoVariable('x', 'int', False)
        fun_output.parametros.append(param)
        self.funciones.append(fun_output)
        fun_input = NodoFuncion('input', 'int')
        self.funciones.append(fun_input)

    def visit_program(self, program):
        # Crear el nodo raiz y agregarlo.
        self.nodo = NodoTablaSimbolos()
        self.tabla_simbolos.root = self.nodo
        # Expanir el arbol para seguir el analisis.
        for declaration in program.declarations_p:
            declaration.accept(self)
        # Asociar a nodo AST.
        program.simbolos = self.nodo

    def visit_var_declaration(self, var_declaration):
        # Revisar si ya esta declarada la variable.
        error_var = self.nodo.check_repetido(var_declaration.id_t)
        if error_var is None:
            # Añadir la declaracion al nodo de la tabla de simbolos.
            self.nodo.new_entry(var_declaration.id_t, lower(var_declaration.type_specifier_t), var_declaration
                                .numero_si_no)
            var_declaration.variable = NodoVariable(var_declaration.id_t, lower(var_declaration.type_specifier_t),
                                                    var_declaration.numero_si_no)
        else:
            # Indicar el error.
            self.errors_tabla_simbolos.write('error en declaracion de variable: ' + error_var + '\n')

    def visit_fun_declaration(self, fun_declaration):
        # Revisar si ya esta declarada la funcion.
        error_fun = None
        for funcion in self.funciones:
            if funcion.nombre == fun_declaration.id_t and funcion.tipo == lower(fun_declaration.type_specifier_t):
                error_fun = funcion
                break
        # Crear la nueva funcion
        fun = NodoFuncion(fun_declaration.id_t, lower(fun_declaration.type_specifier_t))
        # Crear nuevo nodo de la tabla de simbolos.
        new_nodo = NodoTablaSimbolos()
        # Agregar el nuevo nodo al nodo padre.
        self.nodo.hijos.append(new_nodo)
        # Guardar el nodo padre por si hay mas declaraciones de variables despues de la funcion.
        nodo_padre = self.nodo
        # cambiar el nodo sobre el cual se esta trabajando.
        self.nodo = new_nodo
        # Yo soy tu padre
        self.nodo.padre = nodo_padre
        # Se agrega la funcion a la lista de funciones.
        self.funciones.append(fun)
        # Visitar los nodos que contienen los parametros.
        if fun_declaration.params_p is not None:
            for param in fun_declaration.params_p:
                param.accept(self)
        if error_fun is not None:
            for funcion_iteracion in self.funciones:
                if funcion_iteracion != fun:
                    if len(funcion_iteracion.parametros) == len(fun.parametros):
                        if len(funcion_iteracion.parametros) == 0:
                            self.errors_tabla_simbolos.write('Ya esta definida la funcion: ' + error_fun.nombre + '\n')
                            break
                        mismos_tipos = True
                        for i in range(0, len(fun.parametros)):
                            if funcion_iteracion.parametros[i].tipo != fun.parametros[i].tipo:
                                mismos_tipos = False
                                break
                        if mismos_tipos:
                            self.errors_tabla_simbolos.write('Ya esta definida la funcion: ' + error_fun.nombre + '\n')
                            break
        # Visitar el contenido de la funcion.
        if fun_declaration.compound_stmt_p.local_declarations_p is not None or fun_declaration.compound_stmt_p\
                .stmt_list_p is not None:
            fun_declaration.compound_stmt_p.accept(self)
        # Asociar a nodo AST.
        fun_declaration.simbolos = self.nodo
        # Asociar lista funciones a nodo AST.
        fun_declaration.funcion = fun
        # Volver al nodo padre.
        self.nodo = nodo_padre

    def visit_param(self, param):
        error_param = self.nodo.check_repetido(param.id_t)
        if error_param is None:
            self.nodo.new_entry(param.id_t, lower(param.type_specifier_t), param.arreglo_si_no)
            param.variable = NodoVariable(param.id_t, lower(param.type_specifier_t), param.arreglo_si_no)
            self.funciones[len(self.funciones)-1].parametros.append(NodoVariable(param.id_t, lower(
                param.type_specifier_t), param.arreglo_si_no))
        else:
            self.errors_tabla_simbolos.write('error en parametro: ' + error_param + '\n')

    def visit_compound_stmt(self, compound_stmt):
        # Crear nuevo nodo de la tabla de simbolos.
        new_nodo = NodoTablaSimbolos()
        # Agregar el nuevo nodo al nodo padre.
        self.nodo.hijos.append(new_nodo)
        # Guardar el nodo padre por si hay mas declaraciones de variables despues de la funcion.
        nodo_padre = self.nodo
        # cambiar el nodo sobre el cual se esta trabajando.
        self.nodo = new_nodo
        # Yo soy tu padre
        self.nodo.padre = nodo_padre
        # Visitar los nodos que contienen los parametros.
        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    local_declaration.accept(self)
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    stmt.accept(self)
        # Asociar a nodo AST.
        compound_stmt.simbolos = self.nodo
        # Volver al nodo padre.
        self.nodo = nodo_padre

    def visit_selection_stmt(self, selection_stmt):
        # Crear nuevo nodo de la tabla de simbolos.
        new_nodo = NodoTablaSimbolos()
        # Agregar el nuevo nodo al nodo padre.
        self.nodo.hijos.append(new_nodo)
        # Guardar el nodo padre por si hay mas declaraciones de variables despues de la funcion.
        nodo_padre = self.nodo
        # cambiar el nodo sobre el cual se esta trabajando.
        self.nodo = new_nodo
        # Yo soy tu padre
        self.nodo.padre = nodo_padre
        # Visitar los nodos.
        if not selection_stmt.else_si_no:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
        else:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
            if selection_stmt.stmt2_p is not None:
                # Crear nuevo nodo de la tabla de simbolos.
                new_nodo = NodoTablaSimbolos()
                # Agregar el nuevo nodo al nodo padre.
                self.nodo.hijos.append(new_nodo)
                # Guardar el nodo padre por si hay mas declaraciones de variables despues de la funcion.
                nodo_padre = self.nodo
                # cambiar el nodo sobre el cual se esta trabajando.
                self.nodo = new_nodo
                # Yo soy tu padre
                self.nodo.padre = nodo_padre
                # Visitar los nodos.
                selection_stmt.stmt2_p.accept(self)
                # Asociar a nodo AST.
                selection_stmt.simbolos = self.nodo
                # Volver al nodo padre.
                self.nodo = nodo_padre
        # Asociar a nodo AST.
        selection_stmt.simbolos = self.nodo
        # Volver al nodo padre.
        self.nodo = nodo_padre

    def visit_iteration_stmt(self, iteration_stmt):
        # Crear nuevo nodo de la tabla de simbolos.
        new_nodo = NodoTablaSimbolos()
        # Agregar el nuevo nodo al nodo padre.
        self.nodo.hijos.append(new_nodo)
        # Guardar el nodo padre por si hay mas declaraciones de variables despues de la funcion.
        nodo_padre = self.nodo
        # cambiar el nodo sobre el cual se esta trabajando.
        self.nodo = new_nodo
        # Yo soy tu padre
        self.nodo.padre = nodo_padre
        # Visitar los nodos.
        iteration_stmt.expression_p.accept(self)
        if iteration_stmt.stmt_p is not None:
            iteration_stmt.stmt_p.accept(self)
        # Asociar a nodo AST.
        iteration_stmt.simbolos = self.nodo
        # Volver al nodo padre.
        self.nodo = nodo_padre

    def visit_return_stmt(self, return_stmt):
        if return_stmt.expression_si_no:
            if lower(self.funciones[len(self.funciones) - 1].tipo) == 'void':
                self.errors_tabla_simbolos.write('Error funcion ' + self.funciones[len(self.funciones)-1].nombre +
                                                 ' declarada void no debe retornar un valor\n')
            return_stmt.expression_p.accept(self)
        else:
            if lower(self.funciones[len(self.funciones)-1].tipo) == 'int':
                self.errors_tabla_simbolos.write('Error funcion ' + self.funciones[len(self.funciones)-1].nombre +
                                                 ' declarada int debe retornar un valor\n')

    def visit_expression(self, expression):
        expression.var_p.accept(self)
        expression.expression_p.accept(self)

    def visit_var(self, var):
        var_def = self.nodo.check_declarado(var.id_t)
        if var_def is None:
            self.errors_tabla_simbolos.write('Error variable ' + var.id_t + ' no declarada\n')
        if var.expression_si_no:
            var.expression_p.accept(self)
        var.variable = var_def

    def visit_simple_expression(self, simple_expresion):
        simple_expresion.additive_expression1_p.accept(self)
        simple_expresion.additive_expression2_p.accept(self)

    def visit_additive_expression(self, additive_expresion):
        additive_expresion.additive_expression_p.accept(self)
        additive_expresion.term_p.accept(self)

    def visit_term(self, term):
        term.term_p.accept(self)
        if term.factor_p is not None:
            term.factor_p.accept(self)

    def visit_num(self, num):
        pass

    def visit_call(self, call):
        if call.args_p is not None:
            for arg in call.args_p:
                arg.accept(self)
        existe_funcion = False
        for funcion_iteracion in self.funciones:
            if call.id_t == funcion_iteracion.nombre:
                if call.args_p is not None and len(funcion_iteracion.parametros) != 0:
                    if len(funcion_iteracion.parametros) == len(call.args_p):

                        error = False
                        indice = 0
                        for arg in call.args_p:
                            if arg.variable.tipo != funcion_iteracion.parametros[indice].tipo:
                                error = True
                            indice = indice + 1
                        if not error:
                            call.funcion = funcion_iteracion
                            existe_funcion = True
                            break

                else:
                    if len(funcion_iteracion.parametros) == 0 and call.args_p is None:
                        call.funcion = funcion_iteracion
                        existe_funcion = True
                        break
            else:
                existe_funcion = False
        if not existe_funcion:
            self.errors_tabla_simbolos.write('Llamada a funcion que no existe ' + call.id_t + '\n')
