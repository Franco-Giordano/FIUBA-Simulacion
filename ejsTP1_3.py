from matplotlib import pyplot as plt
import random
import math
import numpy as np


def realizacionesNormalEstandar(cant=100000):
	resultados = []

	for i in range(cant):

		u1, u2 = random.random(), random.random()

		z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

		resultados.append(z)

	return resultados

if __name__ == "__main__":

	resultados = realizacionesNormalEstandar()

	plt.hist(resultados)
	plt.show()

	#media
	media = sum(resultados) / len(resultados)
	print("ESPERANZA: ",media)

	#varianza
	print("VARIANZA: ",np.var(resultados))