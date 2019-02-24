import numpy as np
import math as m
import matplotlib.pyplot as plt

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

    def teikna:
        x = np.linspace(-math.pi,math.pi,100)
        # 100 linearly spaced numbers frá -pi til pi
        y = f(x)
        plt.plot(x, y)
        plt.show()
