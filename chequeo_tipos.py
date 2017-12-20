# coding=utf-8
from string import lower


class ChequeoTipos(object):
    def __init__(self):
        self.errors_chequeo_tipos = open('errors_chequeo_tipos.txt', 'w')
        self.inicializadas = []

    def visit_program(self, program):
        for declaration in program.declarations_p:
            declaration.accept(self)

    def visit_var_declaration(self, var_declaration):
        var_declaration.tipo = var_declaration.variable.tipo

    def visit_fun_declaration(self, fun_declaration):
        if fun_declaration.compound_stmt_p.local_declarations_p is not None or \
                        fun_declaration.compound_stmt_p.stmt_list_p is not None:
            fun_declaration.compound_stmt_p.accept(self)
        fun_declaration.tipo = fun_declaration.funcion.tipo
        if fun_declaration.params_p is not None:
            for param in fun_declaration.params_p:
                param.accept(self)
                if param.tipo == 'ERROR':
                    fun_declaration.tipo = param.tipo

    def visit_param(self, param):
        param.tipo = param.variable.tipo
        self.inicializadas.append(param.id_t)

    def visit_compound_stmt(self, compound_stmt):
        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    local_declaration.accept(self)
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    stmt.accept(self)

    def visit_selection_stmt(self, selection_stmt):
        if not selection_stmt.else_si_no:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.expression_p.tipo != 'int':
                self.errors_chequeo_tipos.write('La condición de la selección debe ser de tipo entero.\n')
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
        else:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.expression_p.tipo != 'int':
                self.errors_chequeo_tipos.write('La condición de la selección debe ser de tipo entero.\n')
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
            if selection_stmt.stmt2_p is not None:
                selection_stmt.stmt2_p.accept(self)

    def visit_iteration_stmt(self, iteration_stmt):
        iteration_stmt.expression_p.accept(self)
        if iteration_stmt.expression_p.tipo != 'int':
            self.errors_chequeo_tipos.write('La condición del while debe ser de tipo entero.\n')
        if iteration_stmt.stmt_p is not None:
            iteration_stmt.stmt_p.accept(self)

    def visit_return_stmt(self, return_stmt):
        if return_stmt.expression_si_no:
            return_stmt.expression_p.accept(self)
            return_stmt.tipo = return_stmt.expression_p.tipo

    def visit_expression(self, expression):
        expression.var_p.accept(self)
        expression.expression_p.accept(self)
        if expression.var_p.tipo == expression.expression_p.tipo:
            expression.tipo = expression.var_p.tipo
        else:
            self.errors_chequeo_tipos.write('La expresión debe ser del mismo tipo que la variable declarada.\n')
            expression.tipo = 'ERROR'
        self.inicializadas.append(expression.var_p.id_t)

    def visit_var(self, var):
        if var.expression_si_no:  # Si es llamado un valor del arreglo
            var.expression_p.accept(self)
            if var.expression_p.tipo != 'int':
                self.errors_chequeo_tipos.write('El índice del arreglo ' + var.id_t + ' debe ser de tipo entero.\n')
                var.tipo = 'ERROR'
            else:
                if var.variable is not None:
                    var.tipo = var.variable.tipo
                else:
                    var.tipo = 'ERROR'
        else:
            inicializada_si_no = False
            for inicializada in self.inicializadas:
                if var.id_t == inicializada:
                    inicializada_si_no = True
                    break
            if not inicializada_si_no:
                self.errors_chequeo_tipos.write('La variable ' + var.id_t + ' no está inicializada.\n')
                var.tipo = 'ERROR'
            else:
                if var.variable is not None:
                    var.tipo = var.variable.tipo
                else:
                    var.tipo = 'ERROR'

    def visit_simple_expression(self, simple_expresion):
        simple_expresion.additive_expression1_p.accept(self)
        if simple_expresion.additive_expression1_p.tipo != 'int':
            self.errors_chequeo_tipos.write('El lado izquierdo de la comparación debe ser de tipo entero.\n')
            simple_expresion.tipo = 'ERROR'
        simple_expresion.additive_expression2_p.accept(self)
        if simple_expresion.additive_expression2_p.tipo != 'int':
            self.errors_chequeo_tipos.write('El lado derecho de la comparación debe ser de tipo entero.\n')
            simple_expresion.tipo = 'ERROR'
        if simple_expresion.additive_expression1_p.tipo == 'int' and simple_expresion.additive_expression2_p.tipo == \
                'int':
            simple_expresion.tipo = 'int'

    def visit_additive_expression(self, additive_expresion):
        additive_expresion.additive_expression_p.accept(self)
        if additive_expresion.additive_expression_p.tipo != 'int':
            self.errors_chequeo_tipos.write('El lado izquierdo de la expresión aditiva debe ser de tipo entero.\n')
            additive_expresion.tipo = 'ERROR'
        additive_expresion.term_p.accept(self)
        if additive_expresion.term_p.tipo != 'int':
            self.errors_chequeo_tipos.write('El lado derecho de la expresión aditiva debe ser de tipo entero.\n')
            additive_expresion.tipo = 'ERROR'
        if additive_expresion.additive_expression_p.tipo == 'int' and additive_expresion.term_p.tipo == 'int':
            additive_expresion.tipo = 'int'

    def visit_term(self, term):
        term.term_p.accept(self)
        if term.term_p.tipo != 'int':
            self.errors_chequeo_tipos.write('El lado izquierdo de la expresión multiplicativa debe ser de tipo entero.'
                                            '\n')
            term.tipo = 'ERROR'
        if term.factor_p is not None:
            term.factor_p.accept(self)
            if term.factor_p.tipo != 'int':
                self.errors_chequeo_tipos.write('El lado derecho de la expresión multiplicativa debe ser de tipo entero'
                                                '.\n')
                term.tipo = 'ERROR'
        if term.term_p.tipo == 'int' and term.factor_p.tipo == 'int':
            term.tipo = 'int'

    def visit_num(self, num):
        num.tipo = 'int'

    def visit_call(self, call):
        if call.funcion is not None:
            if call.funcion.nombre != call.id_t:
                self.errors_chequeo_tipos.write('Invocación de función no definida: ' + call.funcion.nombre + '.\n')
                call.tipo = 'ERROR'
            if call.args_p is not None:
                if len(call.funcion.parametros) == len(call.args_p):
                    error = False
                    indice = 0
                    for arg in call.args_p:
                        arg.accept(self)
                        if arg.tipo != call.funcion.parametros[indice].tipo:
                            self.errors_chequeo_tipos.write('Invocación de función definida, pero no con los mismos '
                                                            'parámetros: ' + call.funcion.nombre + '.\n')
                            call.tipo = 'ERROR'
                            error = True
                        indice = indice + 1
                    if not error:
                        call.tipo = call.funcion.tipo
                else:
                    self.errors_chequeo_tipos.write('Invocación de la función incompleta: ' + call.funcion.nombre +
                                                    '.\n')
                    call.tipo = 'ERROR'
            if call.args_p is None:
                call.tipo = call.funcion.tipo

        else:
            call.tipo = 'ERROR'
            if call.args_p is not None:
                for arg in call.args_p:
                    arg.tipo = 'ERROR'
