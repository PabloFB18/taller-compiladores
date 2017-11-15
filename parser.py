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
    """program : declarationlist"""
    p[0] = p[1]




def p_declarationlist(p):
    """declarationlist : declarationlist declaration
                        | declaration"""

    if len(p) == 2 and p[1]:
        p[0] = {}
        line, stat = p[1]
        p[0][line] = stat
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            line, stat = p[2]
            p[0][line] = stat


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

