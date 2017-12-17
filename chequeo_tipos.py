# coding=utf-8
from string import lower


class ChequeoTipos(object):
    def __init__(self):
        pass

    def visit_program(self, program):
        for declaration in program.declarations_p:
            declaration.accept(self)

    def visit_var_declaration(self, var_declaration):
        var_declaration.tipo = lower(var_declaration.type_specifier_t)

    def visit_fun_declaration(self, fun_declaration):
        if fun_declaration.compound_stmt_p.local_declarations_p is not None or fun_declaration.compound_stmt_p.stmt_list_p is not None:
            fun_declaration.compound_stmt_p.accept(self)
            if fun_declaration.compound_stmt_p.tipo == 'ERROR':
                fun_declaration.tipo = fun_declaration.compound_stmt_p.tipo
            else:
                fun_declaration.tipo = lower(fun_declaration.type_specifier_t)
        if fun_declaration.params_p is not None:
            for param in fun_declaration.params_p:
                param.accept(self)
                if param.tipo == 'ERROR':
                    fun_declaration.tipo = param.tipo

    def visit_param(self, param):
        if lower(param.type_specifier_t) != 'int' or lower(param.type_specifier_t) != 'void':
            print('El parámetro es de tipo desconocido.')
            param.tipo = 'ERROR'
        else:
            param.tipo = lower(param.type_specifier_t)

    def visit_compound_stmt(self, compound_stmt):

        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    local_declaration.accept(self)
                    if local_declaration.tipo == 'ERROR':
                        compound_stmt.tipo = local_declaration.tipo
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    stmt.accept(self)
                    if stmt.tipo == 'ERROR':
                        compound_stmt.tipo = stmt.tipo

    def visit_selection_stmt(self, selection_stmt):
        if not selection_stmt.else_si_no:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.expression_p.tipo != 'int':
                print('La condición de la selección debe ser de tipo entero.')
                selection_stmt.tipo = 'ERROR'
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
                if selection_stmt.stmt_p.tipo == 'ERROR':
                    selection_stmt.tipo = selection_stmt.stmt_p.tipo
        else:
            selection_stmt.expression_p.accept(self)
            if selection_stmt.expression_p.tipo != 'int':
                print('La condición de la selección debe ser de tipo entero.')
                selection_stmt.tipo = 'ERROR'
            if selection_stmt.stmt_p is not None:
                selection_stmt.stmt_p.accept(self)
                if selection_stmt.stmt_p.tipo == 'ERROR':
                    selection_stmt.tipo = selection_stmt.stmt_p.tipo
            if selection_stmt.stmt2_p is not None:
                selection_stmt.stmt2_p.accept(self)
                if selection_stmt.stmt2_p.tipo == 'ERROR':
                    selection_stmt.tipo = selection_stmt.stmt2_p.tipo

    def visit_iteration_stmt(self, iteration_stmt):
        iteration_stmt.expression_p.accept(self)
        if iteration_stmt.expression_p.tipo != 'int':
            print(' La condición de la iteración debe ser de tipo entero.')
            iteration_stmt.tipo = 'ERROR'
        if iteration_stmt.stmt_p is not None:
            iteration_stmt.stmt_p.accept(self)
            if iteration_stmt.stmt_p.tipo == 'ERROR':
                iteration_stmt.tipo = iteration_stmt.stmt_p.tipo

    def visit_return_stmt(self, return_stmt):
        if return_stmt.expression_si_no:
            return_stmt.expression_p.accept(self)
            if return_stmt.expression_p.tipo != 'int':
                return_stmt.tipo = 'ERROR'

    def visit_expression(self, expression):
        expression.var_p.accept(self)
        expression.expression_p.accept(self)
        if expression.var_p.tipo == expression.expression_p.tipo:
            expression.tipo = expression.var_p.tipo
        else:
            print('La expresión debe ser del mismo tipo que la variable declarada.')
            expression.tipo = 'ERROR'

    def visit_var(self, var):
        nombre = var.id_t
        variables_declaradas = var.simbolos.declaraciones
        for variable in variables_declaradas:
            if variable.nombre == nombre:
                if variable.arreglo_si_no:  #Si es arreglo
                    if var.expression_si_no: #Si es llamado un valor del arreglo
                        var.expression_p.accept(self)
                        if var.expression_p.tipo != 'int':
                            print('El índice de un arreglo debe ser de tipo entero.')
                            var.tipo = 'ERROR'
                        # TODO: VALIDAR SI EL INDICE NO ES MAYOR AL TAMAÑO
                        var.tipo = lower(variable.tipo)
                    else:
                        var.tipo = 'intArreglo'
                else:
                    # TODO: VER SI ESTA INICIALIZADA
                    var.tipo = lower(variable.tipo)
                break


    def visit_simple_expression(self, simple_expresion):
        simple_expresion.additive_expression1_p.accept(self)
        if simple_expresion.additive_expression2_p.tipo != 'int':
            print('El lado izquierdo de la comparación debe ser de tipo entero.')
            simple_expresion.tipo = 'ERROR'
        simple_expresion.additive_expression2_p.accept(self)
        if simple_expresion.additive_expression2_p.tipo != 'int':
            print('El lado derecho de la comparación debe ser de tipo entero.')
            simple_expresion.tipo = 'ERROR'
        else:
            simple_expresion.tipo = 'int'

    def visit_additive_expression(self, additive_expresion):
        additive_expresion.additive_expression_p.accept(self)
        if additive_expresion.additive_expression_p.tipo != 'int':
            print('El lado izquierdo de la expresión aditiva debe ser de tipo entero.')
            additive_expresion.tipo = 'ERROR'
        additive_expresion.term_p.accept(self)
        if additive_expresion.term_p.tipo != 'int':
            print('El lado derecho de la expresión aditiva debe ser de tipo entero.')
            additive_expresion.tipo = 'ERROR'
        else:
            additive_expresion.tipo = 'int'

    def visit_term(self, term):
        term.term_p.accept(self)
        if(term.term_p.tipo != 'int'):
            print('El lado izquierdo de la expresión multiplicativa debe ser de tipo entero.')
            term.tipo = 'ERROR'
        else:
            term.tipo = term.term_p.tipo
        if term.factor_p is not None:
            term.factor_p.accept(self)
            if (term.factor_p.tipo != 'int'):
                print('El lado derecho de la expresión multiplicativa debe ser de tipo entero.')
                term.tipo = 'ERROR'
            else:
                term.tipo = term.factor_p.tipo

    def visit_num(self, num):
        num.tipo = 'int'

    def visit_call(self, call):
        if call.funcion.nombre != call.id_t:
            print('Invocación de función no definida: ' + call.funcion.nombre)
            call.tipo = 'ERROR'
        if call.args_p is not None:
            if len(call.funcion.parametros) == len(call.args_p):
                indice = 0
                for arg in call.args_p:
                    arg.accept(self)
                    if arg.tipo != call.funcion.parametros[indice]:
                        print('Invocación de función definida, pero no con los mismos parámetros: ' + call.funcion.nombre)
                        call.tipo = 'ERROR'
                    indice = indice + 1
            else:
                print('Invocación de la función incompleta: ' + call.funcion.nombre)
                call.tipo = 'ERROR'
            call.tipo = call.funcion.tipo




