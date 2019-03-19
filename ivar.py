import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt

def hge1(a):
	p=np.arange(-20,1)
	f=lambda x: np.sin(x)
	df=lambda x: np.cos(x);
	err1,err2,err3=[],[],[]
	for
		i in range(len(p)):
		h=10.0**p[i]
		err1+=[(f(a+h) - f(a-h))/(2*h)-df(a)]
		err2+=[(f(a+h) - f(a))/h-df(a)]
		h=2*h;
		err3+=[(f(a-h)-8*f(a-h/2)+8*f(a+h/2) - f(a+h))/(6*h)-df(a)]
plt.plot(p,np.log10(np.abs(err1)),'b')
plt.plot(p,np.log10(np.abs(err2)),'r')
plt.plot(p,np.log10(np.abs(err3)),'g')
