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


plt.figure("þríhyrningar 1")
#Þríhyrningurinn
plt.plot([1,2,2,1], [2,1,3,2], color='b')
plt.ylim(-1,5)
plt.xlim(-1,5)

#Línurnar útfrá þríhyrningnum
plt.plot([0,2], [4,3], color='b')
plt.plot([1,0], [2,0], color='b')
plt.plot([2,4], [1,0], color='b')

#Plotta punktana útfrá línunum
plt.scatter(1, 2, c='b', s=20)
plt.scatter(2, 1, c='b', s=20)
plt.scatter(2, 3, c='b', s=20)

#Plotta punktana í þríhyrningnum
plt.scatter(4, 0, c='b', s=20)
plt.scatter(0, 0, c='b', s=20)
plt.scatter(0, 4, c='b', s=20)


plt.figure("þríhyrningar 2")
#Þríhyrningurinn 2
plt.plot([1,2,3,1], [2,1,2,2], color='b')
plt.ylim(-1,5)
plt.xlim(-1,5)

#Línurnar útfrá þríhyrningnum
plt.plot([1,0], [2,4], color='b')
plt.plot([2,0], [1,0], color='b')
plt.plot([3,4], [2,0], color='b')

#Plotta punktana í þríhyrningnum
plt.scatter(1, 2, c='b', s=20)
plt.scatter(2, 1, c='b', s=20)
plt.scatter(3, 2, c='b', s=20)

#Plotta punktana útfrá línunum
plt.scatter(4, 0, c='b', s=20)
plt.scatter(0, 0, c='b', s=20)
plt.scatter(0, 4, c='b', s=20)
