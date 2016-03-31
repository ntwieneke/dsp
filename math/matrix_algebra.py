# Matrix Algebra

# Question 1

import numpy as np

a = np.matrix([[1,2,3],[2,7,4]])
print a
print a.shape

b = np.matrix([[1,-1],[0,1]])
print b.shape

c = np.matrix([[5,-1],[9,1],[6,0]])
print c.shape

d = np.matrix([[3,-2,-1],[1,2,3]])
print d.shape

u = np.matrix([[6,2,-3,5]])
print u.shape

v = np.matrix([[3,4,-1,4]])
print v.shape

w = np.matrix([[1],[8],[0],[5]])
print w.shape

# Question 2
print "Question2"

print u+v

print u-v

print 6 * u

# print np.dot(u,v)
print "not defined"

print np.linalg.norm(u)

# Question 3

# def solve(problem):
# 	try:
# 		problem
# 	except ValueError:
# 		print "Not defined"

try:
	print a+c
except ValueError:
	print "Not defined"

try:
	print a - c.T
except ValueError:
	print "Not defined"

try:
	print c.T + 3*d
except ValueError:
	print "Not defined"

try:
	print b*a
except ValueError:
	print "Not defined"	

try:
	print b*a.T
except ValueError:
	print "Not defined"	