import math as m

def f(theta):
    pi = m.pi
    #Hliðarlengdir Stewart-pallsins
    L1 = 3
    L2 = 3*m.sqrt(2)
    L3 = L1
    gamma = pi/4

    #Festipunktar tjakkanna
    x0 = 0
    y0 = 0

    x1 = 5
    y1 = 0

    x2 = 0
    y2 = 6

#Hér þarf að finna þeta fyrst
    A2 = L3*m.cos(theta) - x1
    B2 = L3*m.sin(theta)
    A3 = L2*m.cos(theta+gamma) - x2
    B3 = L2*m.sin(theta+gamma) - y2

    p1 = 5
    p2 = p1
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2

def teiknagraf(titill):
    xvals = np.arange(-np.pi, np.pi, 0.01) # Grid of 0.01 spacing from pi to pi
    yvals = f(xvals) # Evaluate function on xvals
    plt.plot(xvals, yvals) #Create line plot with yvals against xvals

    #plt.xlim(0, 100) #Takmörk ásanna
    #plt.ylim(0, 100)

	#merkjum grafið
    plt.grid(True)
    plt.title(titill)
    plt.xlabel('Theta')
    plt.ylabel('Fallgildi')

    plt.show()
