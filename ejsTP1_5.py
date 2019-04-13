from ejsTP1_1 import GCL

from matplotlib import pyplot as plt
import math

x0 = 96771 # = 0.15*74620 + 0.25*100608 + 0.6*100710

multiplicador = 1013904223 

incremento = 1664525

modulo = 2**32

resultados = []

it = x0


for i in range(100000):

	it = GCL(multiplicador, incremento, modulo, it)

	u = it / (modulo-1)

	realizacion = 0

	if u <= 0.4:
		realizacion = 1

	if 0.4 < u <= 0.7:
		realizacion = 2

	if 0.7 < u <= 0.82:
		realizacion = 3

	if 0.82 < u <= 0.92:
		realizacion = 4

	if 0.92 < u:
		realizacion = 5

	resultados.append(realizacion)


plt.hist(resultados)
plt.show()
