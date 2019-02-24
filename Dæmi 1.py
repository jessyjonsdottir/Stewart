import numpy as np

#Fastar stærðir: L1, L2, L3, p1, p2, p3
#Viljum finna theta, x, y sem er þá afleiddar stærðir þeirra gefnu
def f(theta):
    #Hliðarlengdir Stewart-pallsins
    L1 = 2
    L2 = sqrt(2)
    L3 = L2
    gamma = pi/2

    #Festipunktar tjakkanna
    x0 = 0
    y0 = 0

    x1 = 4
    y1 = 0

    x2 = 0
    y2 = 4

#Hér þarf að finna þeta fyrst
    A2 = L3*cos(theta) - x1
    B2 = L3*sin(theta)
    A3 = L2*cos(theta+gamma) - x2
    B3 = L2*sin(theta+gamma) - y2

    #x = p1*cos(theta)
    #y = p1*sin(theta)
    #p1 = sqrt(x**2 + y**2)
    #p2 = sqrt((x+A2)**2 + (y+B2)**2)
    #p3 = sqrt((x+A3)**2 + (y+B3)**2)
    p1 = sqrt(5)
    p2 = p1
    p3 = p1

    #Hvað er þetta
    D = 2(A2*B3 - B2*A3)
    #D má ekki vera 0:
    #if D != 0:
        #x = (B3(p2**2-p1**2-A2**2-B2**2)-B2(p3**2-p1**2-A3**2-B3**2))/D
        #y = (-A3(p2**2-p1**2-A2**2-B2**2)+A2(p3**2-p1**2-A3**2-B3**2))/D

    #else
        #return("Ógilt")
    N1 = B3(p2**2-p1**2-A2**2-B2**2)-B2(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3(p2**2-p1**2-A2**2-B2**2)+A2(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2
