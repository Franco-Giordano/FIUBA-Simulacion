from ejsTP1_3 import realizacionesNormalEstandar

from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.stats import kstest


import numpy as np

realizaciones = realizacionesNormalEstandar()

stat, pvalue = kstest(realizaciones, 'norm', N=100000)

print(pvalue)

if pvalue <= 0.01:
	print("Hay evidencia suficiente para decir que las muestras NO vienen de una normal")

else:
	print("Las muestras provienen de una normal estandar")


fig, ax = plt.subplots(1, 1)
x = np.linspace(norm.ppf(0.0001), norm.ppf(0.9999), 100000) #la normal "real" la grafico entre los cuantiles z0.0001 y z0.9999

rv = norm()
ax.plot(x, rv.cdf(x), 'k-', lw=2)

ax.hist(realizaciones,100, density=True, cumulative=True)
plt.show()