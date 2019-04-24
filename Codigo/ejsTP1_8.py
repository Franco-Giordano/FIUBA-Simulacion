from scipy import stats as sp
import matplotlib.pyplot as plt

from ejsTP1_5 import realizacionesEJ5

realizaciones = realizacionesEJ5()

#cuento las apariciones
obs_values = [0 for i in range(5)]
for i in realizaciones:
	obs_values[i-1] += 1


expected_p_values = [0.4, 0.3, 0.12, 0.1, 0.08]
expected_values = [100000*i for i in expected_p_values]


statistic, pvalue = sp.chisquare(obs_values, f_exp=expected_values)

print(statistic, pvalue)


#si pvalue <= alfa entonces rechazo H0 (digo que son distintas)

if pvalue <= 0.01:
	print("las distribuciones NO son las mismas")

else:
	print("las distribuciones coinciden")