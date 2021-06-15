import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(calc.add(10,'@'),'fail')

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(10,0),'fail')
        print("divide2")

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)




if __name__ == '__main__':
    unittest.main()
#python -m unittest test.py
#coverage run -m unittest test.py
#coverage html
