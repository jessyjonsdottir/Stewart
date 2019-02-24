import math as m

#FYRSTI LIÐUR
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
    
    p1 = m.sqrt(5)
    p2 = p1
    p3 = p1

#Hér þarf að finna þeta fyrst
    A2 = L3*m.cos(theta) - x1
    B2 = L3*m.sin(theta)
    A3 = L2*m.cos(theta+gamma) - x2
    B3 = L2*m.sin(theta+gamma) - y2

  

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2
    
#FJÓRÐI LIÐUR   
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
    
    
#FIMMTI LIÐUR     
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
    p2 = 7
    p3 = 3

    D = 2*(A2*B3 - B2*A3)

    N1 = B3*(p2**2-p1**2-A2**2-B2**2)-B2*(p3**2-p1**2-A3**2-B3**2)
    N2 = -A3*(p2**2-p1**2-A2**2-B2**2)+A2*(p3**2-p1**2-A3**2-B3**2)
    return N1**2 + N2**2 -p1**2*D**2
