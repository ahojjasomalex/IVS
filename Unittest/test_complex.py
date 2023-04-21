import unittest
from CalcUtils.parser import Parser

Parser.log = False
Parser.write_tables = True
Parser.optimize = True


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
        data = '2^4*2`16'
        self.assertEqual(self.p.parser.parse(data), 1.0905077326652577)

    def test_op_precedence_4(self):
        data = '2^4*(2`16)'
        self.assertEqual(self.p.parser.parse(data), 64)

    def test_frenzy_1(self):
        data = '3+3*3+(6-1)!/8+2^4/(2`16)+4!-3*5+2'
        self.assertEqual(self.p.parser.parse(data), 42)


if __name__ == "__main__":
    unittest.main()
