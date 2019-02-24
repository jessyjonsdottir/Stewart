import numpy as np

def f(p1, p2, p3, L1, L2, L3, x1, x2, y2, gamma):
    A2 = L3*cos(theta) - x1
    B2 = L3*sin(theta)
    A3 = L2*cos(theta+gamma)-x2
    B3 = L2*sin(theta+gamma)-y2

    p1 = sqrt(x**2 + y**2)
    p2 = sqrt((x+A2)**2 + (y+B2)**2)
    p3 = sqrt((x+A3)**2 + (y+B3)**2)

    D = 2(A2*B3 - B2*A3)
    if D != 0:
