##
# @package src.CalcUtils.lexer
# lexer.py is a src.CalcUtils helper module that tokenizes string input for mathematical expressions.
#
# It is able to detect lexical error in input such as
# @author Alex Bazo
#
#

import ply.lex as lex


##
# @class Lexer
# main class used for input tokenizing
#
class Lexer(object):
    # all possible tokens
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
    # regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULT = r'\*'
    t_DIV = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_FACT = r'\!'
    t_SQRT = r'\√'
    t_POW = r'\^'
    t_ignore = ' \t'

    def __init__(self):
        """!@brief Lexer class constructor
        """
        self.toks = []
        self.lexer = lex.lex(module=self)

    ##
    # @brief regular expression for numbers (integers and floats)
    # @param t LexToken object
    #
    def t_NUMBER(self, t):
        r"""\d+(?:\.\d+)?"""
        t.value = float(t.value)
        return t

    ##
    # @brief rule that tracks line numbers
    #
    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """!@brief Error handler
        @param t LexToken object
        @return Nothing
        """
        # no sense to continue, clear lexer
        self.clear()

    def fill(self, data):
        """!@brief Helper function that fills lexer class with string for testing in Unittest
        @param data String to tokenize
        @return: Nothing
        """
        self.lexer.input(data)
        try:
            for token in self.lexer:
                self.toks.append(token)
        except lex.LexError:
            self.lexer = None

    def clear(self):
        """!@brief Clears all tokens in lexer
        @return Nothing
        """
        if self.toks is not None:
            self.toks = []

    def get_token_values(self):
        """!@brief Getter function for getting all token values
        @return List of token values
        """
        return [token.value for token in self.toks]

    def get_token_types(self):
        """!@brief Getter function for getting all token types
        @return List of token types
        """
        return [token.type for token in self.toks]

    def print_tokens(self):
        """!@brief Prints all tokens
        @return Nothing
        """
        print([token for token in self.toks])
