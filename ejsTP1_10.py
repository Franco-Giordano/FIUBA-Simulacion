from ejsTP1_3 import realizacionesNormalEstandar

from matplotlib import pyplot as plt
from scipy.stats import norm

import numpy as np

realizaciones = realizacionesNormalEstandar()


#REVISAR: Falta calcular lo correspondiente al test y evaluar el resultado, que no se como hacer
#ordenadas = sorted(realizaciones)
#diferencias = [abs(???)]

x = np.linspace(norm.ppf(0.0001), norm.ppf(0.9999), 100) #la normal "real" la grafico entre los cuantiles z0.0001 y z0.9999
fig, ax = plt.subplots(1, 1)

rv = norm()
ax.plot(x, rv.cdf(x), 'k-', lw=2)

ax.hist(realizaciones,100, density=True, cumulative=True)
plt.show()