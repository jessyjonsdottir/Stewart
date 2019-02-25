import numpy as np
import matplotlib.pyplot as plt



def teiknamynd( x_0, x_1, x_2, y_0, y_1, y_2, xb_0, xb_1, xb_2, yb_0, yb_1, yb_2):

#Þríhyrningurinn
	plt.plot([x_0,x_1,x_2,x_0], [y_0,y_1,y_2,y_0], color='b')
	plt.ylim(-2,7)
	plt.xlim(-2,7)

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
