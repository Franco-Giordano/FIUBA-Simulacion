from ejsTP1_1 import realizacionesEstandarGCL

from matplotlib import pyplot as plt

from scipy import stats as sp


a,b = 0.2,0.5

#calculo las probabilidades, corto cuando ya no distingo diferencia
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



muestras = realizacionesEstandarGCL()

#calculo cantidad de veces que cai 0 afuera, 1 afuera, 2 afuera...
primero = True
contador_local = 0
numeros = {}
for x in muestras:
	if (x>=0.2 and x<=0.5 and primero):
		primero = False
	if (x>=0.2 and x<=0.5 and not primero):
		veces = numeros.get(contador_local,0)
		numeros[contador_local] = veces + 1
		contador_local = 0
	if ((x<0.2 or x>0.5) and not primero):
		contador_local+=1


#ajusto para que sean frecuencias
total = sum(numeros.values())
for k in numeros.keys():
	numeros[k] /= total

#lo paso a lista y relleno con 0 donde no tuve apariciones
lista = []
for i in range(2084):
	lista.append(numeros.get(i,0))

print(probs, lista)

print(sp.chisquare(lista, f_exp=probs))