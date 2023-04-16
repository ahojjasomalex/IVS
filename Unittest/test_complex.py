import unittest
from CalcUtils.parser import Parser


class ParserComplexTestCase(unittest.TestCase):
    def test_parser_add_sub_mult_div_1(self):
        p = Parser()
        data = '5+2-6*3/6'
        res = p.parser.parse(data)
        self.assertEqual(res, 4)

    def test_parser_add_sub_mult_div_2(self):
        p = Parser()
        data = '100*100/100+4/2'
        res = p.parser.parse(data)
        self.assertEqual(res, 102)

    def test_parser_add_sub_mult_div_3(self):
        p = Parser()
        data = '42/3*8-7/10'
        res = p.parser.parse(data)
        self.assertEqual(res, 111.3)

    def test_parser_zero_div(self):
        p = Parser()
        data = '2/(2-2)'
        res = p.parser.parse(data)
        self.assertEqual(res, None)

    def test_op_precedence_1(self):
        p = Parser()
        data = '3+3*3'
        res = p.parser.parse(data)
        self.assertEqual(res, 12)

    def test_op_precedence_2(self):
        p = Parser()
        data = '3+3/3'
        res = p.parser.parse(data)
        self.assertEqual(res, 4)

    def test_op_precedence_3(self):
        p = Parser()
        data = '2^4*2`16'
        res = p.parser.parse(data)
        self.assertEqual(res, 1.0905077326652577)

    def test_op_precedence_4(self):
        p = Parser()
        data = '2^4*(2`16)'
        res = p.parser.parse(data)
        self.assertEqual(res, 64)

    def test_frenzy_1(self):
        p = Parser()
        data = '3+3*3+(6-1)!/8+2^4/(2`16)+4!-3*5+2'
        res = p.parser.parse(data)
        self.assertEqual(res, 42)


if __name__ == "__main__":
    unittest.main()
