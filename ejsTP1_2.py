from ejsTP1_1 import GCL

from matplotlib import pyplot as plt
import math

x0 = 96771 # = 0.15*74620 + 0.25*100608 + 0.6*100710

multiplicador = 1013904223 

incremento = 1664525

modulo = 2**32

resultados = []

u = x0

for i in range(100000):

	u = GCL(multiplicador, incremento, modulo, u)

	resultados.append(-20*math.log(1-u/modulo))


plt.hist(resultados)
plt.show()

#calculo de media, se espera 1/20
media = 1 / (sum(resultados) / len(resultados))
print(media)

#calculo de varianza, se espera 1/20^2
varianza = 1 / (sum(resultados) / len(resultados)) ** 2
print(varianza)