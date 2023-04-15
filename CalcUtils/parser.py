import ply.yacc as yacc
from .lexer import Lexer
from math import factorial


class Parser(object):

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

    tokens = Lexer.tokens
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIV'),
        ('right', 'UMINUS'),
        ('left', 'LPAREN', 'RPAREN')
    )

    def p_expr_uminus(self, p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = -p[2]

    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_mult(self, p):
        'term : term MULT factor'
        p[0] = p[1] * p[3]

    def p_term_div(self, p):
        'term : term DIV factor'
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError as e:
            print(e)  # TODO zero division


    def p_term_sqrt(self, p):
        'term : term SQRT factor'
        p[0] = p[3] ** (1 / p[1])

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input!")
