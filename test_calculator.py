import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0, 2), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(0, 2), 0)

if __name__ == '__main__':
    unittest.main()
