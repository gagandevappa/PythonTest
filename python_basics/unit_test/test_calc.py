import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-10,5),-5)
        self.assertEqual(calc.add(2,10),12)
        self.assertEqual(calc.add(0,0),0)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(-2,10),-12)
        self.assertEqual(calc.subtract(10,2),8)
        self.assertEqual(calc.subtract(0,2),-2)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(-2,10),-20)
        self.assertEqual(calc.multiply(10,2),20)
        self.assertEqual(calc.multiply(0,2),0)
    
    def test_divide(self):
        with self.assertRaises(ValueError):
            calc.divide(10,0)
        self.assertEqual(calc.divide(10,2),5)
        self.assertEqual(calc.divide(-5,2), -3)
        self.assertEqual(calc.divide(5,2), 2)


if __name__ == "__main__":
    unittest.main()