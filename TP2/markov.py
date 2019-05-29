import math

import matplotlib.pyplot as plt

import numpy as np

estados = 51

ESTADOS_POSIBLES = [i for i in range(estados)]


p = 0.7

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def P(i,j):
	if j>=i: #REVISAR ERROR DE EXPONENETE EN ENUNCIADOAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
		return nCr(estados-1, j-i)*(p**(j-i))*((1-p)**(estados-1-j+i))

	else: #CHEQUEAR EL RANGE ESTADOS+1 Y EL I-1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
		return (1-sum([P(i,v) for v in range(i,estados)]))/(i)


transiciones = [[0 for i in range(estados)] for a in range(estados)]

for i in range(estados):
	for j in range(estados):

		transiciones[i][j] = P(i,j)


print([sum(v) for v in transiciones]) #chequeo




evolucion = [0] #elijo 0 el est inicial, si quiero al azar uso np.random.choice(ESTADOS_POSIBLES)


for i in range(100):

	estado_actual = evolucion[-1]

	probabilidades = transiciones[estado_actual]

	evolucion.append(np.random.choice(ESTADOS_POSIBLES, p=probabilidades))

print(sum(evolucion)/101)

plt.step([i for i in range(101)], evolucion)
plt.show()






frecuencias = [0 for i in range(estados)]
evolucion = [0] #elijo 0 el est inicial, si quiero al azar uso np.random.choice(ESTADOS_POSIBLES)


for i in range(100000):

	estado_actual = evolucion[-1]

	probabilidades = transiciones[estado_actual]

	evolucion.append(np.random.choice(ESTADOS_POSIBLES, p=probabilidades))

	frecuencias[estado_actual] += 1


plt.hist(evolucion)
plt.show()



print(frecuencias[0]/100001)



print(sum(frecuencias[41:])/100001)
