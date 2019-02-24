import numpy as np
import matplotlib.pyplot as plt

#Fastar stærðir: L1, L2, L3, p1, p2, p3
#Skilgreinum fasta utan fallsins:
pi = np.pi
    #Hliðarlengdir Stewart-pallsins
L1 = 2
L2 = np.sqrt(2)
L3 = L2
gamma = pi/2
    #Festipunktar tjakkanna
x0 = 0
y0 = 0
x1 = 4
y1 = 0
x2 = 0
y2 = 4
    #Þekktar armalengdir
p1 = np.sqrt(5)
p2 = p1
p3 = p1

######################################LIÐUR 1
#Viljum að forritið taki inn theta
#Viljum að forritið skili x, y
def f(theta):
	#Reiknum A og B
	A2 = L3*np.cos(theta) - x1
	B2 = L3*np.sin(theta)
	A3 = L2*np.cos(theta+gamma) - x2
	B3 = L2*np.sin(theta+gamma) - y2

	D = 2*(A2*B3 - B2*A3)

	N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
	N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
	return N1**2 + N2**2 -(p1**2)*(D**2)

######################################LIÐUR 2
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

#Köllum á teikna fallið
plt.figure("Graf 1")
teiknagraf("Graf 1")
######################################LIÐUR 3

plt.figure("þríhyrningar 1")
#Þríhyrningurinn
plt.plot([1,2,2,1], [2,1,3,2], color='b')
plt.ylim(-1,5)
plt.xlim(-1,5)

#Línurnar útfrá þríhyrningnum
plt.plot([0,2], [4,3], color='b')
plt.plot([1,0], [2,0], color='b')
plt.plot([2,4], [1,0], color='b')

#Plotta punktana útfrá línunum
plt.scatter(1, 2, c='b', s=20)
plt.scatter(2, 1, c='b', s=20)
plt.scatter(2, 3, c='b', s=20)

#Plotta punktana í þríhyrningnum
plt.scatter(4, 0, c='b', s=20)
plt.scatter(0, 0, c='b', s=20)
plt.scatter(0, 4, c='b', s=20)


plt.figure("þríhyrningar 2")
#Þríhyrningurinn 2
plt.plot([1,2,3,1], [2,1,2,2], color='b')
plt.ylim(-1,5)
plt.xlim(-1,5)

#Línurnar útfrá þríhyrningnum
plt.plot([1,0], [2,4], color='b')
plt.plot([2,0], [1,0], color='b')
plt.plot([3,4], [2,0], color='b')

#Plotta punktana í þríhyrningnum
plt.scatter(1, 2, c='b', s=20)
plt.scatter(2, 1, c='b', s=20)
plt.scatter(3, 2, c='b', s=20)

#Plotta punktana útfrá línunum
plt.scatter(4, 0, c='b', s=20)
plt.scatter(0, 0, c='b', s=20)
plt.scatter(0, 4, c='b', s=20)



######################################LIÐUR 4
#Breytum föstunum til að teikna í 4.lið
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
    #Þekktar armalengdir
p1 = 5
p2 = p1
p3 = 3

plt.figure("Graf 2")
teiknagraf("Graf 2")

def xogy(theta):
	#Reiknum A og B
	A2 = L3*np.cos(theta) - x1
	B2 = L3*np.sin(theta)
	A3 = L2*np.cos(theta+gamma) - x2
	B3 = L2*np.sin(theta+gamma) - y2

	D = 2*(A2*B3 - B2*A3)

	N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
	N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)

    x_0 = N1/D
    y_0 = N2/D

    x_1 = x_0 + L1*np.cos(theta+gamma)
    y_1 = y_0 + L1*np.sin(theta+gamma)

    x_2 = x_0 + L1*np.cos(theta)
    y_2 = y_0 + L1*np.sin(theta)

        return x_0, x_1, x_2, y_0, y_1, y_2


import teiknamynd

plt.figure("Dæmi 4")
plt.subplot(221)
teiknamynd("Rót 1", xogy(-0.7208), 0, 0, 4, 0, 4, 0)
plt.subplot(222)
teiknamynd("Rót 2", xogy(-0.3310), 0, 0, 4, 0, 4, 0)
plt.subplot(223)
teiknamynd("Rót 3", xogy(1.1437), 0, 0, 4, 0, 4, 0)
plt.subplot(224)
teiknamynd("Rót 4", xogy(2.1160), 0, 0, 4, 0, 4, 0)



######################################LIÐUR 5
#Breytum armlengd p2
p2 = 7

def teiknagrafbil(titill, xnedra, xefra, ynedra, yefra):
    xvals = np.arange(-np.pi, np.pi, 0.01) # Grid of 0.01 spacing from pi to pi
    yvals = f(xvals) # Evaluate function on xvals
    plt.plot(xvals, yvals) #Create line plot with yvals against xvals

    plt.xlim(xnedra, xefra) #Takmörk ásanna
    plt.ylim(ynedra, yefra)

	#merkjum grafiðs
    plt.grid(True)
    plt.title(titill)
    plt.xlabel('Theta')
    plt.ylabel('Fallgildi')

plt.figure("Graf 3: Stækkun")
teiknagrafbil("Graf 3: Stækkun", -1, 2.7,-5,5 )
plt.figure("Graf 3")
teiknagraf("Graf 3")
plt.show()

import math as m
from numpy import sign
