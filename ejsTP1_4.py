import random
import math
from matplotlib import pyplot as plt


#corregir: intentar generar una normal estandar y luego correrla

c = 4.365756303e6 #haciendo fX(t)/fY(t) se halla que este valor de t maximiza el cociente

realizaciones = []

def cociente(t):
	return (1/math.sqrt(2*math.pi*36)) * math.exp(t-40 -((t-40)**2 / 72)) * 1/c

for i in range(100000):

	t = random.expovariate(1) + 40 #la corro 40 asi la centro igual que la normal que quiero generar

	u = random.random()

	if u < cociente(t):
		#acepto la realizacion, ahora decido si es por encima de la media o por debajo

		u2 = random.random()

		if u2 < 0.5:
			realizaciones.append(t)

		else:
			realizaciones.append(-t)
print(realizaciones)
plt.hist(realizaciones)
plt.show()