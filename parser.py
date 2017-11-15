import ply.yacc as yacc

# Obtener tokens del scanner
from __builtin__ import raw_input

import nodos
from scanner import tokens


precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVI'),
    ('right', 'ID', 'NUM'),
    ('left', 'DPAREN', 'IPAREN')
)


def p_program(p):
    """program : declarationList"""
    p[0] = nodos.Program(p[1])


def p_declaration_list1(p):
    """declarationList : declarationList declaration"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_declaration_list2(p):
    """declarationList : declaration"""
    p[0] = p[1]


def p_declaration1(p):
    """declaration : varDeclaration"""
    p[0] = p[1]


def p_declaration2(p):
    """declaration : funDeclaration"""
    p[0] = p[1]


def p_var_declaration1(p):
    """varDeclaration : typeSpecifier ID PUNTOC"""
    p[0] = nodos.VarDeclaration(p[1], p[2])


def p_var_declaration2(p):
    """varDeclaration : typeSpecifier ID ICORCH NUM DCORCH PUNTOC"""
    p[0] = nodos.VarDeclaration(p[1], p[2], p[4])


def p_type_specifier1(p):
    """typeSpecifier : INT"""
    p[0] = p[1]


def p_type_specifier2(p):
    """typeSpecifier : VOID"""
    p[0] = p[1]


def p_fun_declaration(p):
    """funDeclaration : typeSpecifier ID IPAREN params DPAREN compoundStmt"""
    p[0] = nodos.FunDeclaration(p[1], p[2], p[4], p[6])


def p_params1(p):
    """params : paramList"""
    p[0] = p[1]


def p_params2(p):
    """params : VOID"""
    pass


def p_paramList1(p):
    """paramList : paramList COMA param"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_paramList2(p):
    """paramList : param"""
    p[0] = p[1]


def p_param1(p):
    """param : typeSpecifier ID"""
    p[0] = nodos.Param(p[1], p[2], False)


def p_param2(p):
    """param : typeSpecifier ID ICORCH DCORCH"""
    p[0] = nodos.Param(p[1], p[2], True)


def p_compoundStmt(p):
    """compoundStmt : ILLAVE localDeclarations statementList DLLAVE"""
    p[0] = nodos.CompoundStmt(p[1], p[2])


def p_localDeclarations1(p):
    """localDeclarations : localDeclarations varDeclaration"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_localDeclarationsEmpty(p):
    """localDeclarations :  empty"""
    p[0] = nodos.Null()


def p_statementList1(p):
    """statementList : statementList statement"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_statementListEmpty(p):
    """statementList : empty"""
    p[0] = nodos.Null()


def p_statement1(p):
    """statement : expressionStmt"""
    p[0] = p[1]


def p_statement2(p):
    """statement : compoundStmt"""
    p[0] = p[1]


def p_statement3(p):
    """statement : selectionStmt"""
    p[0] = p[1]


def p_statement4(p):
    """statement : iterationStmt"""
    p[0] = p[1]


def p_statement5(p):
    """statement : returnStmt"""
    p[0] = p[1]


def p_expressionStmt1(p):
    """expressionStmt : expression PUNTOC"""
    p[0] = p[1]


def p_expressionStmt2(p):
    """expressionStmt : PUNTOC"""
    pass


def p_selectionStmt1(p):
    """selectionStmt : IF IPAREN expression DPAREN statement"""
    p[0] = nodos.SelectionStmt(p[1], p[3], p[5])


def p_selectionStmt2(p):
    """selectionStmt :  IF IPAREN expression DPAREN statement ELSE statement"""
    p[0] = nodos.SelectionStmt(p[1], p[3], p[5], p[6], p[7])


def p_iterationStmt(p):
    """iterationStmt :  WHILE IPAREN expression DPAREN statement"""


def p_returnStmt1(p):
    """returnStmt :  RETURN PUNTOC"""


def p_returnStmt2(p):
    """returnStmt :  RETURN expression PUNTOC"""


def p_expression1(p):
    """expression :  var ASIGN expression"""


def p_expression2(p):
    """expression :  simpleExpression"""


def p_var1(p):
    """var :  ID"""


def p_var2(p):
    """var :  ID ICORCH expression DCORCH"""


def p_simpleExpression1(p):
    """simpleExpression :  additiveExpression relop additiveExpression"""


def p_simpleExpression2(p):
    """simpleExpression :  additiveExpression"""


def p_relop1(p):
    """relop : MENORI"""


def p_relop2(p):
    """relop : MENOR"""


def p_relop3(p):
    """relop : MAYOR"""


def p_relop4(p):
    """relop : MAYORI"""


def p_relop5(p):
    """relop : IGUAL"""


def p_relop6(p):
    """relop : DIST"""


def p_additiveExpression1(p):
    """additiveExpression : additiveExpression addop term"""


def p_additiveExpression2(p):
    """additiveExpression : term"""


def p_addop1(p):
    """addop : SUMA"""


def p_addop2(p):
    """addop : RESTA"""


def p_term1(p):
    """term : term mulop factor"""


def p_term2(p):
    """term : factor"""


def p_mulop1(p):
    """mulop : MULTI"""


def p_mulop2(p):
    """mulop : DIVI"""


def p_factor1(p):
    """factor : IPAREN expression DPAREN"""


def p_factor2(p):
    """factor : var"""


def p_factor3(p):
    """factor : call"""


def p_factor4(p):
    """factor : NUM"""


def p_call(p):
    """call : ID IPAREN args DPAREN"""


def p_args1(p):
    """args : argList"""


def p_argsEmpty(p):
    """args : empty"""


def p_argList1(p):
    """argList : argList COMA expression"""


def p_argList2(p):
    """argList : expression"""


def p_empty(p):
    """empty :"""
    pass


# Error rule for syntax errors
def p_error(p):
    print ('Syntax error in input!')
    print ('Error en la linea ' + str(p.lineno))


# Build the parser
parser = yacc.yacc()

with open('sample.txt', 'r') as arch1:
    contents = arch1.read()
    result = parser.parse(contents)
    print result

