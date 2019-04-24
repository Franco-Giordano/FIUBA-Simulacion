from ejsTP1_1 import realizacionesEstandarGCL

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


resultados_previos = realizacionesEstandarGCL(1002)

resultados = resultados_previos[1:]
resultados_previos = resultados_previos[:-2]

resultados_siguientes = resultados[1:]
resultados = resultados[:-1]

plt.scatter(resultados_previos, resultados)

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(resultados_previos, resultados, resultados_siguientes)

plt.show()