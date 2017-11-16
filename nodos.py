class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'empty'


class Program(Nodo):
    def __init__(self, declarations_p):
        self.declarations_p = declarations_p

    def accept(self, visitor):
        visitor.visit_program(self)


class VarDeclaration(Nodo):
    def __init__(self, type_specifier_t, id_t, num_t=None):
        self.type_specifier_t = type_specifier_t
        self.id_t = id_t
        self.num_t = None

        if num_t is not None:
            self.num_t = num_t

    def accept(self, visitor):
        visitor.visit_var_declaration(self)


class FunDeclaration(Nodo):
    def __init__(self, type_specifier_t, id_t, params_p, compound_stmt_p):
        self.type_specifier_t = type_specifier_t
        self.id_t = id_t
        self.params_p = params_p
        self.compound_stmt_p = compound_stmt_p

    def accept(self, visitor):
        visitor.visit_fun_declaration(self)


class Param(Nodo):
    def __init__(self, type_specifier_t, id_t, arreglo_si_no):
        self.type_specifier_t = type_specifier_t
        self.id_t = id_t
        self.arreglo_si_no = arreglo_si_no

    def accept(self, visitor):
        visitor.visit_param(self)


class CompoundStmt(Nodo):
    def __init__(self, local_declaration_p, stmt_list_p):
        self.local_declaration_p = local_declaration_p
        self.stmt_list_p = stmt_list_p

    def accept(self, visitor):
        visitor.visit_compound_stmt(self)


class SelectionStmt(Nodo):
    def __init__(self, if_t, expresion_p, stmt_p, else_t=None, stmt2_p=None):
        self.if_t = if_t
        self.expresion_p = expresion_p
        self.stmt_p = stmt_p

        if else_t is not None:
            self.else_t = else_t
            self.stmt2_p = stmt2_p

    def accept(self, visitor):
        visitor.visit_selection_stmt(self)


# TODO: hasta aqui llegamos
class iterationStmt(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4
        self.hijo5 = hijo5

    def accept(self, visitor):
        visitor.visit_program(self)


class returnStmt1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class returnStmt2(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class expression1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class expression2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class var1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class var2(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4

    def accept(self, visitor):
        visitor.visit_program(self)


class simpleExpression1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class simpleExpression2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class relop1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class relop2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class relop3(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class relop4(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class relop5(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class relop6(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class additiveExpression1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class additiveExpression2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class addop1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class addop2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class term1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class term2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class mulop1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class mulop2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class factor1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class factor2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class factor3(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class factor4(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class call(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4

    def accept(self, visitor):
        visitor.visit_program(self)


class args1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class argList1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class argList2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)
