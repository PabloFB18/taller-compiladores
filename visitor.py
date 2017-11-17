class Visitor(object):
    def __init__(self):
        self.ast = ''
        self.id_program = 0
        self.id_var_declaration = 0
        self.id_fun_declaration = 0
        self.id_param = 0
        self.id_compound_stmt = 0
        self.id_expression_stmt = 0
        self.id_selection_stmt = 0
        self.id_iteration_stmt = 0
        self.id_return_stmt = 0
        self.id_expression = 0
        self.id_var = 0
        self.id_simple_expression = 0
        self.id_aditive_expression = 0
        self.id_term = 0
        self.id_call = 0

    # def visit_null(self, null):
    #     self.ast += "vacio" + "\n\t"
    #     # return id

    def visit_program(self, program):
        self.id_program += 1
        for declaration in program.declarations_p:
            self.ast += '\t"program' + str(self.id_program) + '" '
            declaration.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def visit_var_declaration(self, var_declaration):
        self.id_var_declaration += 1
        if not var_declaration.numero_si_no:
            var = '-> ' + '"var' + str(self.id_var_declaration) + ': ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '"'
            self.ast += var + '\n'
        else:
            var = '-> ' + '"var' + str(self.id_var_declaration) + ': ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '[' + var_declaration.num_t + ']"'
            self.ast += var + '\n'

    def visit_fun_declaration(self, fun_declaration):
        self.id_fun_declaration += 1
        fun = '"function' + str(self.id_fun_declaration) + ': ' + fun_declaration.type_specifier_t + ' ' + \
            fun_declaration.id_t + '"'
        self.ast += '-> ' + fun + '\n'
        if fun_declaration.compound_stmt_p.local_declarations_p is not None or \
                fun_declaration.compound_stmt_p.stmt_list_p is not None:
            self.ast += '\t' + fun + ' '
            fun_declaration.compound_stmt_p.accept(self)
        if fun_declaration.params_p is not None:
            for param in fun_declaration.params_p:
                self.ast += '\t' + fun + ' '
                param.accept(self)

    def visit_param(self, param):
        self.id_param += 1
        if param.arreglo_si_no:
            param = '-> ' + '"param' + str(self.id_param) + ': ' + param.type_specifier_t + ' ' + \
                  param.id_t + '"'
            self.ast += param + '\n'
        else:
            param = '-> ' + '"param' + str(self.id_param) + ': ' + param.type_specifier_t + '[] ' + \
                  param.id_t + '"'
            self.ast += param + '\n'

    def visit_compound_stmt(self, compound_stmt):
        self.id_compound_stmt += 1
        self.ast += '-> ' + '"compound_stmt' + str(self.id_compound_stmt) + '"' + '\n'
        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    self.ast += '\t"compound_stmt' + str(self.id_compound_stmt) + '" '
                    local_declaration.accept(self)
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    self.ast += '\t"compound_stmt' + str(self.id_compound_stmt) + '" '
                    stmt.accept(self)

    def visit_expression_stmt(self, expresion_stmt):
        self.id_expression_stmt += 1
        self.ast += '-> ' + '"expresion' + str(self.id_expression_stmt) + '"' + '\n'
        self.ast += '\t"expresion' + str(self.id_expression_stmt) + '" '
        expresion_stmt.expresion_p.accept(self)

    def visit_selection_stmt(self, selection_stmt):
        if not selection_stmt.else_si_no:
            self.id_selection_stmt += 1
            self.ast += '-> "' + 'if' + str(self.id_selection_stmt) + '"' + '\n'
            self.ast += '\t"' + 'if' + str(self.id_selection_stmt) + '" '
            selection_stmt.expresion_p.accept(self)
            self.ast += '\t"' + 'if' + str(self.id_selection_stmt) + '" '
            selection_stmt.stmt_p.accept(self)
        else:
            self.id_selection_stmt += 1
            self.ast += '-> "' + 'if_else' + str(self.id_selection_stmt) + '"' + '\n'
            self.ast += '\t"' + 'if_else' + str(self.id_selection_stmt) + '" '
            selection_stmt.expresion_p.accept(self)
            self.ast += '\t"' + 'if_else' + str(self.id_selection_stmt) + '" '
            selection_stmt.stmt_p.accept(self)
            self.ast += '\t"' + 'if_else' + str(self.id_selection_stmt) + '" '
            selection_stmt.stmt2_p.accept(self)

    def visit_iteration_stmt(self, iteration_stmt):
        self.id_iteration_stmt += 1
            # self.ast += '-> "' + 'if' + str(self.id_selection_stmt) + '"' + '\n'
            # self.ast += '\t"' + 'if' + str(self.id_selection_stmt) + '" '
            # selection_stmt.expresion_p.accept(self)
            # self.ast += '\t"' + 'if' + str(self.id_selection_stmt) + '" '
            # selection_stmt.stmt_p.accept(self)

    def visit_return_stmt(self, return_stmt):
        self.id_return_stmt += 1

    def visit_expression(self, expression):
        self.id_expression += 1
        pass

    def visit_var(self, var):
        self.id_var += 1
        pass

    def visit_simple_expression(self, simple_expresion):
        self.id_simple_expression += 1
        pass

    def visit_aditive_expression(self, aditive_expresion):
        self.id_aditive_expression += 1
        pass

    def visit_term(self, term):
        self.id_term += 1
        pass

    def visit_call(self, call):
        self.id_call += 1
        pass
