import unittest
import calculator_OOP as c


class TestCalc(unittest.TestCase):

    def test_addition(self):
        data = c.Calc
        data.numbers = [5, 10]
        result = data.addition()
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()