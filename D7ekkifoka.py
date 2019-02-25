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

def f(theta):
#Hér þarf að finna þeta fyrst
    A2 = L3*np.cos(theta) - x1
    B2 = L3*np.sin(theta)
    A3 = L2*np.cos(theta+gamma) - x2
    B3 = L2*np.sin(theta+gamma) - y2

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2


def teiknagraf(titill):
    xvals = np.arange(-10, 10, 0.01) # Grid of 0.01 spacing from pi to pi
    yvals = f(xvals) # Evaluate function on xvals
    plt.plot(xvals, yvals) #Create line plot with yvals against xvals

	#merkjum grafiðs
    plt.grid(True)
    plt.title(titill)
    plt.xlabel('Theta')
    plt.ylabel('Fallgildi')

    #plt.show()

#Köllum á teikna fallið
plt.figure("Graf 1")
teiknagraf("Graf 1")
plt.show()

p2 = 3
for i in range(0, 100):
    teiknagraf("i")
    teiknagraf(-0.7208)
    p2 += 0.2
plt.show()
