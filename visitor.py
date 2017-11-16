class Visitor(object):
    def __init__(self):
        self.ast = ''

    def visit_null(self, null):
        self.ast += "[label=" + "vacio" + "]" + "\n\t"
        return id

    def visit_program(self, program):
        self.ast += "[label= " + "program" + "]" + "\n\t"
        for declaration in program.declarations_p:
            print declaration.accept(self)
            declaration_txt = declaration.accept(self)
            self.ast += "->" + declaration_txt + "\n\t"
        return "digraph G {\n\t"+self.ast+"}"

    def visit_var_declaration(self, var_declaration):
        if var_declaration.num_t is None:
            self.ast += "[label= " + "var declaration: " + var_declaration.type_specifier_t + " " + \
                        var_declaration.id_t + "]" + "\n\t"
        else:
            self.ast += "[label= " + "var declaration: " + var_declaration.type_specifier_t + " " + \
                        var_declaration.id_t + "[" + var_declaration.num_t + "]" + "]" + "\n\t"
        return self.ast

    def visit_fun_declaration(self, fun_declaration):
        pass

    def visit_param(self, para):
        pass

    def visit_compound_stmt(self, compound_stmt):
        pass

    def visit_selection_stmt(self, selection_stmt):
        pass
