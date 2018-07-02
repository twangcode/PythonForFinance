##############
# Arrays with Python lists
##############

# vec = [.5, .75, 1., 1.5, 2.]
# print vec
# mat = [vec, vec, vec]
# print mat
# print mat[1]
# print mat[1][0]
# vec[0] = 'Python'
# print mat
# from copy import deepcopy
# vec = [.5, .75, 1., 1.5, 2.]
# mat = 3 * [deepcopy(vec),]
# print mat
# vec[0] = 'Python'
# print mat

######################
# Numpy Arrays
######################

import numpy as np 
a = np.array([0, .5, 1., 1.5, 2.])
# print a
# print type(a)
# print a[:2]
# print a.sum()
# print a.std()
# print a.cumsum()
# print a * 2
# print a ** 2
# print np.sqrt(a)

b = np.array([a, a * 2])
# print b
# print b[0]
# print b[0, 2]
# print b.sum()
# print b.sum(axis=0)		# column-wise sum
# print b.sum(axis=1)		# row-wise sum
c = np.zeros((2, 3, 4), dtype = 'i', order = 'C')
# print c
d = np.ones_like(c, dtype='f', order='F')
# print d
mat = np.random.standard_normal((5000,5000))
# print mat.sum()
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'), ('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0, 1)), ('Jones', 53, 1.72, (2, 2))], dtype=dt)
# print s
# print s['Name']
# print s['Height'].sum()
# print s[1]['Age']

################################
# Vectorization of Code
##############################

r = np.random.standard_normal((4,3))
s = np.random.standard_normal((4,3))
# print r + s
# print 2 * r + 3
t = np.random.standard_normal(3)
# print r + t
u = np.random.standard_normal(4)
# print r + u		# doesn't work, different shape
# print r.transpose() + u #	r.transpose() is equal to r.T
# print np.shape(r)
# print np.shape(r.T)
# print np.sin(r)
