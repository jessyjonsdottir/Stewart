import math as m
import matplotlib.pyplot as plt
import numpy as np
from numpy import sign

tol = 0.001

pi = np.pi
#Hliðarlengdir Stewart-pallsins
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

def f(theta):
    #Hér þarf að finna þeta fyrst
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

def rotaleit(f,x1,x2, tol=1.0e-09):
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
		return None

	n = int(m.ceil(m.log(abs(x2-x1)/tol)/m.log(2.0)))
	for i in range(n):
		x3 = 0.5*(x1+x2); f3 = f(x3)
		if (abs(f3) > abs(f1)) \
		   and (abs(f3) > abs(f2)):
			return None
		if f3 == 0.0:
			return x3
		if sign(f2) != sign(f3):
			x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	return (x1 + x2)/2.0


def teiknagraf(titill):
	xvals = np.arange(-np.pi, np.pi, 0.01) # Grid of 0.01 spacing from pi to pi
	yvals = f(xvals) # Evaluate function on xvals
	plt.plot(xvals, yvals) #Create line plot with yvals against xvals

	#plt.xlim(0, 100) #Takmörk ásanna
	#plt.ylim(0, 100)

	#merkjum grafiðs
	plt.grid(True)
	plt.title(titill)
	plt.xlabel('Theta')
	plt.ylabel('Fallgildi')
	#plt.show()


p2 = 0
bil = -m.pi
svor = []
teljari2 = 0

for i in range(0,1000):
	teljari1 = 0
	for j in range(0,100):
		values = rotaleit(f,bil, bil+(m.pi)/50)
		if values != None:
			teljari1 += 1
		bil += (m.pi)/50
	if teljari1 != teljari2:
		svor.append(p2)
	teljari2 = teljari1
	teljari1 = 0
	p2 += 0.01

print(svor)

#teikna
plt.plot([0,svor[0]], [0,0], color='r')
plt.plot([svor[0],svor[0]], [0,2], color='b')
plt.plot([svor[0],svor[1]], [2,2], color='r')
plt.plot([svor[1],svor[1]], [2,4], color='b')
plt.plot([svor[1],svor[2]], [4,4], color='r')
plt.plot([svor[2],svor[2]], [4,6], color='b')
plt.plot([svor[2],svor[3]], [6,6], color='r')
plt.plot([svor[3],svor[3]], [6,4], color='b')
plt.plot([svor[3],svor[4]], [4,4], color='r')
plt.plot([svor[4],svor[4]], [4,2], color='b')
plt.plot([svor[4],svor[7]], [2,2], color='r')
plt.plot([svor[7],svor[7]], [2,0], color='b')
plt.plot([svor[7],10], [0,0], color='r')

plt.title("Verkefni 7")
plt.xlabel('Lengd p2')
plt.ylabel('Fjöldi núllstöðva')
plt.show()
