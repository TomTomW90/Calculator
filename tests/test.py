import unittest
import calculator_OOP as c


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.temp = c.Calc.addition([5, 10])

    def test_addition(self):
        self.assertEqual(self.temp, 15)


if __name__ == '__main__':
    unittest.main()
