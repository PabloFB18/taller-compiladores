class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'empty'


class program(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def accept(self, visitor):
        visitor.visit_program(self)


class declarationList1(Nodo): 
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2


class declarationList2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class declaration1(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class declaration2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class varDeclaration1(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3


class varDeclaration2(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4
        self.hijo5 = hijo5
        self.hijo6 = hijo6

class typeSpecifier1(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class typeSpecifier2(Nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class funDeclaration(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4
        self.hijo5 = hijo5
        self.hijo6 = hijo6


class params1(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class params2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class paramList1(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3


class paramList2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class param1(Nodo): 
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2


class param2(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4


class compoundStmt(Nodo): 
    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4


class localDeclarations1(Nodo): 
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2


class statementList1(Nodo): 
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2


class statement1(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class statement2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class statement3(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class statement4(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class statement5(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


class expressionStmt1(Nodo): 
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2


class expressionStmt2(Nodo): 
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1


# TODO: hasta aqui llegamos
class selectionStmt1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class selectionStmt2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class iterationStmt(Nodo): 
    def __init__(self, name): 
        self.name = name    


class returnStmt1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class returnStmt2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class expression1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class expression2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class var1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class var2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class simpleExpression1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class simpleExpression2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop3(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop4(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop5(Nodo): 
    def __init__(self, name): 
        self.name = name    


class relop6(Nodo): 
    def __init__(self, name): 
        self.name = name    


class additiveExpression1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class additiveExpression2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class addop1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class addop2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class term1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class term2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class mulop1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class mulop2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class factor1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class factor2(Nodo): 
    def __init__(self, name): 
        self.name = name    


class factor3(Nodo): 
    def __init__(self, name): 
        self.name = name    


class factor4(Nodo): 
    def __init__(self, name): 
        self.name = name    


class call(Nodo): 
    def __init__(self, name): 
        self.name = name    


class args1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class argsEmpty(Nodo): 
    def __init__(self, name): 
        self.name = name    


class argList1(Nodo): 
    def __init__(self, name): 
        self.name = name    


class argList2(Nodo): 
    def __init__(self, name): 
        self.name = name    

