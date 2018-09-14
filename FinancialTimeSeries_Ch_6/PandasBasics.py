import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Build a dataframe:
df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'], index=['a', 'b', 'c', 'd'])
# Typical operations on a DataFrame obj:
# print df.index
# print df.columns
# print df.ix['c']
# print df.ix[['a', 'd']]
# print df.ix[df.index[1:3]]
# print df.sum()
# print df.apply(lambda x: x ** 2)
# print df ** 2
df['floats'] = [1.5, 2.5, 3.5, 4.5]
df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'], index=['d', 'a', 'b', 'c'])
df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75, 'names': 'Henry'}, index=['z']), sort=True)
df = df.join(pd.DataFrame([1, 4, 9, 16, 25], \
						index=['a', 'b', 'c', 'd', 'y'], \
						columns=['squares']), \
						how='outer')

# =======================================================================

a = np.random.standard_normal((9,4))
a = a.round(6)
df = pd.DataFrame(a)
df.columns=[['No1', 'No2', 'No3', 'No4']]
dates = pd.date_range('2015-1-1', periods=9, freq='M')
# print dates
df.index = dates
# print np.array(df)

# =========================================================================
# print df.sum()
# print df.mean()
# print df.cumsum()
# print df.describe()
# print df
# df.cumsum().plot(subplots=True)

# plt.show()

# ============================================================================
# Series Class::::
# print type(df)
# print df['No1']
# print type(df['No1']) ########????????????????

# ============================================================================
# Groupby operations::

df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
# print df.columns
df = pd.DataFrame(df.values, columns=['NO1', 'NO2', 'NO3', 'NO4', 'Quarter'])
# print type(df['NO1'])
groups = df.groupby('Quarter')
# print groups.max()

# ============================================================================
# Financial Data:
import pandas_datareader.data as pdr 
import fix_yahoo_finance as fyf 
fyf.pdr_override()
DAX = pdr.get_data_yahoo('^GDAXI', start='2000-1-1')
# print DAX.info()
DAX['Close'].plot(figsize=(8,5))
plt.show()



def main():
	return


if __name__ == '__main__':
	main()