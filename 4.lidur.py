import numpy as np
import matplotlib.pyplot as plt
import Teiknagraf.py*
import Teiknamynd.py*

#Breytum föstunum til að teikna í 4.lið
    #Hliðarlengdir Stewart-pallsins
L1 = 3
L2 = 3*np.sqrt(2)
L3 = L1
gamma = np.pi/4
pi = np.pi
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

#Skilgreinum breytur fyrir x & y hnit þrýhyrningsins fyrir xogy()
x_0 = 5
y_0 = 5

x_1 = 5
y_1 = 5

x_2 = 5
y_2 = 5

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

	x_0 = N1 / D
	y_0 = N2 / D
	print(x_0)
	print(y_0)

	if(theta+gamma > (np.pi/2)):
		x_1 = x_0 - L1*np.sin(theta+gamma-(np.pi/2))
		y_1 = y_0 + L1*np.sin(theta+gamma)
	else:
		x_1 = x_0 + L1*np.cos(theta+gamma)
		y_1 = y_0 + L1*np.sin(theta+gamma)

	if(gamma > (np.pi/2)):
		x_2 = x_0 - L1*np.cos(theta-(np.pi/2))
		y_2 = y_0 + L1*np.sin(theta)
	else:
		x_2 = x_0 + L1*np.cos(theta)
		y_2 = y_0 + L1*np.sin(theta)
	teiknamynd( x_0, x_1, x_2, y_0, y_1, y_2 , 0, 0, 5, 0, 6, 0)


plt.figure("Dæmi 4")
plt.subplot(221)
xogy(-0.7208)
plt.subplot(222)
xogy(-0.3310)
plt.subplot(223)
xogy(1.1437)
plt.subplot(224)
xogy(2.1160)

#er ehv heima hallo ?
