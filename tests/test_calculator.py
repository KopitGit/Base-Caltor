import unittest
from backend.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.perform_operation('add', 2, 3), 5)
        self.assertEqual(self.calc.perform_operation('add', 2, 5), 7)
    
    def test_subtract(self):
        self.assertEqual(self.calc.perform_operation('subtract', 5, 2), 3)
    
    def test_multiply(self):
        self.assertEqual(self.calc.perform_operation('multiply', 3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(self.calc.perform_operation('divide', 10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.perform_operation('divide', 10, 0)
    
    def test_square(self):
        self.assertEqual(self.calc.perform_operation('square', 4), 16)
    
    def test_sqrt(self):
        self.assertEqual(self.calc.perform_operation('sqrt', 9), 3)
        with self.assertRaises(ValueError):
            self.calc.perform_operation('sqrt', -1)
    
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.calc.perform_operation('invalid', 1)




if __name__ == '__main__':
    unittest.main()