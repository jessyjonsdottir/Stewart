import math as m
import matplotlib.pyplot as plt
import numpy as np
from numpy import sign

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
    #Breytum p2 frá 1-10 og skoðum
    p2 = 1
    #p3 er fastur sem 3
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2

def teiknagrafbil(titill, xnedra, xefra, ynedra, yefra):
    # bil og grid stærð
    xvals = np.arange(-np.pi, np.pi, 0.01)
    yvals = f(xvals)
    plt.plot(xvals, yvals) #Create line plot with yvals against xvals

    plt.xlim(xnedra, xefra) #Takmörk ásanna
    plt.ylim(ynedra, yefra)

	#merkjum grafið
    plt.grid(True)
    plt.title(titill)
    plt.xlabel('Theta')
    plt.ylabel('Fallgildi')

plt.figure("Graf 6.1: Stækkun")
teiknagrafbil("Graf 6.1: Stækkun", -1, 2.7,-5,5 )
plt.show()
