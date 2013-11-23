#tests for forecast error
import unittest
import os
import sys
sys.path.append(os.path.join('..'))
from errors import ErrorMethods
	
#run tests with python -m unittest -v error_tests

class TestError(unittest.TestCase):

	def setUp(self):
		self.tester = ErrorMethods()
		self.actuals = [10,9,20,40,30,100,10,7,13,20]
		self.forecast = [10,10,18,35,40,90,20,11,7,32]
		self.n = len(self.forecast)

	def test_error(self):
		result = [0,-1,2,5,-10,10,-10,-4,6,-12]
		self.assertEqual(result,self.tester.error(self.actuals,self.forecast))

	def test_abs_error(self):
		result = [0,1,2,5,10,10,10,4,6,12]
		self.assertEqual(result,self.tester.abs_error(self.actuals,self.forecast))

	def test_abs_percent_error(self):
		result = [0,11.1,10,12.5,33.3,10,100,57.1,46.2,60]
		self.assertEqual(result,self.tester.abs_percent_error(self.actuals,self.forecast))

	def test_mae(self):
		pass

	def test_mape(self):
		result = [0,1.1,2.1,3.4,6.7,7.7,17.7,23.4,28.0,34.0]
		self.assertEqual(result,self.tester.mape(self.actuals,self.forecast))

	def test_wape(self):
		result = [0,5.3,7.7,10.1,16.5,13.4,17.4,18.6,20.1,23.2]
		self.assertEqual(result,self.tester.wape(self.actuals,self.forecast))


if __name__ == '__main__':
    unittest.main()
