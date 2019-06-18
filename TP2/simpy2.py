import simpy 
import random as rnd
#rnd.seed(1)

tiempos = []

class Solicitud:
	def __init__(self, env, lista_con_tiempos_procesamiento):
		self.env = env
		self.tiempo_ejecucion = self.generarTiempoEjecucion()
		self.tiempo_procesamiento = None #no se sabe hasta que se ejecute
		self.lista_tiempos= lista_con_tiempos_procesamiento


	def ejecutar(self, servidor):
		with servidor.request() as req:
			self.tiempo_procesamiento = env.now
			yield req
			yield self.env.timeout(self.tiempo_ejecucion)
			self.tiempo_procesamiento = env.now - self.tiempo_procesamiento #el tiempo sera lo que tardo entre que pidio el recurso y lo termino de usar (final - inicial) 
			self.lista_tiempos.append(self.tiempo_procesamiento)

	def generarTiempoEjecucion(self):
	
		uniforme = rnd.random()

		if uniforme <= 0.6:	#es A
			return rnd.uniform(65, 85)

		if 0.6 < uniforme <= 0.85:	#es B
			return rnd.uniform(45, 75)

		if 0.85 < uniforme:	#es C
			return rnd.uniform(70, 110)



def generar_solicitudes(environment, count, con_politica_round_robin=True):

	#son 6 servidores distintos de capacidad 1, NO es lo mismo a que tenga 1 servidor con capacidad 6
	servidores = [simpy.Resource(env, capacity=1) for i in range(6)]
	
	servidor_a_asignar = 0

	for i in range(count):


		solicitud = Solicitud(env, tiempos)
		environment.process(solicitud.ejecutar(servidores[servidor_a_asignar]))
		t = rnd.expovariate(1.0/45)
		yield environment.timeout(t)

		if con_politica_round_robin:
			servidor_a_asignar = (servidor_a_asignar+1)%6

		else: #politica aleatoria
			servidor_a_asignar = rnd.randint(0,5)


iteraciones = 1000000

env = simpy.Environment()
env.process(generar_solicitudes(env, iteraciones, con_politica_round_robin=True))
env.run() #termina cuando todos atendidos
print("Tardo {} milisegundos en ejecutar".format(env.now))
print("PROMEDIO CON ROUND ROBIND: ", sum(tiempos)/len(tiempos), '\n-------------------------------------\n\n')


tiempos = []
env = simpy.Environment()
env.process(generar_solicitudes(env, iteraciones, con_politica_round_robin=False))
env.run() #termina cuando todos atendidos
print("Tardo {} milisegundos en ejecutar".format(env.now))
print("PROMEDIO CON ALEATORIO: ", sum(tiempos)/len(tiempos))