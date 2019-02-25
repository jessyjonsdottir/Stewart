import math
import matplotlib.pyplot as plt
import numpy as np

tol =0.001

pi = np.pi
#Hliðarlengdir Stewart-pallsins


def f(theta):
    L1 = 3
    L2 = 3*np.sqrt(2)
    L3 = L1
    gamma = pi/4

#Festipunktar tjakkanna
    x0 = 0
    y0 = 0

    x1 = 5
    y1 = 0

    x2 = 0
    y2 = 6
    A2 = L3*np.cos(theta) - x1
    B2 = L3*np.sin(theta)
    A3 = L2*np.cos(theta+gamma) - x2
    B3 = L2*np.sin(theta+gamma) - y2

    #p1 er fastur sem 5
    p1 = 5

    #p3 er fastur sem 3
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2

def rotaleit(f,x1,x2):
    #Athugum strax hvort x1 eða x2 séu rætur
	f1 = f(x1)
	if f1 == 0.0:
		return x1
	f2 = f(x2)
	if f2 == 0.0:
		return x2
    #Athugum hvort formerki fallgildis á endum bilsins séu jöfn; 
    #ef svo er er rótin ekki á bilinu
	if sign(f1) == sign(f2):
		return ('Rótin er ekki á bilinu')
  
	n = int(m.ceil(m.log(abs(x2-x1)/tol)/m.log(2.0)))
	for i in range(n):
		x3 = 0.5*(x1+x2); f3 = f(x3)
		if (switch == 1) and (abs(f3) > abs(f1)) \
		   and (abs(f3) > abs(f2)):
			return None
		if f3 == 0.0:
			return x3
		if sign(f2) != sign(f3):
			x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	return (x1 + x2)/2.0

p2 = 0
space = -math.pi
answer = []
counterB = 0
for i in range(0,10000):
    counterA = 0
    for j in range(0,100):
        values = rotaleit(f, space, space+(math.pi)/50)
        if values != None:
            counterA += 1
        space += (math.pi)/50
    if counterA != counterB:
        answer.append(p2)
    counterB = counterA
    counterA = 0
    p2 += 0.001

print(answer)
