from ejsTP1_1 import realizacionesGCL

from matplotlib import pyplot as plt
import math

uniformes = realizacionesGCL()

resultados = [-20*math.log(1-u/(2**32)) for u in uniformes]


plt.title('Distribucion de realizaciones luego de transformar')
plt.ylabel('Cantidad de ocurrencias')
plt.xlabel('Muestra generada')

plt.hist(resultados)
plt.show()

#calculo de media, se espera 20
media = (sum(resultados) / len(resultados))
print(media)

#calculo de varianza, se espera 1/20^2
varianza = 1 / (sum(resultados) / len(resultados)) ** 2
print(varianza)