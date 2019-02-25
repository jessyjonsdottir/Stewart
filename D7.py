import math as m
import matplotlib.pyplot as plt
import numpy as np

tol =0.001

<<<<<<< HEAD
pi = np.pi
#Hliðarlengdir Stewart-pallsins
L1 = 3
L2 = 3*np.sqrt(2)
L3 = L1
gamma = pi/4
=======

def f(theta):
    L1 = 3
    L2 = 3*m.sqrt(2)
    L3 = L1
    gamma = m.pi/4
>>>>>>> 4be3147f6f8917c6fe0c718d8014e3cca7942739

#Festipunktar tjakkanna
x0 = 0
y0 = 0

x1 = 5
y1 = 0

x2 = 0
y2 = 6

<<<<<<< HEAD
def f(theta):
    #Hér þarf að finna þeta fyrst
    A2 = L3*np.cos(theta) - x1
    B2 = L3*np.sin(theta)
    A3 = L2*np.cos(theta+gamma) - x2
    B3 = L2*np.sin(theta+gamma) - y2
=======
    x2 = 0
    y2 = 6

    A2 = L3*m.cos(theta) - x1
    B2 = L3*m.sin(theta)
    A3 = L2*m.cos(theta+gamma) - x2
    B3 = L2*m.sin(theta+gamma) - y2
>>>>>>> 4be3147f6f8917c6fe0c718d8014e3cca7942739

    #p1 er fastur sem 5
    p1 = 5

    #p3 er fastur sem 3
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2

def bisection(a,b):
    if f(a) * f(b) >= 0:
        return None
    c = a
    while (b-a) >= tol:
        c = (a+b)/2
        if f(c) == 0:
            break
        elif f(c)*f(a) < 0:
            b=c
        else:
            a=c
    return c

p2 = 0

space = -math.pi
answer = []
counterB = 0


for i in range(0,100000):
	counterA = 0
	for j in range(0,100):
		values = bisection(space, space+(math.pi)/50)
		if values != None:
			counterA += 1
		space += (math.pi)/50
	if counterA != counterB:
		answer.append(p2)
	counterB = counterA
	counterA = 0
	p2 += 0.01
print(answer)
