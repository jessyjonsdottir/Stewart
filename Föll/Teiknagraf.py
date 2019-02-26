import numpy as np
import matplotlib.pyplot as plt

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
