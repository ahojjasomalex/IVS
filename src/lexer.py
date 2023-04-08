import ply.lex as lex


class Lexer(object):
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'FACT',
        'SQRT'
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_FACT = r'\!'
    t_SQRT = r'\`'
    t_ignore = ' \t'

    def __init__(self):
        self.lexer = None
        self.build()

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def t_NUMBER(self, t):
        r'\d+(?:\.\d+)?'
        t.value = float(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def fill(self, data):
        self.lexer.input(data)

    def print_tokens(self):
        for token in self.lexer:
            print(token)
