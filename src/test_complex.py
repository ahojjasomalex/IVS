##
# @package src.test_complex
# test_complex.py contains complex tests for src.CalcUtils.parser module
# @authors Alex Bazo, Richard Jurica, Jan Kroutil
#


import unittest
from CalcUtils.parser import Parser
from parameterized import parameterized

Parser.log = False
Parser.write_tables = False
Parser.optimize = True


##
# @class ParserComplexTestCase
# TestCase class for complex tests for Parser
#
class ParserComplexTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    def test_parser_add_sub_mult_div_1(self):
        data = '5+2-6*3/6'
        self.assertEqual(self.p.parser.parse(data), 4)

    def test_parser_add_sub_mult_div_2(self):
        data = '100*100/100+4/2'
        self.assertEqual(self.p.parser.parse(data), 102)

    def test_parser_add_sub_mult_div_3(self):
        data = '42/3*8-7/10'
        self.assertEqual(self.p.parser.parse(data), 111.3)

    def test_parser_zero_div(self):
        data = '2/(2-2)'
        try:
            res = self.p.parser.parse(data)
        except ZeroDivisionError:
            res = None
        self.assertEqual(res, None)

    def test_op_precedence_1(self):
        data = '3+3*3'
        self.assertEqual(self.p.parser.parse(data), 12)

    def test_op_precedence_2(self):
        data = '3+3/3'
        self.assertEqual(self.p.parser.parse(data), 4)

    def test_op_precedence_3(self):
        data = '2^4*2√16'
        self.assertEqual(self.p.parser.parse(data), 64)

    def test_op_precedence_4(self):
        data = '2^4*(2√16)'
        self.assertEqual(self.p.parser.parse(data), 64)

    def test_frenzy_1(self):
        data = '3+3*3+(6-1)!/8+2^4/(2√16)+4!-3*5+2'
        self.assertEqual(self.p.parser.parse(data), 42)

    def test_negative_sqrt1(self):
        data = '(-4)√(16)'
        self.assertEqual(self.p.parser.parse(data), 1/2)

    def test_negative_sqrt2(self):
        data = '(-3)√(27)'
        self.assertEqual(round(self.p.parser.parse(data), 10), round(1/3, 10))

    def test_sqrt_decimals(self):
        data = '2.1√(-27)'
        self.assertEqual(round(self.p.parser.parse(data), 9), 4.803986657)

##
# @class ParserAssociativityTestCase
# TestCase class for operation associativity tests for Parser
#
class ParserAssociativityTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    @parameterized.expand([
        ['plus', ['1+2+3', '3+2+1', '2+1+3', '3+1+2'], [6] * 4],
        ['minus', ['1-2-3', '3-2-1', '2-1-3', '3-1-2'], [-4, 0, -2, 0]],
        ['mult', ['1*2*4*3', '3*4*2*1', '4*2*1*3', '3*1*2*4'], [24] * 4],
        ['div', ['1/2/4/3', '3/4/2/1', '4/2/1/3', '3/1/2/4'],
         [eval('1/2/4/3'), eval('3/4/2/1'), eval('4/2/1/3'), eval('3/1/2/4')]]
    ])
    def test_asoc(self, name, data, res):
        for d, r in zip(data, res):
            p_res = self.p.parser.parse(d)
            self.assertEqual(p_res, r)


if __name__ == "__main__":
    unittest.main()
