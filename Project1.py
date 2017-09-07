from __future__ import division
from matplotlib.pyplot import *
from numpy import *

N = 4

h = 1/(N+1)
a = -1
b = 2
c = -1

#x = [i*h for i in range(N)]

#Analytic solution
def U(x):
	return 1-(1-exp(-10))*x - exp(-10*x)

#Numerical solution
def f(x):
	return 100*exp(-10*x)

#Defining all arrays needed for storing values 
#Vektor v for Av = B
#Vektor B og A for Av = B
d_twidd = zeros(N)
f_twidd = zeros(N)

x = zeros(N+2)
B = zeros(N)
A = zeros((N,N))

#Conditions for x-array and numerical solution Av = B 

x[0] = 0
x[N+1] = 1

v = zeros(N+2)
v[0] = 0  
v[N+1] = 0

#Producing x-array

for j in range(1, N):
	x[j] = j*h 

#Filling A with 2's on diag and -1 on diags below and above diag
#Setting values for B
for i in range(N):
	A[i][i] = b
	A[i][i-1] = a
	A[i-1][i] = c
	B[i] = h**2*f(x[i])
A[0][i] = 0
A[i][0] = A[0][i]

f_twidd[0] = f(x[0]) #Init value for row reduction
d_twidd[0] = 2 #Init value for row reduction

#A[0][N-1] = 0
#A[N-1][0] = 0

for k in range(1,N-1):
	d_twidd[k] = (k+1)/k
	f_twidd[k] = f(x[k]) + ((k-1)*f_twidd[k-1])/k
	v[k-1] = ((k-1)/k)*(f_twidd[k-1] + v[k])

v[k] = f_twidd[k]/d_twidd[k]
print v

#plot(x, f(x), label = 'Analytic sol')
#xlabel('$x$', fontsize = 16)
#ylabel('y', fontsize = 16)

#hold('on')
#plot(x, v, label = 'Num sol')
#show()
