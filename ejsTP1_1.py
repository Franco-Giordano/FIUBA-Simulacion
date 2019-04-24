
from matplotlib import pyplot as plt


#GCL

def GCL(multi, inc, mod, x0):
	#x0 = valor anterior

	return ((multi * x0) + inc) % mod

def realizacionesGCL(cantidad=100000):
	x0 = 96771 # = 0.15*74620 + 0.25*100608 + 0.6*100710

	multiplicador = 1013904223 

	incremento = 1664525

	modulo = 2**32

	resultados = []

	iteracion_actual = x0

	for i in range(cantidad):

		iteracion_actual = GCL(multiplicador, incremento, modulo, iteracion_actual)
		resultados.append(iteracion_actual)

	return resultados

def realizacionesEstandarGCL(cantidad=100000):
	return [i/(2**32) for i in realizacionesGCL(cantidad=cantidad)]



if __name__ == "__main__":
	
	resultados_A = realizacionesGCL(cantidad=5)

	print(resultados_A)

	resultados_B = realizacionesEstandarGCL()

	plt.title('Distribucion de realizaciones con GCL')
	plt.ylabel('Cantidad de ocurrencias')
	plt.xlabel('Muestra generada')
	plt.hist(resultados_B)
	plt.show()
