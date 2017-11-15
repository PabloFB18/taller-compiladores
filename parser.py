import ply.yacc as yacc

# Obtener tokens del scanner
from __builtin__ import raw_input

from scanner import tokens


precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVI'),
    ('right','ID','NUM'),
    ('left', 'DPAREN','IPAREN')
)


def p_program(p):
    """program : declarationList"""
    #p[0] = program(p[1],'program')

def p_declarationList1(p):
    """declarationList : declarationList declaration"""

def p_declarationList2(p):
    """declarationList : declaration"""

def p_declaration1(p):
    """declaration : varDeclaration"""

def p_declaration2(p):
    """declaration : funDeclaration"""

def p_varDeclaration1(p):
    """varDeclaration : typeSpecifer ID PUNTOC"""

def p_varDeclaration2(p):
    """varDeclaration : typeSpecifer ID ICORCH NUM DCORCH PUNTOC"""

def p_typeSpecifier1(p):
    """typeSpecifer : INT"""

def p_typeSpecifier2(p):
    """typeSpecifer : VOID"""

def p_funDeclaration(p):
    """funDeclaration : typeSpecifer ID IPAREN NUM DPAREN compoundStmt"""

def p_params1(p):
    """params : paramList"""

def p_params2(p):
    """params : VOID"""

def p_paramList1(p):
    """paramList : paramList COMA param"""

def p_paramList2(p):
    """paramList : param"""

def p_param1(p):
    """param : typeSpecifier ID"""

def p_param2(p):
    """param : typeSpecifier ID ICORCH DCORCH"""

def p_compoundStmt(p):
    """compoundStmt : ILLAVE localDeclarations statementList DLLAVE"""

def p_localDeclarations1(p):
    """localDeclarations : localDeclarations varDeclarations"""

def p_localDeclarations2(p):
    """localDeclarations :  empty"""

def p_statementList1(p):
    """statementList : statementList statement"""

def p_statementList2(p):
    """statementList : empty"""

def p_statement1(p):
    """statement : expressionStmt"""

def p_statement2(p):
    """statement : compoundStmt"""

def p_statement3(p):
    """statement : selectionStmt"""

def p_statement4(p):
    """statement : iterationStmt"""

def p_statement5(p):
    """statement : returnStmt"""

def p_expressionStmt1(p):
    """expressionStmt : statementList statement PUNTOC"""

def p_expressionStmt2(p):
    """expressionStmt : PUNTOC"""

def p_selectionStmt1(p):
    """selectionStmt : IF IPAREN expression DPAREN statement"""

def p_selectionStmt2(p):
    """selectionStmt :  IF IPAREN expression DPAREN statement ELSE statement"""

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

def P_additiveExpression1(p):
    """additiveExpression : additiveExpression addop term"""

def P_additiveExpression2(p):
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

def p_args2(p):
    """args : empty"""

def p_argList1(p):
    """argsList : argList COMA expression"""

def p_argList2(p):
    """argsList : expression"""




# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

