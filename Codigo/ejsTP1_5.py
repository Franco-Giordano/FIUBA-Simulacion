from ejsTP1_1 import realizacionesEstandarGCL

from matplotlib import pyplot as plt
import math

def realizacionesEJ5(cantidad=100000):

	realizacionesUniformes = realizacionesEstandarGCL(cantidad)

	resultados = []

	for u in realizacionesUniformes:

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

	return resultados

if __name__ == "__main__":

	plt.hist(realizacionesEJ5())
	plt.show()
