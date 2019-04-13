from ejsTP1_1 import GCL

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x0 = 96771 # = 0.15*74620 + 0.25*100608 + 0.6*100710

multiplicador = 1013904223 

incremento = 1664525

modulo = 2**32

resultados_previos = []

it = x0

for i in range(100002):

	it = GCL(multiplicador, incremento, modulo, it)

	u = it / (modulo-1)

	resultados_previos.append(u)

# roto las listas, no se si esta bien. Falta chequear y hacer el analisis

resultados = resultados_previos[1:]
resultados_previos = resultados_previos[:-2]

resultados_siguientes = resultados[1:]
resultados = resultados[:-1]



fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(resultados_previos, resultados, resultados_siguientes)

plt.show()