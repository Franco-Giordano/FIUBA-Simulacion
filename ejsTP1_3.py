from matplotlib import pyplot as plt
import random
import math

resultados = []


for i in range(100000):

	u1, u2 = random.random(), random.random()

	z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

	resultados.append(z)

plt.hist(resultados)
plt.show()

#media
media = sum(resultados) / len(resultados)
print(media)

#varianza ???????????????
