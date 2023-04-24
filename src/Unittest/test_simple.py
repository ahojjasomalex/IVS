import unittest

import ply.lex

from lexer import Lexer
from parser import Parser

Parser.log = False
Parser.write_tables = False
Parser.optimize = True


class LexerSimpleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.l = Lexer()
        
    def tearDown(self):
        del self.l    

    def test_simple_add(self):
        data = '5+5'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [5.0, '+', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'PLUS', 'NUMBER'])

    def test_simple_sub(self):
        data = '5-5'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [5.0, '-', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MINUS', 'NUMBER'])

    def test_simple_mult(self):
        data = '5*5'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [5.0, '*', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MULT', 'NUMBER'])

    def test_simple_div(self):
        data = '5/5'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [5.0, '/', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'DIV', 'NUMBER'])

    def test_simple_fact(self):
        data = '5!'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [5.0, '!'])
        self.assertEqual(token_types, ['NUMBER', 'FACT'])


class LexerSimpleBadInputTestCase(unittest.TestCase):

    def setUp(self):
        self.l = Lexer()

    def tearDown(self):
        del self.l

    def test_simple_badchars(self):
        data = 'aghsfdajhoiaowudiandasd0721'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [])
        self.assertEqual(token_types, [])

    def test_simple_good_bad_chars(self):
        data = '1+1-1+2aghsfdajhoiaowudiandasd0721'
        self.l.fill(data)
        token_values = self.l.get_token_values()
        token_types = self.l.get_token_types()

        self.assertEqual(token_values, [])
        self.assertEqual(token_types, [])


class ParserSimpleTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    def test_simple_add(self):
        data = '3+3'
        res = self.p.parser.parse(data)
        self.assertEqual(res, 6.0)

    def test_simple_sub(self):
        data = '3-2'
        self.assertEqual(self.p.parser.parse(data), 1.0)

    def test_simple_sub_neg(self):
        data = '2-3'
        self.assertEqual(self.p.parser.parse(data), -1.0)

    def test_simple_mult(self):
        data = '3*3'
        self.assertEqual(self.p.parser.parse(data), 9.0)

    def test_simple_div(self):
        data = '3/3'
        self.assertEqual(self.p.parser.parse(data), 1.0)

    def test_simple_sqrt(self):
        data = '3√27'
        self.assertEqual(self.p.parser.parse(data), 3.0)

    def test_simple_sqrt_neg(self):
        data = '3√(-27)'
        self.assertEqual(self.p.parser.parse(data), None)

    def test_simple_pow(self):
        data = '3^3'
        self.assertEqual(self.p.parser.parse(data), 27.0)

    def test_simple_fact(self):
        data = '5!'
        self.assertEqual(self.p.parser.parse(data), 120.0)

    def test_simple_fact_2(self):
        data = '5.5!'
        try:
            res = self.p.parser.parse(data)
        except FloatingPointError:
            res = None
        self.assertEqual(res, None)

    def test_simple_fact_3(self):
        data = '(2+3)!'
        self.assertEqual(self.p.parser.parse(data), 120.0)

    def test_simple_neg_nums(self):
        data = '-2+(-3)'
        self.assertEqual(self.p.parser.parse(data), -5.0)

    def test_simple_neg_paren(self):
        data = '-(2+5)'
        self.assertEqual(self.p.parser.parse(data), -7.0)


class ParserSimpleBadInputsTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    def test_simple_bad_add(self):
        data = '.3+3'
        try:
            res = self.p.parser.parse(data)
        except ply.lex.LexError:
            res = None
        self.assertEqual(res, None)

    def test_simple_empty(self):
        data = ''
        try:
            res = self.p.parser.parse(data)
        except SyntaxError:
            res = None
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
