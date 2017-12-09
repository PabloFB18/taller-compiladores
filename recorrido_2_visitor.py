class Recorrido2Visitor(object):
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

    def visit_program(self, program):
        self.id_program += 1
        id_program = self.id_program
        for declaration in program.declarations_p:
            self.ast += '\t"program' + str(id_program) + 'NODE TYPE:'+str(self.check_sym_tab(program)) + '" '
            declaration.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def visit_var_declaration(self, var_declaration):
        self.id_var_declaration += 1
        id_var_declaration = self.id_var_declaration
        if not var_declaration.numero_si_no:
            var = '-> ' + '"var' + str(id_var_declaration) + 'NODE TYPE:'+str(self.check_sym_tab(var_declaration)) + ': ' + var_declaration.type_specifier_t + ' ' + \
                  var_declaration.id_t + '"'
            self.ast += var + '\n'
        else:
            var = '-> ' + '"var' + str(id_var_declaration) + 'NODE TYPE:'+str(self.check_sym_tab(var_declaration)) + ': ' + var_declaration.type_specifier_t + ' ' + \
                  var_declaration.id_t + '[' + var_declaration.num_t + ']"'
            self.ast += var + '\n'

    def visit_fun_declaration(self, fun_declaration):
        pass

    def visit_param(self, param):
        pass

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

    def check_sym_tab(self, nodo):
        kind = nodo.kind

        if kind == 'fun_declaration':
            return 'ERROR'

        if kind == 'expression':
            tipo = self.check_sym_tab(nodo.hijo[0])
            if tipo != 'int':
                return 'ERROR'
            return 'int'

        if kind == 'simple_expression':
            tipo = self.check_sym_tab(nodo.hijo[0])
            if tipo != 'int':
                return 'ERROR'
            tipo = self.check_sym_tab(nodo.hijo[1])
            if tipo != 'int':
                return 'ERROR'
            return 'bool'

        if kind == 'additive_expression':
            tipo = self.check_sym_tab(nodo.hijo[0])
            if tipo != 'int':
                return 'ERROR'
            tipo = self.check_sym_tab(nodo.hijo[1])
            if tipo != 'int':
                return 'ERROR'
            return 'int'

        if kind == 'term':
            tipo = self.check_sym_tab(nodo.hijo[0])
            if tipo != 'int':
                return 'ERROR'
            tipo = self.check_sym_tab(nodo.hijo[1])
            if tipo != 'int':
                return 'ERROR'
            return 'int'

        # Falta lo de la funcion y las variables, me base en el semantic.c

        return 'ERROR'
