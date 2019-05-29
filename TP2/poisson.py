import random as rnd

tiempo_total = 0

cantidad_iteraciones = 10000000

for muestra in range(cantidad_iteraciones):

	tiempo_procesamiento_actual = 0
	
	micros_hasta_arribo = rnd.expovariate(250)
	tiempo_procesamiento_actual += micros_hasta_arribo

	es_simple = (rnd.random() <= 0.6)

	requiere_datos = (rnd.random() <= 0.65)

	if requiere_datos:
		tiempo_procesamiento_actual += rnd.expovariate(2000)

	if es_simple:
		tiempo_procesamiento_actual += rnd.expovariate(60)
	else: #si es compleja
		tiempo_procesamiento_actual += rnd.expovariate(10)

	tiempo_total += tiempo_procesamiento_actual

print("Microsegundos promedio en procesar: ",tiempo_total/cantidad_iteraciones)





tiempo_total_cache = 0

for muestra in range(cantidad_iteraciones):

	tiempo_procesamiento_actual = 0
	
	micros_hasta_arribo = rnd.expovariate(250)
	tiempo_procesamiento_actual += micros_hasta_arribo

	es_simple = (rnd.random() <= 0.6)

	requiere_datos = (rnd.random() <= 0.65)

	if requiere_datos:

		tiempo_procesamiento_actual += rnd.expovariate(500) #busqueda en cache

		esta_en_cache = (rnd.random() <= 0.6)

		if not esta_en_cache:
			tiempo_procesamiento_actual += rnd.expovariate(1500) #busqueda en memoria

	if es_simple:
		tiempo_procesamiento_actual += rnd.expovariate(60)
	else: #si es compleja
		tiempo_procesamiento_actual += rnd.expovariate(10)

	tiempo_total_cache += tiempo_procesamiento_actual

print("Microsegundos promedio en procesar CON CACHE: ",tiempo_total_cache/cantidad_iteraciones)