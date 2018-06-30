#
# Monte Carlo Valuation of a European Call option
# in Black-Scholes-Merton model
#

from numpy import *

# set up parameter values:

S0 = 100		# Stock price atm
K = 105			# Strike price
T = 1.0			# Time to maturity
r = 0.05		# Risk-free rate
sigma = 0.2		# volatility

I = 1000000		# Number of simulation

def MC_Valuation_Euro_Call(stockPrice, strikePrice, time, rate, sigma, numberSimulation):
	z = random.standard_normal(numberSimulation)
	ST = stockPrice * exp((rate - 0.5 * sigma ** 2) * time + sigma * sqrt(time) * z)
	hT = maximum(ST - strikePrice, 0)
	callPrice = exp(-rate * time) * mean(hT)
	return callPrice

def main():
	callPrice = MC_Valuation_Euro_Call(S0, K, T, r, sigma, I)
	print "Value of the European Call Option is $%5.3f" %callPrice

if __name__ == '__main__':
	main()