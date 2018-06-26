#
# This example shows 3 different methods to do Monte Carlo simulations:
# 1. Pure Python
# 2. Vectorized Numpy
# 3. Fully Vectorized Numpy
#
from time import time 
from scipy import stats
from math import log, exp, sqrt
import random
import numpy as np

# Define BSM_Call_Value function to calculate European call value according to 
# Black-Scholes equation. We'll use this as benchmark:
def BSM_Call_Value(stockPrice, strikePrice, rate, timeToMature, sigma):
	stockPrice = float(stockPrice)
	strikePrice = float(strikePrice)
	d1 = (log(stockPrice / strikePrice) + (rate + .5 * sigma ** 2) * timeToMature) / (sigma * timeToMature)
	d2 = (log(stockPrice / strikePrice) + (rate - .5 * sigma ** 2) * timeToMature) / (sigma * timeToMature)
	callValue = stockPrice * stats.norm.cdf(d1) - exp(-rate * timeToMature) * strikePrice * stats.norm.cdf(d2)
	return callValue

# A Monte Carlo Simulation using just python built-in list. 
def Pure_Py_MC (stockPrice, strikePrice, rate, timeToMature, sigma, iteration=250000, timeSteps=50, timeit=True):
	random.seed()
	start_time = time()
	delta_t = timeToMature / timeSteps
	# MC is the list consists of all 250000 different paths
	# each path is a list of 50 steps from time_0 to maturity
	# Calculate MC 
	MC = []
	for i in range(iteration):
		path = []
	# Calculate each path:
		for step in range(timeSteps + 1):
			if step:
				z = random.gauss(0.0, 1.0)
				stockPrice_t = path[step - 1] * exp((rate - .5 * sigma ** 2) * delta_t + sigma * sqrt(delta_t) * z)
				path.append(stockPrice_t)
			else:
				path.append(stockPrice)
		MC.append(path)

	# Calculate the Monte Carlo estimator
	callValue = exp(-rate * timeToMature) * sum([max(path[-1] - strikePrice, 0) for path in MC]) / iteration

	# return and print results
	if timeit:
		print 'Run time of Pure Python Monte Carlo Simulation is %5.3f seconds.' %(time() - start_time)
	return callValue	

# A Monte Carlo Simulation using numpy vectorized calculation.
def Vec_MC (stockPrice, strikePrice, rate, timeToMature, sigma, iteration=250000, timeSteps=50, timeit=True):
	np.random.seed()
	delta_t = timeToMature / timeSteps
	start_time = time()
	# Generate a [iteration * timeSteps] sized matrix filled with standard normal distribution
	z = np.random.standard_normal([iteration, timeSteps + 1])
	# Calculate 250000 iterations of different paths of stock movement
	log_stockPrice_t = np.cumsum((rate - .5 * sigma ** 2) * delta_t + sigma * sqrt(delta_t) * z, axis=1) + log(stockPrice)
	stockPrice_t = np.exp(log_stockPrice_t)
	
	# Calculate the Monte Carlo estimator
	callValue = exp(-rate * timeToMature) * np.maximum((stockPrice_t[:,-1] - strikePrice), 0).mean()
	
	# return and print results
	if timeit:
		print 'Run time of Vectorized Monte Carlo Simulation is %5.3f seconds.' %(time() - start_time)
	return callValue


def main():
### Set up parameters for calculation:
### =================
	stockPrice = 100.
	strikePrice = 105.
	timeToMature = 1.
	rate = 0.05
	sigma = 0.2
### =================
### Get benchmark:
	callValue = BSM_Call_Value(stockPrice, strikePrice, rate, timeToMature, sigma)
	print 'European Call Option Value by BSM equation is $%5.3f' %callValue
###	print 'Call price should be: $%5.5f, used %5.5f microseconds.' %(callValue, run_time)
	Pure_Py_MC_Value = Pure_Py_MC(stockPrice, strikePrice, rate, timeToMature, sigma)
	print 'European Call Option Value by Pure Python Monte Carlo Simulation is $%5.3f' %Pure_Py_MC_Value
	Vec_MC_Value = Vec_MC(stockPrice, strikePrice, rate, timeToMature, sigma)
	print 'European Call Option Value by Vectorized Monte Carlo Simulation is $%5.3f' %Vec_MC_Value

if __name__ == '__main__':
	main()