import pandas_datareader.data as pdr 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

def Add_Two_MA(symbol, start_dt, end_dt, source='quandl', draw_plot=False): 
	data = pdr.DataReader(symbol, source, start_dt, end_dt)
# Reverse order for data
# data[:5] means select the first 5 rows
# data[::2] means select every other row
# data[::-1] means select reverse rows
	data = data[::-1]
	data['TwoMonthMA'] = np.round(data['AdjClose'].rolling(window=42).mean(), 2)
	data['OneYearMA'] = np.round(data['AdjClose'].rolling(window=252).mean(), 2)

# Plot:
	if draw_plot:
		data[['AdjClose', 'TwoMonthMA', 'OneYearMA']].plot()
		plt.show()
	return data

def Trading_Signal(data, threshold=10, draw_plot=False):
	data['42-252'] = data['TwoMonthMA'] - data['OneYearMA']
	
	data['Regime'] = np.where(data['42-252'] > threshold, 1, 0)
	data['Regime'] = np.where(data['42-252'] < -threshold, -1, data['Regime'])
	
	if draw_plot:
		data['Regime'].plot()
		plt.ylim([-1.1, 1.1])
		plt.show()

	return data

def Back_Test(data):
	data['BuyHoldRet'] = np.log(data['AdjClose'] / data['AdjClose'].shift(1))
	data['BuyHoldRet'].cumsum().apply(np.exp).plot()
	plt.show()

def main():
	print 'Start Running...'
	symbol = 'GOOG'
	start_dt = '1/1/2010'
	end_dt = '1/1/2018'
	
	data = Add_Two_MA(symbol, start_dt, end_dt)
	data = Trading_Signal(data)
	Back_Test(data)


if __name__ == '__main__':
	main()