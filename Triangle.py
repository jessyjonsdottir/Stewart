import matplotlib.pyplot as plt

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

#Sýnum nú myndina
plt.show()
