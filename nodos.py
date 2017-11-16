class Nodo():
    pass


# class Null(Nodo):
#     def __init__(self):
#         self.type = 'empty'


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
    def __init__(self, local_declarations_p, stmt_list_p):
        self.local_declarations_p = local_declarations_p
        self.stmt_list_p = stmt_list_p

    def accept(self, visitor):
        visitor.visit_compound_stmt(self)


class ExpressionStmt(Nodo):
    def __init__(self, expresion_p):
        self.expresion_p = expresion_p

    def accept(self, visitor):
        visitor.visit_expression_stmt(self)


class SelectionStmt(Nodo):
    def __init__(self, if_t, expresion_p, stmt_p, else_t=None, stmt2_p=None):
        self.if_t = if_t
        self.expresion_p = expresion_p
        self.stmt_p = stmt_p
        self.else_t = None

        if else_t is not None:
            self.else_t = else_t
            self.stmt2_p = stmt2_p

    def accept(self, visitor):
        visitor.visit_selection_stmt(self)


class IterationStmt(Nodo):
    def __init__(self, while_t, expression_p, stmt_p):
        self.while_t = while_t
        self.expression_p = expression_p
        self.stmt_p = stmt_p

    def accept(self, visitor):
        visitor.visit_iteration_stmt(self)


class ReturnStmt(Nodo):
    def __init__(self, return_t, expression_p=None):
        self.return_t = return_t

        if expression_p is not None:
            self.expression_p = expression_p

    def accept(self, visitor):
        visitor.visit_return_stmt(self)


class Var(Nodo):
    def __init__(self, id_t, expression_p=None):
        self.id_t = id_t
        if expression_p is not None:
            self.expression_p = expression_p

    def accept(self, visitor):
        visitor.visit_var(self)


class SimpleExpression(Nodo):
    def __init__(self, additive_expression1_p, relop_p=None, additive_expression2_p=None):
        self.additive_expression1_p = additive_expression1_p
        if relop_p is not None and additive_expression2_p is not None:
            self.relop_p = relop_p
            self.additive_expression2_p = additive_expression2_p

    def accept(self, visitor):
        visitor.visit_simple_expression(self)


class Relop1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class Relop2(Nodo):
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
