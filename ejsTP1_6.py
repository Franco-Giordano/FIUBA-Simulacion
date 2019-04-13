import random
from matplotlib import pyplot as plt

xs, ys = [],[]

for i in range(100000):

	u1 = random.uniform(-1,1)

	u2 = random.uniform(-1,1)

	if u1**2 + u2**2 <= 1: #si pertenece al circulo unitario...

		xs.append(u1)
		ys.append(u2)


plt.scatter(xs,ys)
plt.show()