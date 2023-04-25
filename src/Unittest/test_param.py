##
# @package src.Unittest.test_param
# test_param.py contains parametrized tests for src.CalcUtils.parser module
#

import unittest
from parser import Parser
from parameterized import parameterized

# Setting up Parser class variables for testing
Parser.log = False
Parser.write_tables = False
Parser.optimize = True


##
# @class ParametrizedTestCase
# TestCase class parametrized tests for Parser
#
class ParametrizedTestCase(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def tearDown(self):
        del self.p

    @parameterized.expand([
        ['plus', '+', [x for x in range(11)], [x for x in range(1, 11)]],
        ['minus', '-', [x for x in range(11)], [x for x in range(1, 11)]],
        ['mult', '*', [x for x in range(11)], [x for x in range(1, 11)]],
        ['div', '/', [x for x in range(11)], [x for x in range(1, 11)]]
    ])
    def test_binary_simple(self, name, op, a, b):
        for i, j in zip(a, b):
            data = f'{i}{op}{j}'
            res = self.p.parser.parse(data)
            self.assertEqual(res, eval(data))

    @parameterized.expand([
        ['plus', '+', [x for x in range(11)], [x for x in range(1, 11)]],
        ['minus', '-', [x for x in range(11)], [x for x in range(1, 11)]],
        ['mult', '*', [x for x in range(11)], [x for x in range(1, 11)]],
        ['div', '/', [x for x in range(11)], [x for x in range(1, 11)]]
    ])
    def test_binary_complex(self, name, op, a, b):
        for i, j in zip(a, b):
            data = f'{i}{op}{j}{op}{j}{i}{op}{i}.{j}'
            res = self.p.parser.parse(data)
            self.assertEqual(res, eval(data))


if __name__ == "__main__":
    unittest.main()
