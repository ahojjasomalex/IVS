import unittest
from CalcUtils.lexer import Lexer
from CalcUtils.parser import Parser


class LexerSimpleTestCase(unittest.TestCase):

    def test_simple_add(self):
        l = Lexer()
        data = '5+5'
        l.fill(data)
        token_values = l.get_token_values()
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '+', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'PLUS', 'NUMBER'])

    def test_simple_sub(self):
        l = Lexer()
        data = '5-5'
        l.fill(data)
        token_values = l.get_token_values()
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '-', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MINUS', 'NUMBER'])

    def test_simple_mult(self):
        l = Lexer()
        data = '5*5'
        l.fill(data)
        token_values = l.get_token_values()
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '*', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MULT', 'NUMBER'])

    def test_simple_div(self):
        l = Lexer()
        data = '5/5'
        l.fill(data)
        token_values = l.get_token_values()
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '/', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'DIV', 'NUMBER'])

    def test_simple_fact(self):
        l = Lexer()
        data = '5!'
        l.fill(data)
        token_values = l.get_token_values()
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '!'])
        self.assertEqual(token_types, ['NUMBER', 'FACT'])


class ParserSimpleTestCase(unittest.TestCase):
    def test_simple_add(self):
        p = Parser()
        data = '3+3'
        res = p.parser.parse(data)
        self.assertEqual(res, 6.0)

    def test_simple_sub(self):
        p = Parser()
        data = '3-2'
        res = p.parser.parse(data)
        self.assertEqual(res, 1.0)

    def test_simple_sub_neg(self):
        p = Parser()
        data = '2-3'
        res = p.parser.parse(data)
        self.assertEqual(res, -1.0)

    def test_simple_mult(self):
        p = Parser()
        data = '3*3'
        res = p.parser.parse(data)
        self.assertEqual(res, 9.0)

    def test_simple_div(self):
        p = Parser()
        data = '3/3'
        res = p.parser.parse(data)
        self.assertEqual(res, 1.0)

    def test_simple_sqrt(self):
        p = Parser()
        data = '3`27'
        res = p.parser.parse(data)
        self.assertEqual(res, 3.0)

    def test_simple_pow(self):
        p = Parser()
        data = '3^3'
        res = p.parser.parse(data)
        self.assertEqual(res, 27.0)

    def test_simple_fact(self):
        p = Parser()
        data = '5!'
        res = p.parser.parse(data)
        self.assertEqual(res, 120.0)

    def test_simple_fact_2(self):
        p = Parser()
        data = '5.5!'
        res = p.parser.parse(data)
        self.assertEqual(res, None)

    def test_simple_fact_3(self):
        p = Parser()
        data = '(2+3)!'
        res = p.parser.parse(data)
        self.assertEqual(res, 120.0)

    def test_simple_neg_nums(self):
        p = Parser()
        data = '-2+(-3)'
        res = p.parser.parse(data)
        self.assertEqual(res, -5.0)


if __name__ == '__main__':
    unittest.main()
