
# Three different methods to run a loop: 3*log(x)+cos(x)**2 
# where x range from 1 to 25000000
# returns the execution time
#

import time
import numpy as np 
import numexpr as ne 
from math import *

def loop_1(loops):
	# a simple for loop
	start_time = time.time()
	a = range(1, loops)
	for x in a :
		f = 3 * log(x) + cos(x) ** 2
	print "Execution time is %5.3fs" % (time.time() - start_time)

def loop_2(loops):
	# using numpy vector notation
	start_time = time.time()
	a = np.arange(1, loops)
	f = 3 * np.log(a) + np.cos(a) ** 2
	print "Execution time is %5.3fs" % (time.time() - start_time)

def loop_3(loops, threads):
	# using numexpr and multiple threads
	start_time = time.time()
	ne.set_num_threads(threads)
	a = np.arange(1, loops)
	f = '3 * log(a) + cos(a) ** 2'
	r = ne.evaluate(f)
	print "Execution time is %5.3fs" % (time.time() - start_time)

def main():
	loops = 25000000
	loop_1(loops)
	loop_2(loops)
	loop_3(loops, 4)

if __name__ == '__main__':
	main()