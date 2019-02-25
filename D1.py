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
