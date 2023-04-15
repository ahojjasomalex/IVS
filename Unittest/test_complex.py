import unittest
from CalcUtils.parser import Parser


class ParserComplexTestCase(unittest.TestCase):
    def test_parser_add_sub_mult_div_1(self):
        p = Parser()
        data = '5+2-6*3/6'
        res = p.parser.parse(data)
        self.assertEqual(res, 4.0)

    def test_parser_add_sub_mult_div_2(self):
        p = Parser()
        data = '100*100/100+4/2'
        res = p.parser.parse(data)
        self.assertEqual(res, 102.0)

    def test_parser_add_sub_mult_div_3(self):
        p = Parser()
        data = '42/3*8-7/10'
        res = p.parser.parse(data)
        self.assertEqual(res, 111.3)

    def test_parser_add_sub_mult_div_4(self):
        p = Parser()
        data = '2/0'
        res = p.parser.parse(data)
        self.assertEqual(res, None)


if __name__ == "__main__":
    unittest.main()
