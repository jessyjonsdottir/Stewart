import matplotlib.pyplot as plt

#Þríhyrningurinn
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

#Sýnum nú myndina
plt.show()
