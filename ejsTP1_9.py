from ejsTP1_1 import realizacionesEstandarGCL

from matplotlib import pyplot as plt
import math

#calculo pn hasta que se queda igual
a,b = 0.2,0.5

probs = [b-a]
termino = False
i = 1
while not termino:
	nuevaProb = probs[0] * ((1-probs[0]) ** i)

	if nuevaProb == probs[i-1]:
		termino = True

	else:
		probs.append(nuevaProb)
		i += 1


print(probs)

muestras = realizacionesEstandarGCL()
