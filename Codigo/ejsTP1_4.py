import random
import math
from matplotlib import pyplot as plt
from scipy.stats import norm

import numpy as np


c = 1.3 #haciendo fX(t)/fY(t) se halla que este valor (aproximado) de t maximiza el cociente

realizaciones_std = []

def cociente(t):
	return (1/math.sqrt(2*math.pi)) * math.exp(t - (t**2 / 2)) * 1/c

for i in range(100000):

	t = random.expovariate(1) #genero mi realizacion exponencial de media 1

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

x = np.linspace(norm.ppf(0.001, 40,6), norm.ppf(0.999,40,6), 100) #la normal "real" la grafico entre los cuantiles z0.001 y z0.999
fig, ax = plt.subplots(1, 1)

rv = norm(40,6)
ax.plot(x, rv.pdf(x), 'k-', lw=2)

ax.hist(realizaciones,100, density=True)
plt.show()


print('ESPERANZA: {}, VARIANZA: {}'.format(np.mean(realizaciones), np.var(realizaciones)))