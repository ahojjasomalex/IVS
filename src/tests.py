import unittest
from ivs_math import Operations
from lexer import Lexer


class MyTestCase(unittest.TestCase):

    def test_add(self):
        op = Operations()
        a = 1
        b = 2
        op.add(a, b)
        op.calc()

        self.assertEqual(a + b, op.callstack[0])  # add assertion here


class LexerSimpleTestCase(unittest.TestCase):
    def test_simple_add(self):
        l = Lexer()
        data = '5+5'
        l.fill(data)
        token_values = l.get_token_values()
        l.fill(data)
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '+', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'PLUS', 'NUMBER'])

    def test_simple_sub(self):
        l = Lexer()
        data = '5-5'
        l.fill(data)
        token_values = l.get_token_values()
        l.fill(data)
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '-', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MINUS', 'NUMBER'])

    def test_simple_mult(self):
        l = Lexer()
        data = '5*5'
        l.fill(data)
        token_values = l.get_token_values()
        l.fill(data)
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '*', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'MULT', 'NUMBER'])

    def test_simple_div(self):
        l = Lexer()
        data = '5/5'
        l.fill(data)
        token_values = l.get_token_values()
        l.fill(data)
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '/', 5.0])
        self.assertEqual(token_types, ['NUMBER', 'DIV', 'NUMBER'])

    def test_simple_fact(self):
        l = Lexer()
        data = '5!'
        l.fill(data)
        token_values = l.get_token_values()
        l.fill(data)
        token_types = l.get_token_types()

        self.assertEqual(token_values, [5.0, '!'])
        self.assertEqual(token_types, ['NUMBER', 'FACT'])


if __name__ == '__main__':
    unittest.main()
