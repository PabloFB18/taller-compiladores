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


# class declarationList1(Nodo):
#     def __init__(self, hijo1, hijo2, name):
#         self.name = name
#         self.hijo1 = hijo1
#         self.hijo2 = hijo2
#
#     def accept(self, visitor):
#         visitor.visit_program(self)
#
#
# class declarationList2(Nodo):
#     def __init__(self, hijo1, name):
#         self.name = name
#         self.hijo1 = hijo1
#
#     def accept(self, visitor):
#         visitor.visit_program(self)
#
#
# class declaration1(Nodo):
#     def __init__(self, hijo1, name):
#         self.name = name
#         self.hijo1 = hijo1
#
#     def accept(self, visitor):
#         visitor.visit_program(self)
#
#
# class declaration2(Nodo):
#     def __init__(self, hijo1, name):
#         self.name = name
#         self.hijo1 = hijo1
#
#     def accept(self, visitor):
#         visitor.visit_program(self)


class VarDeclaration(Nodo):
    def __init__(self, type_specifier_t, identificador_t, num_t=None):
        self.type_specifier_t = type_specifier_t
        self.identificador_t = identificador_t

        if num_t is not None:
            self.num_t = num_t

    def accept(self, visitor):
        visitor.visit_var_declaration(self)


# class varDeclaration2(Nodo):
#     def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, name):
#         self.name = name
#         self.hijo1 = hijo1
#         self.hijo2 = hijo2
#         self.hijo3 = hijo3
#         self.hijo4 = hijo4
#         self.hijo5 = hijo5
#         self.hijo6 = hijo6
#
#     def accept(self, visitor):
#         visitor.visit_program(self)
#
#
# class typeSpecifier1(Nodo):
#     def __init__(self, hijo1, name):
#         self.name = name
#         self.hijo1 = hijo1
#
#     def accept(self, visitor):
#         visitor.visit_program(self)
#
#
# class typeSpecifier2(Nodo):
#     def __init__(self, hijo1, name):
#         self.name = name
#         self.hijo1 = hijo1
#
#     def accept(self, visitor):
#         visitor.visit_program(self)


class FunDeclaration(Nodo):
    def __init__(self, type_specifier_t, identificador_t, params_p, compound_stmt_p):
        self.type_specifier_t = type_specifier_t
        self.identificador_t = identificador_t
        self.params_p = params_p
        self.compound_stmt_p = compound_stmt_p

    def accept(self, visitor):
        visitor.visit_fun_declaration(self)


class params1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class params2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class paramList1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def accept(self, visitor):
        visitor.visit_program(self)


class paramList2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class param1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class param2(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4

    def accept(self, visitor):
        visitor.visit_program(self)


class compoundStmt(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4

    def accept(self, visitor):
        visitor.visit_program(self)


class localDeclarations1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class statementList1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class statement1(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class statement2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class statement3(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class statement4(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class statement5(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class expressionStmt1(Nodo):
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def accept(self, visitor):
        visitor.visit_program(self)


class expressionStmt2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class selectionStmt1(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4
        self.hijo5 = hijo5

    def accept(self, visitor):
        visitor.visit_program(self)


class selectionStmt2(Nodo):
    def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, hijo7, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4
        self.hijo5 = hijo5
        self.hijo6 = hijo6
        self.hijo7 = hijo7

    def accept(self, visitor):
        visitor.visit_program(self)


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
