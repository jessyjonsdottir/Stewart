import math as m
import matplotlib.pyplot as plt
import numpy as np

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
    #Breytum p2 frá 1 og hækkum okkur þangað til við finnum gildi á p2 með 2 rótum
    p2 = 8
    #p3 er fastur sem 3
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2

#Grafið sem teiknar fallið
def teiknagrafbil(titill, xnedra, xefra, ynedra, yefra):
    #Bil og grid stærð
    xvals = np.arange(-np.pi, np.pi, 0.01)
    yvals = f(xvals)
    #Plotta með x-ás vs y-ás
    plt.plot(xvals, yvals)

    #Ásarnir
    plt.xlim(xnedra, xefra)
    plt.ylim(ynedra, yefra)

	#Merkjum grafið
    plt.grid(True)
    plt.title(titill)
    plt.xlabel('Theta')
    plt.ylabel('Fallgildi')

plt.figure("Graf 6.8.1, p2=8")
teiknagrafbil("Graf 6.8.1, p2=8", -pi, pi, -10000, 100000)
plt.show()
