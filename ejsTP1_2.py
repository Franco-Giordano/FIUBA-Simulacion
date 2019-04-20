from ejsTP1_1 import realizacionesGCL

from matplotlib import pyplot as plt
import math

uniformes = realizacionesGCL()

resultados = [-20*math.log(1-u/(2**32)) for u in uniformes]

plt.hist(resultados)
plt.show()

#calculo de media, se espera 1/20
media = 1 / (sum(resultados) / len(resultados))
print(media)

#calculo de varianza, se espera 1/20^2
varianza = 1 / (sum(resultados) / len(resultados)) ** 2
print(varianza)