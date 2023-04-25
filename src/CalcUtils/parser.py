import functools
import ply.yacc as yacc
from lexer import Lexer
from math import factorial
import logging

# logging.basicConfig(filename='logger.log', level=logging.DEBUG)


def logger(level=logging.DEBUG):
    """! Decorator factory for logging
    :param level: Logging level
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, p):
            if self.__class__.log:
                logging.info(f"Entering func {func.__name__}")
            result = func(self, p)
            if self.__class__.log:
                _p = []
                for x in p.slice:
                    _p.append(x.value)
                logging.debug(f'{*_p,}')

            return result

        return wrapper

    return decorator


class Parser(object):
    tokens = Lexer.tokens
    log = False
    write_tables = True
    optimize = True

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self, debug=False, write_tables=Parser.write_tables, optimize=Parser.optimize)

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIV'),
        ('right', 'UMINUS'),
        ('left', 'POW', 'SQRT'),
        ('left', 'LPAREN', 'RPAREN', 'FACT')

    )

    # @logger()
    def p_expr_uminus(self, p):
        """expression : MINUS expression %prec UMINUS"""
        p[0] = -p[2]

    # @logger()
    def p_expression_plus(self, p):
        """expression : expression PLUS term"""
        p[0] = p[1] + p[3]

    # @logger()
    def p_expression_minus(self, p):
        """expression : expression MINUS term"""
        p[0] = p[1] - p[3]

    # @logger()
    def p_expression_term(self, p):
        """expression : term"""
        p[0] = p[1]

    # @logger()
    def p_term_mult(self, p):
        """term : term MULT factor"""
        p[0] = p[1] * p[3]

    # @logger()
    def p_term_div(self, p):
        """term : term DIV factor"""
        p[0] = p[1] / p[3]

    # @logger()
    def p_factor_sqrt(self, p):
        """factor : factor SQRT factor"""
        if p[3] < 0:  # number is negative
            if p[1] % 2 == 0:  # base is even -> error
                p[0] = None
                raise ValueError
            if p[1] % 2 != 0:  # base is not even
                if p[1].is_integer():  # number is integer, save '-' operator
                    p[0] = - round(abs(p[3] ** (1 / p[1])), 10)
                else:
                    p[0] = round(abs(p[3] ** (1 / p[1])), 10)
        else:
            p[0] = p[3] ** (1 / p[1])

    # @logger()
    def p_factor_pow(self, p):
        """factor : factor POW factor"""
        p[0] = p[1] ** p[3]

    # @logger()
    def p_term_fact(self, p):
        """factor : term FACT
                  | NUMBER FACT"""
        to_fact = p[1]
        if to_fact.is_integer():
            p[0] = float(factorial(int(p[1])))
        else:
            # print(f"{to_fact} is not an integer", file=sys.stderr)
            p[0] = None
            raise FloatingPointError

    # @logger()
    def p_term_factor(self, p):
        """term : factor"""
        p[0] = p[1]

    # @logger()
    def p_factor_num(self, p):
        """factor : NUMBER"""
        p[0] = p[1]

    # @logger()
    def p_factor_expr(self, p):
        """factor : LPAREN expression RPAREN"""
        p[0] = p[2]

    def p_error(self, p):
        if not p:
            raise SyntaxError

        while True:
            tok = self.parser.token()
            if not tok:
                break
        self.parser.restart()

        raise SyntaxError
