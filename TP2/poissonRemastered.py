import random as rnd
#rnd.seed(1)
class Instruccion:

	def __init__(self, arribo_anterior, busca_con_cache=False, tiempo_arribo=0):

		if tiempo_arribo==0:
			self.tiempo_arribo = arribo_anterior + rnd.expovariate(250)
		else:
			self.tiempo_arribo = tiempo_arribo
		self.tiempo_ejecucion = self.generarTiempoEjecucion(busca_con_cache)
		self.tiempo_procesamiento = self.tiempo_ejecucion 	 # de momento es desconocido, se asume que no debe esperar

		# tiempo_ejecucion + tiempo_espera = tiempo_procesamiento


	def tiempo_en_el_que_termina_de_ejecutarse(self):
		return self.tiempo_arribo + self.tiempo_procesamiento

	def generarTiempoEjecucion(self,busca_con_cache):
		tiempo_ejecucion = 0
	
		es_simple = (rnd.random() <= 0.6)

		requiere_datos = (rnd.random() <= 0.65)

		if requiere_datos:

			if not busca_con_cache:
				tiempo_ejecucion += rnd.expovariate(2000)


			elif busca_con_cache:
				tiempo_ejecucion += rnd.expovariate(500) #busqueda en cache

				esta_en_cache = (rnd.random() <= 0.6)

				if not esta_en_cache:
					tiempo_ejecucion += rnd.expovariate(1500) #busqueda en memoria


		if es_simple:
			tiempo_ejecucion += rnd.expovariate(60)
		else: #si es compleja
			tiempo_ejecucion += rnd.expovariate(10)

		return tiempo_ejecucion

	def nuevo_tiempo_de_espera(self,t_espera):
		self.tiempo_procesamiento = self.tiempo_ejecucion + t_espera

	def convertir_a_con_cache(self):
		self.tiempo_ejecucion = self.generarTiempoEjecucion(busca_con_cache=True)
		return Instruccion(0,busca_con_cache=True,tiempo_arribo=self.tiempo_arribo)

	def __str__(self):
		return '<{}, {}>'.format(self.tiempo_arribo, self.tiempo_procesamiento)


cantidad_iteraciones = 10000


#creo vector de instrucciones, con sus tiempos de arribo sin buscar en cache
#el primero no debe esperar: no tiene a nadie antes que el
instrucciones_recibidas = [Instruccion(0, busca_con_cache=False)]

for i in range(cantidad_iteraciones-1):
	instrucciones_recibidas.append(Instruccion(instrucciones_recibidas[-1].tiempo_arribo))

instrucciones_con_cache = [ins.convertir_a_con_cache() for ins in instrucciones_recibidas.copy()]


tiempos = [i.tiempo_ejecucion for i in instrucciones_recibidas]
promedio_procesamiento = sum(tiempos) / len(instrucciones_recibidas)
print('PRUEBAS:\nSIN CACHE---------------------\nPromedio t ejecucion: ',promedio_procesamiento)



tiempos = [i.tiempo_ejecucion for i in instrucciones_con_cache]
promedio_procesamiento = sum(tiempos) / len(instrucciones_con_cache)
print('CON CACHE---------------------\nPromedio t ejecucion: ',promedio_procesamiento, '\n\n\n')

#print([(e.tiempo_arribo, e.tiempo_ejecucion) for e in instrucciones_recibidas]) 		chequeo
#DEBUG: instrucciones_recibidas = [Instruccion(a) for a in range(4000)]
print('---------------------SIN CACHE---------------------')
print("calculo esperas...")

for index,instruccion in enumerate(instrucciones_recibidas):

	#encuentro instrucciones entre t arribo y t_arribo+t_espera+t_ejecucion (cuando termine la actual)
	# es decir, busco las instrucciones afectadas

	termina_ejecutarse = instruccion.tiempo_en_el_que_termina_de_ejecutarse()

	afectadas = []
	for indice in range(index+1, len(instrucciones_recibidas)):

		actual = instrucciones_recibidas[indice]
		if actual.tiempo_arribo < termina_ejecutarse:
			afectadas.append(instrucciones_recibidas[indice])


	#a cada afectada debo avisarle que tiene un nuevo tiempo de espera, porque yo todavia seguia en ejecucion
	for af in afectadas:
		espera = instruccion.tiempo_en_el_que_termina_de_ejecutarse() - af.tiempo_arribo
		af.nuevo_tiempo_de_espera(espera)

print('calculo promedios...')
tiempos = [i.tiempo_procesamiento for i in instrucciones_recibidas]
promedio_procesamiento = sum(tiempos) / len(instrucciones_recibidas)
print('Promedio procesamiento: ',promedio_procesamiento)



print('\n---------------------CON CACHE---------------------')

print("calculo esperas")

for index,instruccion in enumerate(instrucciones_con_cache):

	#encuentro instrucciones entre t arribo y t_arribo+t_espera+t_ejecucion (cuando termine la actual)
	# es decir, busco las instrucciones afectadas

	termina_ejecutarse = instruccion.tiempo_en_el_que_termina_de_ejecutarse()

	afectadas = []
	for indice in range(index+1, len(instrucciones_con_cache)):

		actual = instrucciones_con_cache[indice]
		if actual.tiempo_arribo < termina_ejecutarse:
			afectadas.append(instrucciones_con_cache[indice])


	#a cada afectada debo avisarle que tiene un nuevo tiempo de espera, porque yo todavia seguia en ejecucion
	for af in afectadas:
		espera = instruccion.tiempo_en_el_que_termina_de_ejecutarse() - af.tiempo_arribo
		af.nuevo_tiempo_de_espera(espera)

print('calculo promedios')
tiempos = [i.tiempo_procesamiento for i in instrucciones_con_cache]
promedio_procesamiento = sum(tiempos) / len(instrucciones_con_cache)
print('Promedio procesamiento: ', promedio_procesamiento)



























# for muestra in range(cantidad_iteraciones):

	# tiempo_procesamiento_actual = 0
	
	# micros_hasta_arribo = rnd.expovariate(250)
	# tiempo_procesamiento_actual += micros_hasta_arribo

	# es_simple = (rnd.random() <= 0.6)

	# requiere_datos = (rnd.random() <= 0.65)

	# if requiere_datos:
	# 	tiempo_procesamiento_actual += rnd.expovariate(2000)

	# if es_simple:
	# 	tiempo_procesamiento_actual += rnd.expovariate(60)
	# else: #si es compleja
	# 	tiempo_procesamiento_actual += rnd.expovariate(10)

# 	tiempo_total += tiempo_procesamiento_actual

# print("Microsegundos promedio en procesar: ",tiempo_total/cantidad_iteraciones)





# tiempo_total_cache = 0

# for muestra in range(cantidad_iteraciones):

# 	tiempo_procesamiento_actual = 0
	
# 	micros_hasta_arribo = rnd.expovariate(250)
# 	tiempo_procesamiento_actual += micros_hasta_arribo

# 	es_simple = (rnd.random() <= 0.6)

# 	requiere_datos = (rnd.random() <= 0.65)

	# if requiere_datos:

	# 	tiempo_procesamiento_actual += rnd.expovariate(500) #busqueda en cache

	# 	esta_en_cache = (rnd.random() <= 0.6)

	# 	if not esta_en_cache:
	# 		tiempo_procesamiento_actual += rnd.expovariate(1500) #busqueda en memoria

# 	if es_simple:
# 		tiempo_procesamiento_actual += rnd.expovariate(60)
# 	else: #si es compleja
# 		tiempo_procesamiento_actual += rnd.expovariate(10)

# 	tiempo_total_cache += tiempo_procesamiento_actual

# print("Microsegundos promedio en procesar CON CACHE: ",tiempo_total_cache/cantidad_iteraciones)