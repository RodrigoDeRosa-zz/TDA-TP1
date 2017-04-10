from iteradores_grafo import Bfs_iter
import heapq
VALOR_INALCANZABLE = 1000000000.0

class Graph(object):
    """
    Objeto generico que se comporta como un grafo de aristas sin sentido
    y con peso.
    Cada vertice se representa con un clave, que debe ser un string.
    A cada clave se le puede asignar un valor cualquiera.
    """


    def __init__(self):
        """
        El grafo se inicializa vacio.
        """

        self.vertices = {} #Diccionario de diccionarios. Matriz de adyacencias
        self.datos = {} #Diccionario de datos.
        self.tam = 0

    def __iter__(self):
        return self.vertices.__iter__()

    def __len__(self):
        """
        Devuelve la cantidad de vertices del grafo.
        """
        return len(self.vertices)

    def pertenece(self, clave):
        """
        Clave: String o Int que representa al vertice/nodo.

        Devuelve True si la clave pertenece al grafo, False de lo contrario.
        """

        return self.vertices.has_key(clave)

    def aniadir_vertice(self, clave, dato):
        """
        Clave: String o Int que representa al vertice/nodo.
        Dato: dato de cualquier tipo asociado.

        Devuelve False si la clave ya se encontraba, y True si la agrega.
        Si la clave ya existia, no cambia su dato.
        """

        if self.pertenece(clave):
            return False

        self.vertices[clave] = {}
        self.datos[clave] = dato
        self.tam += 1
        return True

    def obtener_dato(self, clave):
        """
        Clave: String o Int que representa al vertice/nodo.

        Devuelve el dato del nodo representado por la clave dada.
        Si la clave no pertenece al grafo, devuelve None.
        """
        if not self.pertenece(clave):
            return None

        return self.datos[clave]


    def cambiar_dato(self, clave, dato):
        """
        Clave: String o Int que representa al vertice/nodo.
        Dato: dato de cualquier tipo asociado.

        Modifica el valor de un vertice/nodo especificado y devuelve True.
        Si la clave no pertenece al grafo, devuelve False.
        """

        if not self.pertenece(clave):
            return False

        self.datos[clave] = dato

        return True

    def unir_vertices(self, clave_1, clave_2, peso):
        """
        Clave_1 y 2: String o Int que representa al vertice/nodo.
        Peso: tipo de dato que simbolise un peso.

        Une dos vertices/nodos existentes en el grafo con un determinado peso,
        y luego devuelve True.
        Si alguna de las dos claves no pertenece al grafo, no realiza nada y
        devuelve False.
        """

        if (not self.pertenece(clave_1)) or (not self.pertenece(clave_2)):
            return False

        self.vertices[clave_1][clave_2] = peso
        self.vertices[clave_2][clave_1] = peso

        return True

    def obtener_peso(self, clave_1, clave_2):
        """
        Clave_1 y 2: String o Int que representa al vertice/nodo.

        Devuelve el peso que une al vertice de Clave_1 con el de Clave_2.

        Si Clave_1 no conoce a Clave_2 levanta una excepcion.
        """

        if not self.conoce(clave_1, clave_2):
            raise IndexError

        return self.vertices[clave_1][clave_2]


    def conoce(self, clave_1, clave_2):
        """
        Clave_1 y 2: String o Int que representa al vertice/nodo.

        Devuelve True si un vertice/nodo conoce al otro, False de caso contrario.
        Levanta un error si alguna de las dos claves no pertenecen al grafo.
        """

        if (not self.pertenece(clave_1)) or (not self.pertenece(clave_2)):
            raise IndexError

        return self.vertices[clave_1].has_key(clave_2)

    def obtener_conocidos(self, clave):
        """
        Clave: String o Int que representa al vertice/nodo.

        Devuelve una lista con los vertices conocidos por el vertice
        identificado con el string clave.

        Si la clave no pertenece al grafo, levanta una excepcion.
        """

        if not self.pertenece(clave):
            raise IndexError

        return self.vertices[clave].keys()

    def obtener_aristas(self, clave):
    	"""
        Clave: String o Int que representa al vertice/nodo.

        Devuelve una lista con los pesos de las aristas por el vertice
        identificado con el string clave.

        Los pesos son un objeto definido por el susuario.

        Si la clave no pertenece al grafo, levanta una excepcion.
        """

        if not self.pertenece(clave):
            raise IndexError

        aristas = []
        for nodo_conocido in self.vertices[clave].keys():
        	aristas.append(self.vertices[clave][nodo_conocido])

        return aristas

    def es_conexo(self):
        """
        Devuelve True si el grafo es conexo. False de lo contrario.
        """
        if len(self.vertices) == 0:
            return False

        iter = Bfs_iter(self, self.vertices.keys()[0])
        count = 0

        while not iter.al_final():
            iter.siguiente()
            count += 1

        return count == len(self.vertices)


###################################################################################
#                   FUNCIONES PUBLICAS
###################################################################################


def grafo_a_estrella(grafo, origen, destino, heuristica):
    """
    Recibe un objeto del tipo grafo un valor de origen y otro de destino.
    La funcion heuristica que a la vez recibe debe ser del estilo:
    heuristica(dato vertice 1, dato vertice 2, peso entre vertice 1 y 2) y debe devolver un entero.

    Devuelve un objeto del tipo grafo con la cualidad de ser de a estrella.
    """

    if type(grafo) != Graph:
        raise TypeError
    grafo_a = Graph()
    if not len(grafo): return grafo_minimo

    padre = {}
    distancia = {}
    visitados = {}
    cola = []

    for vertice in grafo:
        padre[vertice] = None
        distancia[vertice] = VALOR_INALCANZABLE
        visitados[vertice] = False

    distancia[str(origen)] = 0
    grafo_a.aniadir_vertice(str(origen), grafo.obtener_dato(str(origen)))
    heapq.heappush(cola, origen)

    while len(cola) > 0:
        minimo = heapq.heappop(cola)
        minimo = str(minimo)
        if int(minimo) == destino:
            actual = minimo

            while padre[actual]:
                grafo_a.aniadir_vertice(actual, grafo.obtener_dato(actual))
                grafo_a.aniadir_vertice(padre[actual], grafo.obtener_dato(padre[actual]))
                grafo_a.unir_vertices(actual, padre[actual], grafo.obtener_peso(actual, padre[actual]))
                actual = padre[actual]

            return grafo_a

        for conocido in grafo.obtener_conocidos(minimo):
            distancia_v = distancia[minimo] + heuristica(grafo.obtener_dato(minimo), grafo.obtener_dato(conocido), grafo.obtener_peso(minimo,conocido))
            if distancia[conocido] > distancia_v and visitados[conocido] == False:
                padre[conocido] = minimo
                distancia[conocido] = distancia_v
                visitados[conocido] = True
                if int(conocido) not in cola:
                    heapq.heappush(cola, int(conocido))





def grafo_tendido_minimo(grafo, peso_obtener):
    """
    Recibe un objeto del tipo grafo y una funcion de lectura de peso.
    La funcion de lectura debe ser del estilo:
    peso_obtener(peso1) y debe devolver el valor del peso.

    Devuelve un objeto del tipo grafo con la cualidad de ser de tendido
    minimo.
    """

    if type(grafo) != Graph:
        raise TypeError
    grafo_minimo = Graph()
    if not len(grafo): return grafo_minimo

    padre = {}
    distancia = {}
    cola = []

    for vertice in grafo:
        padre[vertice] = None
        distancia[vertice] = VALOR_INALCANZABLE
        heapq.heappush(cola, (distancia[vertice], vertice))
        grafo_minimo.aniadir_vertice(vertice, grafo.datos[vertice])

    primer_vertice = grafo.vertices.keys()[0]
    distancia[primer_vertice] = 0
    cola = _actualizar_cola_prioridad(cola, distancia)

    while len(cola) > 0:
        minimo = heapq.heappop(cola)[1]
        for conocido in grafo.obtener_conocidos(minimo):
            if _pertenece_cola(cola, conocido) and (distancia[conocido] > peso_obtener(grafo.vertices[minimo][conocido])):
                padre[conocido] = minimo
                distancia[conocido] = peso_obtener(grafo.vertices[minimo][conocido])
            cola = _actualizar_cola_prioridad(cola, distancia)

    for vertice in grafo:
        if padre[vertice] == None: continue
        grafo_minimo.unir_vertices(vertice, padre[vertice], grafo.vertices[vertice][padre[vertice]])

    return grafo_minimo

def crear_vertices_aux():
    v = {}
    for w in self.vertices:
        #Para cada vertice en el grafo, seteamos
        #visitado, low, num.
        v[w] = [false,0,0]
def obtener_punto_articulacion(self):
  counter = 0
  puntos_articulacion = []
  vertices_aux = crear_vertices_aux()

  self.obterner_punto_articulacion_rec(puntos_articulacion, vertices[0],counter)
  return puntos_articulacion

def obterner_punto_articulacion_rec(self, puntos_articulacion, v, counter):
  v.visitado=True
  counter += 1
  v.low = counter
  v.num = counter

  for w in





###################################################################################
#                   FUNCIONES PRIVADAS
###################################################################################

def _pertenece_cola(cola, clave):
    """
    Devuelve True si pertenece a la cola de prioridad. False si no.
    """
    for elemento in cola:
        if elemento[1] == clave:
            return True
    return False

def _actualizar_cola_prioridad(cola, distancia):
    """
    Cola: Cola a ser actualizada. Formato (distancia, clave)
    Distancia: Diccionario {clave : distancia}
    """
    cola_aux = []

    for elemento in cola:
        cola_aux.append((distancia[elemento[1]], elemento[1]))

    heapq.heapify(cola_aux)

    return cola_aux
