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


class ParserSimpleSqrtTestCase(unittest.TestCase):
    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    def test_simple_sqrt_pos_odd_base_pos_n(self):
        data = '3√27'
        self.assertEqual(self.p.parser.parse(data), 3.0)

    def test_simple_sqrt_pos_odd_base_neg_n(self):
        data = '3√(-27)'
        self.assertEqual(self.p.parser.parse(data), -3)

    def test_simple_sqrt_neg_odd_base_pos_n(self):
        data = '(-3)√27'
        self.assertEqual(round(self.p.parser.parse(data), 10), round(1/3, 10))

    def test_simple_sqrt_neg_odd_base_neg_n(self):
        data = '(-3)√(-27)'
        self.assertEqual(round(self.p.parser.parse(data), 10), round(-1/3, 10))

    def test_simple_sqrt_neg__odd_base_pos_n(self):
        data = '-3√27'
        self.assertEqual(self.p.parser.parse(data), -3)

    def test_simple_sqrt_neg__odd_base_neg_n(self):
        data = '-3√(-27)'
        self.assertEqual(self.p.parser.parse(data), 3)

    def test_simple_sqrt_pos_even_base_pos_n(self):
        data = '2√16'
        self.assertEqual(self.p.parser.parse(data), 4)

    def test_simple_sqrt_pos_even_base_neg_n(self):
        data = '2√(-16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, None)

    def test_simple_sqrt_neg_even_base_pos_n(self):
        data = '(-2)√16'
        self.assertEqual(self.p.parser.parse(data), 1/4)

    def test_simple_sqrt_neg_even_base_neg_n(self):
        data = '(-2)√(-16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, None)

    def test_simple_sqrt_neg__even_base_pos_n(self):
        data = '-2√16'
        self.assertEqual(self.p.parser.parse(data), -4)

    def test_simple_sqrt_neg__even_base_neg_n(self):
        data = '-2√(-16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, None)

    def test_simple_sqrt_float_base_pos_n(self):
        data = '2.1√(16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(round(res, 10), 3.7444709698)

    def test_simple_sqrt_float_base_neg_n(self):
        data = '2.1√(-16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, 3.7444709698)

    def test_simple_sqrt_neg_base(self):
        data = '-2√(-16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, None)

    def test_simple_sqrt_neg_base_2(self):
        data = '-2√(16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, -4)

    def test_simple_sqrt_neg_base_3(self):
        data = '(-2)√(16)'
        try:
            res = self.p.parser.parse(data)
        except ValueError:
            res = None
        self.assertEqual(res, 1/4)


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
