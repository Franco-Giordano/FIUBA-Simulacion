import simpy 
import random as rnd
#rnd.seed(1)

tiempos = []

class Instruccion:
	def __init__(self, env, lista_con_tiempos_procesamiento,busca_con_cache=False):
		self.env = env
		self.tiempo_ejecucion = self.generarTiempoEjecucion(busca_con_cache)
		self.tiempo_procesamiento = None #no se sabe hasta que se ejecute
		self.lista_tiempos= lista_con_tiempos_procesamiento


	def ejecutar(self, procesador):
		with procesador.request() as req:
			self.tiempo_procesamiento = env.now
			yield req 
			yield self.env.timeout(self.tiempo_ejecucion)
			self.tiempo_procesamiento = env.now - self.tiempo_procesamiento #el tiempo sera lo que tardo entre que pidio el recurso y lo termino de usar (final - inicial) 
			self.lista_tiempos.append(self.tiempo_procesamiento)

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



def generar_instrucciones(environment, count, busca_con_cache=False):
	procesador = simpy.Resource(env, capacity = 1)
	for i in range(count):
		instruccion = Instruccion(env, tiempos,busca_con_cache)
		environment.process(instruccion.ejecutar(procesador))
		t = rnd.expovariate(250)
		yield environment.timeout(t)



iteraciones = 10000

env = simpy.Environment()
env.process(generar_instrucciones(env, iteraciones, busca_con_cache=False))
env.run() #termina cuando todos atendidos
print("Tardo {} microsegundos en ejecutar".format(env.now))
print("PROMEDIO SIN CACHE: ", sum(tiempos)/len(tiempos), '\n-------------------------------------\n\n')


tiempos = []
env = simpy.Environment()
env.process(generar_instrucciones(env, iteraciones, busca_con_cache=True))
env.run() #termina cuando todos atendidos
print("Tardo {} microsegundos en ejecutar".format(env.now))
print("PROMEDIO CON CACHE: ", sum(tiempos)/len(tiempos))