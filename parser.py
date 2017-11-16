import ply.yacc as yacc

# Obtener tokens del scanner
from __builtin__ import raw_input

import nodos
from scanner import tokens
from visitor import Visitor

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVI'),
    ('right', 'ID', 'NUM'),
    ('left', 'DPAREN', 'IPAREN')
)


def p_program(p):
    """program : declaration_list"""
    p[0] = nodos.Program(p[1])


def p_declaration_list1(p):
    """declaration_list : declaration_list declaration"""
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
    p[0] = [p[1]]


def p_declaration1(p):
    """declaration : var_declaration"""
    p[0] = p[1]


def p_declaration2(p):
    """declaration : fun_declaration"""
    p[0] = p[1]


def p_var_declaration1(p):
    """var_declaration : type_specifier ID PUNTOC"""
    p[0] = nodos.VarDeclaration(p[1], p[2])


def p_var_declaration2(p):
    """var_declaration : type_specifier ID ICORCH NUM DCORCH PUNTOC"""
    p[0] = nodos.VarDeclaration(p[1], p[2], p[4])


def p_type_specifier1(p):
    """type_specifier : INT"""
    p[0] = p[1]


def p_type_specifier2(p):
    """type_specifier : VOID"""
    p[0] = p[1]


def p_fun_declaration(p):
    """fun_declaration : type_specifier ID IPAREN params DPAREN compound_stmt"""
    p[0] = nodos.FunDeclaration(p[1], p[2], p[4], p[6])


def p_params1(p):
    """params : param_list"""
    p[0] = p[1]


def p_params2(p):
    """params : VOID"""
    pass


def p_param_list1(p):
    """paramList : paramList COMA param"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_param_list2(p):
    """param_list : param"""
    p[0] = p[1]


def p_param1(p):
    """param : type_specifier ID"""
    p[0] = nodos.Param(p[1], p[2], False)


def p_param2(p):
    """param : type_specifier ID ICORCH DCORCH"""
    p[0] = nodos.Param(p[1], p[2], True)


def p_compound_stmt(p):
    """compound_stmt : ILLAVE local_declarations statement_list DLLAVE"""
    p[0] = nodos.CompoundStmt(p[1], p[2])


def p_local_declarations1(p):
    """local_declarations : local_declarations var_declaration"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_local_declarations_empty(p):
    """local_declarations :  empty"""
    p[0] = nodos.Null()


def p_statement_list1(p):
    """statement_list : statement_list statement"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


def p_statement_list_empty(p):
    """statement_list : empty"""
    p[0] = nodos.Null()


def p_statement1(p):
    """statement : expression_stmt"""
    p[0] = p[1]


def p_statement2(p):
    """statement : compound_stmt"""
    p[0] = p[1]


def p_statement3(p):
    """statement : selection_stmt"""
    p[0] = p[1]


def p_statement4(p):
    """statement : iteration_stmt"""
    p[0] = p[1]


def p_statement5(p):
    """statement : return_stmt"""
    p[0] = p[1]


def p_expression_stmt1(p):
    """expression_stmt : expression PUNTOC"""
    #p[0] = p[1]
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]




def p_expression_stmt2(p):
    """expression_stmt : PUNTOC"""
    pass


def p_selection_stmt1(p):
    """selection_stmt : IF IPAREN expression DPAREN statement"""
    #p[0] = nodos.SelectionStmt(p[1], p[3], p[5])
    if isinstance(p[1], list):
        p[0].extend(p[1])
    else:
        p[0].extend([p[1]])

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

    if isinstance(p[5], list):
        p[0].extend(p[5])
    else:
        p[0].extend([p[5]])


def p_selection_stmt2(p):
    """selection_stmt :  IF IPAREN expression DPAREN statement ELSE statement"""
    #p[0] = nodos.SelectionStmt(p[1], p[3], p[5], p[6], p[7])
    if isinstance(p[1], list):
        p[0].extend(p[1])
    else:
        p[0].extend([p[1]])

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

    if isinstance(p[5], list):
        p[0].extend(p[5])
    else:
        p[0].extend([p[5]])

    if isinstance(p[6], list):
        p[0].extend(p[6])
    else:
        p[0].extend([p[6]])

    if isinstance(p[7], list):
        p[0].extend(p[7])
    else:
        p[0].extend([p[7]])


def p_iteration_stmt(p):
    """iterationStmt :  WHILE IPAREN expression DPAREN statement"""
    #p[0] = nodos.iterationStmt(p[1],p[3],p[5])
    if isinstance(p[1], list):
        p[0].extend(p[1])
    else:
        p[0].extend([p[1]])

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

    if isinstance(p[5], list):
        p[0].extend(p[5])
    else:
        p[0].extend([p[5]])


def p_return_stmt1(p):
    """returnStmt :  RETURN PUNTOC"""
    #p[0] = nodos.returnStmt(p[1])
    if isinstance(p[1], list):
        p[0].extend(p[1])
    else:
        p[0].extend([p[1]])


def p_return_stmt2(p):
    """returnStmt :  RETURN expression PUNTOC"""
    #p[0] = nodos.returnStmt(p[1],p[2])
    if isinstance(p[1], list):
        p[0].extend(p[1])
    else:
        p[0].extend([p[1]])

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_expression1(p):
    """expression :  var ASIGN expression"""
    p[0] = nodos.expression1(p[1], p[2], p[3])


def p_expression2(p):
    """expression :  simpleExpression"""
    p[0] = nodos.expression2(p[1])


def p_var1(p):
    """var :  ID"""


def p_var2(p):
    """var :  ID ICORCH expression DCORCH"""


def p_simple_expression1(p):
    """simple_expression :  additive_expression relop additive_expression"""


def p_simple_expression2(p):
    """simple_expression :  additive_expression"""


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


def p_additive_expression1(p):
    """additive_expression : additive_expression addop term"""


def p_additive_expression2(p):
    """additive_expression : term"""


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


def p_args_empty(p):
    """args : empty"""


def p_arg_list1(p):
    """arg_list : arg_list COMA expression"""


def p_arg_list2(p):
    """arg_list : expression"""


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
    visitor = Visitor()
    nodos.Program.accept(result, visitor)
    print(visitor.ast)

