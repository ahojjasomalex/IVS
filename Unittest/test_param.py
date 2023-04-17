import unittest
from CalcUtils.parser import Parser
from parameterized import parameterized

Parser.log = False
Parser.write_tables = True


class ParametrizedTestCase(unittest.TestCase):
    @parameterized.expand([
        ['plus', '+', [x for x in range(11)], [x for x in range(1, 11)]],
        ['minus', '-', [x for x in range(11)], [x for x in range(1, 11)]],
        ['tim', '*', [x for x in range(11)], [x for x in range(1, 11)]],
        ['div', '/', [x for x in range(11)], [x for x in range(1, 11)]]
    ])
    def test_binary_simple(self, name, op, a, b):
        p = Parser()
        for i, j in zip(a, b):
            data = f'{i}{op}{j}'
            res = p.parser.parse(data)
            self.assertEqual(res, eval(data))

    @parameterized.expand([
        ['plus', '+', [x for x in range(11)], [x for x in range(1, 11)]],
        ['minus', '-', [x for x in range(11)], [x for x in range(1, 11)]],
        ['tim', '*', [x for x in range(11)], [x for x in range(1, 11)]],
        ['div', '/', [x for x in range(11)], [x for x in range(1, 11)]]
    ])
    def test_binary_complex(self, name, op, a, b):
        p = Parser()
        for i, j in zip(a, b):
            data = f'{i}{op}{j}{op}{j}{i}{op}{i}.{j}'
            res = p.parser.parse(data)
            self.assertEqual(res, eval(data))


if __name__ == "__main__":
    unittest.main()
