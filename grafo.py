# coding=utf-8

from heap import Heap

INFINITO = -1
DISTANCIA = 1
HABITANTES = 3
COORD = 1
LONGITUD = 0
LATITUD = 1

class Vertice(object):

	def __init__(self, clave, dato = None):
		"""Crea un objeto de clase Vertice. Recibe:
			- clave : cadena que identifica al vertice.
			- dato (opc.) : dato de cualquier tipo al almacenar."""
		self.clave = clave
		self.dato = dato
		self.visitado = False
		self.low = 0
		self.num = 0

	def __cmp__(self, other):
		"""Comparación de vertices. Dos vertices son iguales sii tienen
		la misma clave."""
		if other is None: return 1
		if self.clave == other.clave: return 0
		return 1

	def __str__(self):
		cadena = str(self.clave)
		return cadena

	def devolver_clave(self):
		return self.clave

class Arista(object):

	def __init__(self, clave, origen, destino, peso):
		"""Crea un objeto de clase Arista. Recibe:
			- clave : identificador único de la arista.
			- origen / destino : objetos de clase Vertice que se conectan.
			- peso : indica el peso de la Arista."""
		self.clave = clave
		self.origen = origen
		self.destino = destino
		self.peso = peso

	def __str__(self):
		cadena = "Arista: " + str(self.clave) + "    "
		cadena += "Origen: " + str(self.origen) + "   "
		cadena += "Destino: " + str(self.destino) + "    "
		if self.peso:
			cadena += "Peso: " + str(self.peso)
		return cadena

class Grafo(object):

	def __init__(self, vertices = [], aristas = [], adyacencia = {}):
		"""Crea un objeto de clase Grafo. Es un grafo simple y con vertices
		con claves diferentes. Recibe:
			- vertices (opc.) : lista de Vertices del grafo.
			- aristas (opc.) : lista de Aristas del grafo.
			- adyacencia (opc.) : diccionario que representa la matriz de adyacencia
			del grafo."""
		self.vertices = vertices
		self.aristas = aristas
		self.adyacencia = self._crear_matriz_adyacencia()

	def _crear_matriz_adyacencia(self):
		"""Crea la matriz de adyacencia que relaciona a todos los Vertices del grafo
		a partir de la informacion de las Aristas."""
		adyacencia = {}

		for vertice in self.vertices:
			adyacencia[vertice] = {}
			for arista in self.aristas:
				if vertice == arista.origen:
					adyacencia[vertice][arista.destino] = arista.peso
				elif vertice == arista.destino:
					adyacencia[vertice][arista.origen] = arista.peso
				else: continue

		return adyacencia

	def __str__(self):
		cadena = ""
		for vertice in self.vertices:
			cadena += str(vertice) + "-"
		return cadena[:len(cadena)-1]

	def buscar_vertice(self,dato):
		"""Dado un dato busca un vertice y lo devuelve"""
		for ver in self.vertices:
			if ver.devolver_clave() == dato:
				return ver
		return None

	def agregar_vertice(self, vertice):
		"""Agrega al conjunto de Vertices del grafo lo recibido:
			- vertice : objeto de clase Vertice"""
		self.vertices.append(vertice)

	def agregar_arista(self, arista):
		"""Agrega al conjunto de Aristas del grafo lo recibido:
			- arista : objeto de clase Arista.
		Se actualiza la matriz de adyacencia, uniendo los vertices de la
		arista en el grafo."""
		self.aristas.append(arista)
		if not self.adyacencia.has_key(arista.destino):
			self.adyacencia[arista.destino] = {}
		if not self.adyacencia.has_key(arista.origen):
			self.adyacencia[arista.origen] = {}
		self.adyacencia[arista.destino][arista.origen] = arista.peso
		self.adyacencia[arista.origen][arista.destino] = arista.peso

	def borrar_arista(self, arista):
		"""Elimina del conjunto de Aristas del grafo lo recibido:
			- arista : objeto de clase Arista.
		Se actualiza la matriz de adyacencia, separando los Vertices que
		ésta unía."""
		self.aristas.remove(arista)
		del self.adyacencia[arista.destino][arista.origen]
		del self.adyacencia[arista.origen][arista.destino]

	def borrar_vertice(self, vertice):
		"""Elimina del conjunto de Vertices del grafo lo recibido:
			- vertice : objeto de clase Vertice.
		Se actualiza la matriz de adyacencia, eliminando las Aristas que
		unían al vertice recibido con algún otro y borrando todas las
		ralaciones."""
		self.vertices.remove(vertice)
		for adyacente in self.adyacencia[vertice]:
			del self.adyacencia[adyacente][vertice]
		del self.adyacencia[vertice]

		i = 0
		while i < len(self.aristas):
			arista = self.aristas[i]
			if vertice == arista.origen or vertice == arista.destino:
				self.aristas.remove(arista)
				i -= 1
				continue
			i += 1

	def manh(self, vertice, destino):
		manhattan = abs(vertice.dato[COORD][LONGITUD] - destino.dato[COORD][LONGITUD]) + abs(vertice.dato[COORD][LATITUD] - destino.dato[COORD][LATITUD])
		return manhattan

	def camino_optimo(self, origen, destino):
		"""Busca el camino optimo entre el origen y el destino, ambos Vertices."""
		padre = {}
		padre[origen] = None
		distancia = {}
		habitantes = {}
		for vertice in self.vertices:
			distancia[vertice] = INFINITO
			habitantes[vertice] = INFINITO
		distancia[origen] = 0
		habitantes[origen] = origen.dato[HABITANTES]
		heap = Heap()
		heap.encolar((origen.dato[HABITANTES], 0, origen))
		while not heap.esta_vacio():
			habs, peso, vertice = heap.desencolar()
			if vertice == destino:
				return self._generar_camino(padre, origen, destino)
			for w in self.adyacencia[vertice]:
				if (distancia[w] > distancia[vertice] + self.adyacencia[vertice][w][DISTANCIA] + self.manh(w, destino) or habitantes[w] < w.dato[HABITANTES] + habitantes[vertice]) or distancia[w] == INFINITO:
					distancia[w] = distancia[vertice] + self.adyacencia[vertice][w][DISTANCIA] + self.manh(w, destino)
					habitantes[w] = w.dato[HABITANTES] + habitantes[vertice]
					padre[w] = vertice
					heap.encolar((habitantes[w], distancia[w], w))
		return None

	def _generar_camino(self, padre, origen, destino):
		"""Genera una lista donde se guardan, en orden, los vertices
		visitados en el camino del origen al destino."""
		camino_inv = []
		vertice = destino
		while padre[vertice] != None and padre[vertice] not in camino_inv:
			camino_inv.append(vertice)
			vertice = padre[vertice]
		camino = [origen]
		i = len(camino_inv) - 1
		while i > 0:
			camino.append(camino_inv[i])
			i -= 1
		camino.append(destino)
		return camino

	def obtener_arbol_generador(self, origen):
		"""Genera un arbol de tendido mínimo que comienza en el Vertice recibido."""
		visitado = {}
		camino = []
		for vertice in self.vertices:
			visitado[vertice] = False
		visitado[origen] = True
		heap = Heap()
		for w in self.adyacencia[origen]:
			heap.encolar((self.adyacencia[origen][w][DISTANCIA], origen, w))
		cantidad = 1
		largo = len(self.vertices)
		while not heap.esta_vacio() and cantidad < largo:
			(peso, padre_v, vertice) = heap.desencolar()
			if not visitado[vertice]:
				visitado[vertice] = True
				cantidad += 1
				camino.append((vertice, padre_v))
				for w in self.adyacencia[vertice]:
					if not visitado[w]:
						heap.encolar((self.adyacencia[vertice][w][DISTANCIA], vertice, w))
		return camino

	def obtener_punto_articulacion(self):
		counter = 0
		puntos_articulacion = []
		self.obterner_punto_articulacion_rec(puntos_articulacion, vertices[0],counter)
		return puntos_articulacion

	def obterner_punto_articulacion_rec(self, puntos_articulacion, v, counter):
		v.visitado=True
		counter += 1
		v.low = counter
		v.num = counter 
