import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
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

######################################LIÐUR 5
#Breytum armlengd p2
p2 = 7

plt.figure("Graf 3")
teiknagraf("Graf 3")
plt.show()
=======
class Toluleg(object):
    """Alls konar dót, Toluleg."""
    def __init__(self, arg):
        super(Toluleg, self).__init__()
        self.arg = arg

    #Fastar stærðir: L1, L2, L3, p1, p2, p3
    #Viljum að forritið taki inn theta
    #Viljum að forritið skili x, y
    def f(theta):
        pi = m.pi
        #Hliðarlengdir Stewart-pallsins
        L1 = 2
        L2 = m.sqrt(2)
        L3 = L2
        gamma = pi/2

        #Festipunktar tjakkanna
        x0 = 0
        y0 = 0

        x1 = 4
        y1 = 0

        x2 = 0
        y2 = 4

        #Reiknum A og B
        A2 = L3*m.cos(theta) - x1
        B2 = L3*m.sin(theta)
        A3 = L2*m.cos(theta+gamma) - x2
        B3 = L2*m.sin(theta+gamma) - y2

        #Þekktar armalengdir
        p1 = m.sqrt(5)
        p2 = p1
        p3 = p1

        #
        D = 2*(A2*B3 - B2*A3)

        N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
        N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
        return N1**2 + N2**2 -p1**2*D**2


    x = np.linspace(-m.pi,m.pi,100)
    # 100 linearly spaced numbers frá -pi til pi
    y = f(x)
    plt.scatter(x, y)
    plt.show()
>>>>>>> 9040e5f04240941c7557fa767702a137b7008d39
