import unittest
from ivs_math import Operations


class MyTestCase(unittest.TestCase):

    def test_add(self):
        op = Operations()
        a = 1
        b = 2
        op.add(a, b)
        op.calc()

        self.assertEqual(a + b, op.callstack[0])  # add assertion here


if __name__ == '__main__':
    unittest.main()
