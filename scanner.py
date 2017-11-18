from ply import lex
import io

reserved = {
    'ELSE': 'ELSE',
    'IF': 'IF',
    'INT': 'INT',
    'VOID': 'VOID',
    'RETURN': 'RETURN',
    'WHILE': 'WHILE'
}

tokens = [
            'SUMA',
            'RESTA',
            'MULTI',
            'DIVI',
            'MENOR',
            'MENORI',
            'MAYOR',
            'MAYORI',
            'IGUAL',
            'DIST',
            'ASIGN',
            'IPAREN',
            'DPAREN',
            'ICORCH',
            'DCORCH',
            'ILLAVE',
            'DLLAVE',
            'COMA',
            'PUNTOC',
            'NUM',
            'ID',
            'RESERVED'
         ] + list(reserved.values())

# operadores
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'\/'
t_MENOR = r'<'
t_MENORI = r'<='
t_MAYOR = r'>'
t_MAYORI = r'>='
t_IGUAL = r'=='
t_DIST = r'<>'

# asignacion
t_ASIGN = r'\='

# delimitadores
t_IPAREN = r'\('
t_DPAREN = r'\)'
t_ICORCH = r'\['
t_DCORCH = r'\]'
t_ILLAVE = r'\{'
t_DLLAVE = r'\}'
t_COMA = r','
t_PUNTOC = r'\;'

# tokens ignorados
t_ignore = ' \t\n'


# nueva linea
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# identificadores
def t_ID(t):
    r'[eE][lL][sS]E|[iI]F|[iI][nN]T|[vV][oO][iI]D|[rR][eE][tT][uU][rR]N|[wW][hH][iI][lL]E|([A-Za-z]+(_[A-Za-z]+)*_?([a-z]|[0-9]+))|[a-z]'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t


# numero
def t_NUM(t):
    r'0[0-9]|[1-9][0-9]+'
    return t


# comentario multilinea
def t_comentMult(t):
    r'<\/(.|\n)*?\/>'
    t.lexer.lineno += t.value.count('\n')


# comentario de una linea
def t_coment(t):
    r'(\?|\!).*'


# error
def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    errors_lexer.write("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno) + '\n')
    # tratamiento de errores
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()

errors_lexer = open('errors_lexer.txt', 'w')

# out1 = open('scanner-exmples/out1.txt', 'w')
# with open('scanner-exmples/sample1.txt', 'r') as arch1:
#     contents = arch1.read()
#     lex.input(contents)
#     print('\n sample1')
#     for tok in iter(lex.token, None):
#         print(repr(tok.type), repr(tok.value))
#         out1.write(repr(tok.type))
#         out1.write(repr(tok.value)+'\n')
#
# out1 = open('scanner-exmples/out2.txt', 'w')
# with open('scanner-exmples/sample2.txt', 'r') as arch1:
#     contents = arch1.read()
#     lex.input(contents)
#     print('\n sample2')
#     for tok in iter(lex.token, None):
#         print(repr(tok.type), repr(tok.value))
#         out1.write(repr(tok.type))
#         out1.write(repr(tok.value)+'\n')
#
# out1 = open('scanner-exmples/out3.txt', 'w')
# with open('scanner-exmples/sample3.txt', 'r') as arch1:
#     contents = arch1.read()
#     lex.input(contents)
#     print('\n sample3')
#     for tok in iter(lex.token, None):
#         print(repr(tok.type), repr(tok.value))
#         out1.write(repr(tok.type))
#         out1.write(repr(tok.value)+'\n')
#
# out1 = open('scanner-exmples/out4.txt', 'w')
# with open('scanner-exmples/sample4.txt', 'r') as arch1:
#     contents = arch1.read()
#     lex.input(contents)
#     print('\n sample4')
#     for tok in iter(lex.token, None):
#         print(repr(tok.type), repr(tok.value))
#         out1.write(repr(tok.type))
#         out1.write(repr(tok.value)+'\n')
#
# out1 = io.open('scanner-exmples/out5.txt', 'w', encoding='utf8', errors="ignore")
# with open('scanner-exmples/sample5.txt', 'r') as arch1:
#     contents = arch1.read()
#     lex.input(contents)
#     print('\n sample5')
#     for tok in iter(lex.token, None):
#         print(repr(tok.type), repr(tok.value))
#         out1.write(repr(tok.type))
#         out1.write(repr(tok.value)+'\n')
