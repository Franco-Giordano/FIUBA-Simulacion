
from matplotlib import pyplot as plt


#GCL

def GCL(multi, inc, mod, x0):
	#x0 = valor anterior

	return ((multi * x0) + inc) % mod


if __name__ == "__main__":
	x0 = 96771 # = 0.15*74620 + 0.25*100608 + 0.6*100710

	multiplicador = 1013904223 

	incremento = 1664525

	modulo = 2**32

	resultados_A = []

	iteracion_actual = x0

	for i in range(5):

		iteracion_actual = GCL(multiplicador, incremento, modulo, iteracion_actual)
		print(iteracion_actual)
		resultados_A.append(iteracion_actual)

	resultados_B = []

	iteracion_actual = x0
	for i in range(100000):

		iteracion_actual = GCL(multiplicador, incremento, modulo, iteracion_actual)
		resultados_B.append(iteracion_actual / (modulo-1))


	plt.hist(resultados_B)
	plt.show()