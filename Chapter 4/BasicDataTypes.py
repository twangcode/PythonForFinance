############
# int type
############
a = 10
print type(a)
print a.bit_length()
b = 100000
print b.bit_length()
c = 10 ** 100
print c
print c.bit_length()

##################
# float type
##################
a = 1. / 4
print type(a)
b = 0.35
print b + 0.1
print b.as_integer_ratio()

import decimal
from decimal import Decimal 

print decimal.getcontext()
print Decimal(1) / Decimal(11)

decimal.getcontext().prec = 4
print Decimal(1) / Decimal(11)

decimal.getcontext().prec = 50
print Decimal(1) / Decimal(11)

#################
# strings
#################
t = 'this is a string object'
print t.capitalize()
print t.split()
print 'http://www.python.org'.strip('htp:/')
print 'lalalalala'.count('la')

import re
series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""
dt = re.compile("'[0-9/:\s]+'")
print dt.findall(series)