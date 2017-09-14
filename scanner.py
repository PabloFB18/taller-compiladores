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
            'ID'
         ] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUMA = r'\+'