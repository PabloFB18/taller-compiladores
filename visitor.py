class Visitor(object):
    def __init__(self):
        self.ast = ''

    # def visit_null(self, null):
    #     self.ast += "vacio" + "\n\t"
    #     # return id

    def visit_program(self, program):
        for declaration in program.declarations_p:
            self.ast += '\t"program" '
            declaration.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def visit_var_declaration(self, var_declaration):
        if var_declaration.num_t is None:
            var = '-> ' + '"var: ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '"'
            self.ast += var + '\n'
        else:
            var = '-> ' + '"var: ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '[' + var_declaration.num_t + ']"'
            self.ast += var + '\n'

    def visit_fun_declaration(self, fun_declaration):
        fun = '"function: ' + fun_declaration.type_specifier_t + ' ' + \
                    fun_declaration.id_t + '"'
        self.ast += '-> ' + fun + '\n'
        if fun_declaration.compound_stmt_p.local_declarations_p is not None or \
                fun_declaration.compound_stmt_p.stmt_list_p is not None:
            self.ast += '\t' + fun
            fun_declaration.compound_stmt_p.accept(self)
        if fun_declaration.params_p is not None:
            for param in fun_declaration.params_p:
                self.ast += '\t' + fun
                param.accept(self)

    def visit_param(self, param):
        if param.arreglo_si_no:
            param = '-> ' + '"param: ' + param.type_specifier_t + ' ' + \
                  param.id_t + '"'
            self.ast += param + '\n'
        else:
            param = '-> ' + '"param: ' + param.type_specifier_t + '[] ' + \
                  param.id_t + '"'
            self.ast += param + '\n'

    def visit_compound_stmt(self, compound_stmt):
        self.ast += '-> ' + '"compound stmt"' + '\n'
        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    self.ast += '\t"compound stmt" '
                    local_declaration.accept(self)
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    self.ast += '\t"compound stmt" '
                    stmt.accept(self)

    def visit_expression_stmt(self, expresion_stmt):
        self.ast += '-> ' + '"expresion"' + '\n'
        self.ast += '\t"expresion" '
        expresion_stmt.expresion_p.accept(self)

    def visit_selection_stmt(self, selection_stmt):
        self.ast += '-> ' + '"if / if else"' + '\n'
        self.ast += '\t"expresion" '

    def visit_iteration_stmt(self, iteration_stmt):
        pass

    def visit_return_stmt(self, return_stmt):
        pass

    def visit_var(self, var):
        pass

    def visit_simple_expression(self, simple_expresion):
        pass
