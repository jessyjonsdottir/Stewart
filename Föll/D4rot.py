import math as m
from numpy import sign

#x1 og x2 eru endar bilsins
#ef switch=1, þá athugar fallið hvort f(x) minnki ekki með hverju skrefi

def rotaleit(f,x1,x2,switch=1,tol=1.0e-09):
  #Athugum strax hvort x1 eða x2 séu rætur
	f1 = f(x1)
	if f1 == 0.0:
		return x1
	f2 = f(x2)
	if f2 == 0.0:
		return x2
  #Athugum hvort formerki fallgildis á endum bilsins séu jöfn; 
  #ef svo er er rótin ekki á bilinu
	if sign(f1) == sign(f2):
		return ('Rótin er ekki á bilinu')

	n = int(m.ceil(m.log(abs(x2-x1)/tol)/m.log(2.0)))
	for i in range(n):
		x3 = 0.5*(x1+x2); f3 = f(x3)
		if (switch == 1) and (abs(f3) > abs(f1)) \
		   and (abs(f3) > abs(f2)):
			return None
		if f3 == 0.0:
			return x3
		if sign(f2) != sign(f3):
			x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	return (x1 + x2)/2.0
