#Time Series - common error checking formulas
#Note: Runs in python3, requires numpy
import numpy as np

class ErrorMethods:

	#simple error checking: actuals - forecast
	def error(self,a,b):
		return [x-y for x,y in zip(a, b)]

	#absolute error checking: abs(actuals - forecast)
	def abs_error(self,a,b):
		return [abs(x-y) for x,y in zip(a, b)]

	#absolute % error
	def abs_percent_error(self,a,b):
		return [round(100*float(abs(x-y))/x,1) for x,y in zip(a, b)]

	#mean average percent error (mape)
	def mape(self,a,b):
		abs_error_local = [abs(x-y)/x for x,y in zip(a, b)]
		sum_abs_error_local = np.cumsum(abs_error_local)
		return [round(float(i/len(a))*100,1) for i in sum_abs_error_local]

	#weighted average percent error (wape)
	def wape(self,a,b):
		abs_error_local = [abs(x-y) for x,y in zip(a, b)]
		sum_abs_error_local = np.cumsum(abs_error_local)
		sum_actuals = np.cumsum(a)
		return [round(float(x/y) * 100,1)for x,y in zip(sum_abs_error_local,sum_actuals)]


	
