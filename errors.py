#http://docs.python.org/2/library/operator.html
import numpy as np

class ErrorMethods:

	def error(self,a,b):
		return [x-y for x,y in zip(a, b)]

	def abs_error(self,a,b):
		return [abs(x-y) for x,y in zip(a, b)]

	def abs_percent_error(self,a,b):
		return [round(100*float(abs(x-y))/x,1) for x,y in zip(a, b)]

	def mae(self,a,b):
		pass

	def mape(self,a,b):
		abs_error_local = [abs(x-y)/x for x,y in zip(a, b)]
		sum_abs_error_local = np.cumsum(abs_error_local)
		return [round(float(i/len(a))*100,1) for i in sum_abs_error_local]

	def wape(self,a,b):
		abs_error_local = [abs(x-y) for x,y in zip(a, b)]
		sum_abs_error_local = np.cumsum(abs_error_local)
		sum_actuals = np.cumsum(a)
		return [round(float(x/y) * 100,1)for x,y in zip(sum_abs_error_local,sum_actuals)]


	
