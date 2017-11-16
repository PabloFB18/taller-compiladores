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
    def __init__(self, local_declaration_p, stmt_list_p):
        self.local_declaration_p = local_declaration_p
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


class Expression(Nodo):
    def __init__(self, var_p, asign_t, expression_p):

        self.var_p = var_p
        self.asign_t = asign_t
        self.expression_p = expression_p

    def accept(self, visitor):
        visitor.visit_expression(self)


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


class Relop(Nodo):
    def __init__(self, relop_t):
        self.relop_t = relop_t

    def accept(self, visitor):
        visitor.visit_relop(self)


class AdditiveExpression(Nodo):
    def __init__(self, term_p, additive_expression_p=None, addop_t=None):
        self.term_p = term_p
        if additive_expression_p is not None and addop_t is not None:
            self.additive_expression_p = additive_expression_p
            self.addop_t = addop_t

    def accept(self, visitor):
        visitor.visit_additive_expression(self)


class Term(Nodo):
    def __init__(self, factor_p, term_p=None, mulop_t=None):
        self.factor_p = factor_p
        if term_p is not None and mulop_t is not None:
            self.term_p = term_p
            self.mulop_t = mulop_t

    def accept(self, visitor):
        visitor.visit_term(self)


class Call(Nodo):
    def __init__(self, id_t, args_p):
        self.id_t = id_t
        self.args_p = args_p

    def accept(self, visitor):
        visitor.visit_call(self)






