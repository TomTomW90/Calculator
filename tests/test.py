import unittest
from calculator_OOP import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.temp = Calc()

    def test_addition(self):
        self.temp.addition([5, 10])
        self.assertEqual(self.temp, 15)


if __name__ == '__main__':
    unittest.main()
