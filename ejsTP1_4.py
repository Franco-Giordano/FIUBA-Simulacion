import random
import math
from matplotlib import pyplot as plt



c = 1.3 #haciendo fX(t)/fY(t) se halla que este valor (aproximado) de t maximiza el cociente

realizaciones_std = []

def cociente(t):
	return (1/math.sqrt(2*math.pi)) * math.exp(t - (t**2 / 2)) * 1/c

for i in range(100000):

	t = random.expovariate(1) #la corro 40 asi la centro igual que la normal que quiero generar

	u = random.random()

	if u < cociente(t):
		#acepto la realizacion, ahora decido si es por encima de la media o por debajo

		u2 = random.random()

		if u2 < 0.5:
			realizaciones_std.append(t)

		else:
			realizaciones_std.append(-t)

#hago el cambio de variable para que tenga una normal con media 40,desvio 6
realizaciones = [z*6 + 40 for z in realizaciones_std]

plt.hist(realizaciones,100)
plt.show()