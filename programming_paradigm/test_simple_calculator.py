import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertNotEqual(self.calc.add(10, 2), 14)
        with self.assertRaises(NameError):
            self.calc.add(undefined_input, 3)

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 30), -10)
        with self.assertRaises(TypeError):
            self.calc.subtract("string", 5)

    def test_multiplication(self):
        '''Test multiplication method'''
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        with self.assertRaises(TypeError):
            self.calc.multiply("string", 5)

    def test_division(self):
        '''Test the division method'''
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertNotEqual(self.calc.divide(2, 2), 0)