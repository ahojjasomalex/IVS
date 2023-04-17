import sys

import ply.lex
import ply.lex as lex


class Lexer(object):
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'MULT',
        'DIV',
        'LPAREN',
        'RPAREN',
        'FACT',
        'SQRT',
        'POW'
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULT = r'\*'
    t_DIV = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_FACT = r'\!'
    t_SQRT = r'\`'
    t_POW = r'\^'
    t_ignore = ' \t'

    def __init__(self):
        self.toks = []
        self.lexer = lex.lex(module=self)

    def t_NUMBER(self, t):
        r"""\d+(?:\.\d+)?"""
        t.value = float(t.value)
        return t

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        # print(f"Illegal character '{t.value[0]}'", file=sys.stderr)
        self.clear()

    def fill(self, data):
        self.lexer.input(data)
        try:
            for token in self.lexer:
                self.toks.append(token)
        except ply.lex.LexError:
            self.lexer = None

    def clear(self):
        if self.toks is not None:
            self.toks = []

    def get_tokens(self):
        return self.toks

    def get_token_values(self):
        return [token.value for token in self.toks]

    def get_token_types(self):
        return [token.type for token in self.toks]

    def print_tokens(self):
        print([token for token in self.toks])
