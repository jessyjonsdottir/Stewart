import numpy as np
import matplotlib.pyplot as plt

debug = False

#Breytum föstunum til að þeir samræmist 4. lið
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
p2 = 7
p3 = 3

#Skilgreinum breytur fyrir x & y hnit þrýhyrningsins fyrir xogy()
x_0 = 5
y_0 = 5

x_1 = 5
y_1 = 5

x_2 = 5
y_2 = 5

def teiknatri( x_0, x_1, x_2, y_0, y_1, y_2, xb_0, xb_1, xb_2, yb_0, yb_1, yb_2):
	#Þríhyrningurinn
	plt.plot([x_0,x_1,x_2,x_0], [y_0,y_1,y_2,y_0], color='b')
	plt.ylim(-7,10)
	plt.xlim(-7,10)

	#Línurnar útfrá þríhyrningnum
	plt.plot([xb_0,x_0], [yb_0,y_0], color='b')
	plt.plot([xb_1,x_1], [yb_1,y_1], color='b')
	plt.plot([xb_2,x_2], [yb_2,y_2], color='b')

	#Plotta punktana í þríhyrningnum
	plt.scatter(x_0, y_0, c='b', s=20)
	plt.scatter(x_1, y_1, c='b', s=20)
	plt.scatter(x_2, y_2, c='b', s=20)

	#Plotta punktana útfrá línunum
	plt.scatter(xb_0, yb_0, c='b', s=20)
	plt.scatter(xb_1, yb_1, c='b', s=20)
	plt.scatter(xb_2, yb_2, c='b', s=20)

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

def teiknarot(theta):
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

	x_1 = x_0 + L2*np.cos(theta+gamma)
	y_1 = y_0 + L2*np.sin(theta+gamma)

	x_2 = x_0 + L3*np.cos(theta)
	y_2 = y_0 + L3*np.sin(theta)

	if(debug is True):
		print("x hnit:")
		print(x_0)
		print("y hnit:")
		print(y_0)

		print("L1")
		print(np.sqrt((x_1-x_2)**2+(y_1-y_2)**2))
		print(L1)

		print("L2")
		print(np.sqrt((x_1-x_0)**2+(y_1-y_0)**2))
		print(L2)

		print("L3")
		print(np.sqrt((x_2-x_0)**2+(y_2-y_0)**2))
		print(L3)
	plt.grid()
	teiknatri( x_0, x_1, x_2, y_0, y_1, y_2 , 0, 0, 5, 0, 6, 0)

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

####HÉR GERIST STÖFFIÐ

plt.figure("Dæmi 5: Graf")
teiknagraf("Graf 2")

r1 = -0.6731
r2 = -0.3547
r3 = 0.03776
r4 = 0.4588
r5 = 0.9776
r6 = 2.5138

plt.figure("Dæmi 5: Þríhyrningar" )
plt.subplot(321)
teiknarot(r1)

plt.subplot(322)
teiknarot(r2)

plt.subplot(323)
teiknarot(r3)

plt.subplot(324)
teiknarot(r4)

plt.subplot(325)
teiknarot(r5)

plt.subplot(326)
teiknarot(r6)

plt.show()
