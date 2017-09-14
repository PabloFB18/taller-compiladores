reserved = {
    'else': '(?i)else',
    'if': '(?i)if',
    'int': '(?i)int',
    'void': '(?i)void',
    'return': '(?i)return',
    'while': '(?i)while'
}

tokens = [
            'SUMA',
            'RESTA',
            'MULTI'
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
            'RESERVED'
         ] + list(reserved.values())

# operadores
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_MENOR = r'<'
t_MENORI = r'<='
t_MAYOR = r'>'
t_MAYORI = r'>='
t_IGUAL = r'=='
t_DIST = r'!='

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
t_PUNTOC = r'\.'

# tokens ignorados
t_ignore = ' \t\n'

# nueva linea
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# palabra reservada
def t_RESERVED(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value,'RESERVED')    # chequear palabras reservadas
    return t

# identificadores
def t_ID(t):
    r'[A-Za-z]+(_[A-Za-z]+)*_?([a-z]|[0-9]+)'
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

