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
        self.id_additive_expression = 0
        self.id_term = 0
        self.id_num = 0
        self.id_call = 0

    # def visit_null(self, null):
    #     self.ast += "vacio" + "\n\t"
    #     # return id

    def visit_program(self, program):
        self.id_program += 1
        id_program = self.id_program
        for declaration in program.declarations_p:
            self.ast += '\t"program' + str(id_program) + '" '
            declaration.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def visit_var_declaration(self, var_declaration):
        self.id_var_declaration += 1
        id_var_declaration = self.id_var_declaration
        if not var_declaration.numero_si_no:
            var = '-> ' + '"var' + str(id_var_declaration) + ': ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '"'
            self.ast += var + '\n'
        else:
            var = '-> ' + '"var' + str(id_var_declaration) + ': ' + var_declaration.type_specifier_t + ' ' + \
                        var_declaration.id_t + '[' + var_declaration.num_t + ']"'
            self.ast += var + '\n'

    def visit_fun_declaration(self, fun_declaration):
        self.id_fun_declaration += 1
        id_fun_declaration = self.id_fun_declaration
        fun = '"function' + str(id_fun_declaration) + ': ' + fun_declaration.type_specifier_t + ' ' + \
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
        id_param = self.id_param
        if param.arreglo_si_no:
            param = '-> ' + '"param' + str(id_param) + ': ' + param.type_specifier_t + ' ' + \
                  param.id_t + '"'
            self.ast += param + '\n'
        else:
            param = '-> ' + '"param' + str(id_param) + ': ' + param.type_specifier_t + '[] ' + \
                  param.id_t + '"'
            self.ast += param + '\n'

    def visit_compound_stmt(self, compound_stmt):
        self.id_compound_stmt += 1
        id_compound_stmt = self.id_compound_stmt
        self.ast += '-> ' + '"compound_stmt' + str(id_compound_stmt) + '"' + '\n'
        if compound_stmt.local_declarations_p is not None:
            for local_declaration in compound_stmt.local_declarations_p:
                if local_declaration is not None:
                    self.ast += '\t"compound_stmt' + str(id_compound_stmt) + '" '
                    local_declaration.accept(self)
        if compound_stmt.stmt_list_p is not None:
            for stmt in compound_stmt.stmt_list_p:
                if stmt is not None:
                    self.ast += '\t"compound_stmt' + str(id_compound_stmt) + '" '
                    stmt.accept(self)

    # def visit_expression_stmt(self, expresion_stmt):
    #     self.id_expression_stmt += 1
    #     id_expression_stmt = self.id_expression_stmt
    #     self.ast += '-> ' + '"expresion_stmt' + str(id_expression_stmt) + '"' + '\n'
    #     self.ast += '\t"expresion_stmt' + str(id_expression_stmt) + '" '
    #     expresion_stmt.expresion_p.accept(self)

    def visit_selection_stmt(self, selection_stmt):
        self.id_selection_stmt += 1
        id_selection_stmt = self.id_selection_stmt
        if not selection_stmt.else_si_no:
            self.ast += '-> "' + 'if' + str(id_selection_stmt) + '"' + '\n'
            self.ast += '\t"' + 'if' + str(id_selection_stmt) + '" '
            selection_stmt.expression_p.accept(self)
            self.ast += '\t"' + 'if' + str(id_selection_stmt) + '" '
            selection_stmt.stmt_p.accept(self)
        else:
            self.ast += '-> "' + 'if_else' + str(id_selection_stmt) + '"' + '\n'
            self.ast += '\t"' + 'if_else' + str(id_selection_stmt) + '" '
            selection_stmt.expression_p.accept(self)
            self.ast += '\t"' + 'if_else' + str(id_selection_stmt) + '" '
            selection_stmt.stmt_p.accept(self)
            self.ast += '\t"' + 'if_else' + str(id_selection_stmt) + '" '
            selection_stmt.stmt2_p.accept(self)

    def visit_iteration_stmt(self, iteration_stmt):
        self.id_iteration_stmt += 1
        id_iteration_stmt = self.id_iteration_stmt
        self.ast += '-> "' + 'while' + str(id_iteration_stmt) + '"' + '\n'
        self.ast += '\t"' + 'while' + str(id_iteration_stmt) + '" '
        iteration_stmt.expression_p.accept(self)
        self.ast += '\t"' + 'while' + str(id_iteration_stmt) + '" '
        iteration_stmt.stmt_p.accept(self)

    def visit_return_stmt(self, return_stmt):
        self.id_return_stmt += 1
        id_return_stmt = self.id_return_stmt
        self.ast += '-> "' + 'return' + str(id_return_stmt) + '"' + '\n'
        if not return_stmt.expression_si_no:
            self.ast += '\t"' + 'return' + str(id_return_stmt) + '" '
            return_stmt.expression_p.accept(self)

    def visit_expression(self, expression):
        self.id_expression += 1
        id_expression = self.id_expression
        self.ast += '-> "' + 'assign' + str(id_expression) + '"' + '\n'
        self.ast += '\t"' + 'assign' + str(id_expression) + '" '
        expression.var_p.accept(self)
        self.ast += '\t"' + 'assign' + str(id_expression) + '" '
        expression.expression_p.accept(self)

    def visit_var(self, var):
        self.id_var += 1
        id_var = self.id_var
        self.ast += '-> "' + 'var' + str(id_var) + ': ' + var.id_t + '"' + '\n'
        if var.expression_si_no:
            self.ast += '\t"' + 'var' + str(id_var) + ': ' + var.id_t + '" '
            var.expression_p.accept(self)

    def visit_simple_expression(self, simple_expresion):
        self.id_simple_expression += 1
        id_simple_expression = self.id_simple_expression
        self.ast += '-> "COMPARADOR' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '"' + '\n'
        self.ast += '\t"COMPARADOR' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
        simple_expresion.additive_expression1_p.accept(self)
        self.ast += '\t"COMPARADOR' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
        simple_expresion.additive_expression2_p.accept(self)

    def visit_additive_expression(self, additive_expresion):
        self.id_additive_expression += 1
        id_additive_expression = self.id_additive_expression
        self.ast += '-> "SIGNO' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '"' + '\n'
        self.ast += '\t"SIGNO' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
        additive_expresion.additive_expression_p.accept(self)
        self.ast += '\t"SIGNO' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
        additive_expresion.term_p.accept(self)

    def visit_term(self, term):
        self.id_term += 1
        id_term = self.id_term
        self.ast += '-> "SIGNO' + str(id_term) + ': ' + term.mulop_t + '"' + '\n'
        self.ast += '\t"SIGNO' + str(id_term) + ': ' + term.mulop_t + '" '
        term.term_p.accept(self)
        self.ast += '\t"SIGNO' + str(id_term) + ': ' + term.mulop_t + '" '
        term.factor_p.accept(self)

    def visit_num(self, num):
        self.id_num += 1
        id_num = self.id_num
        self.ast += '-> "NUM' + str(id_num) + ': ' + num.num_t + '"' + '\n'

    def visit_call(self, call):
        self.id_call += 1
        id_call = self.id_call
        self.ast += '-> "' + 'call' + str(id_call) + '"' + '\n'
        for arg in call.args_p:
            self.ast += '\t"' + 'call' + str(id_call) + '" '
            arg.accept(self)

