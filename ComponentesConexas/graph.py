#from iteradores_grafo import Bfs_iter
import heapq
VALOR_INALCANZABLE = 1000000000.0

class Graph(object):
    """
    Objeto generico que se comporta como un grafo de aristas sin sentido
    y con peso.
    Cada vertice se representa con un clave, que debe ser un string.
    A cada clave se le puede asignar un valor cualquiera.
    """


    def __init__(self, dir = False):
        """
        El grafo se inicializa vacio.
        """

        self.vertices = {} #Diccionario de diccionarios. Matriz de adyacencias
        self.datos = {} #Diccionario de datos.
        self.tam = 0
        self.dirigido = dir

    def __iter__(self):
        return self.vertices.__iter__()

    def __len__(self):
        """
        Devuelve la cantidad de vertices del grafo.
        """
        return len(self.vertices)

    def __str__(self):
        return str(self.vertices)

    def get_vertices(self):
        return self.vertices

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
        Si el grafo es dirigido, solamente une la clave 1 apuntando a 2.
        """

        if (not self.pertenece(clave_1)) or (not self.pertenece(clave_2)):
            return False

        self.vertices[clave_1][clave_2] = peso
        if(not self.dirigido):
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


    def crear_vertices_aux(self):
        v = {}
        for w in self.vertices:
            #Para cada vertice en el grafo, seteamos
            #visitado, low, num, el padre y la raiz.
            v[w] = [False,0,0,None, False]
        return v

    def invertir(self):
        """Funcion que se encarga de invertir un grafo dirigido.
        En caso de que el grafo no sea dirigido se devuelve el mismo grafo."""
        if(not self.dirigido):
            return self

        g = Graph(True)

        for v in self.vertices:
            g.aniadir_vertice(v,0)
            for x in self.obtener_conocidos(v):
                g.aniadir_vertice(x,0)
                g.unir_vertices(x,v,0)
        return g

    def obtener_dic_vertices_numerado(self):
        """Funcion que nos devuelve un diccionario que contiene
        la numeracion como clave de cada vertice"""
        dic = {}

        for x in self.vertices:
            orden = self.datos[x]
            dic[orden]=x

        return dic


    def obtener_componentes_conexas(self,vertice_comienzo):

        #obtengo el grafo de dfs del grafo original
        g_dfs = self.obtener_grafo_dfs(vertice_comienzo)

        #Invertimos el grafo original
        g_invertido = self.invertir()

        #obtengo un diccionario que contiene la numeracion como clave
        #y el string como valor.
        dic_numeraciones = g_dfs.obtener_dic_vertices_numerado()

        #Recorremos el grafo invertido en orden de numeracion decreciente
        maximo_actual=len(dic_numeraciones)
        componentes =[]
        tam_aux = 0
        visitados_totales = []

        #condicion de corte: que nos quedemos sin nodos para recorrer
        # o que ya se hayan visitado todos los nodos.
        while(maximo_actual>0 and self.tam > tam_aux):
            x=dic_numeraciones[maximo_actual]
            if(not x in visitados_totales):
                grafo_aux = g_invertido.obtener_grafo_dfs(x)
                componentes.append(grafo_aux)
                tam_aux += len(grafo_aux)
                #agregamos a la lista los vertices ya visitados.
                visitados_totales += grafo_aux.vertices.keys()
            maximo_actual -= 1

        return componentes


    def obtener_punto_articulacion(self, vertice_comienzo):
        """Funcion que recibe el vertice de comienzo como un string"""

        g = self.obtener_grafo_dfs(vertice_comienzo)
        puntos_articulacion=[]
        for x in g.vertices:
            if(len(g.obtener_conocidos(x)) >=2):
                puntos_articulacion.append(x)
        return puntos_articulacion


    def obtener_grafo_dfs(self, v):

        g = Graph(True)
        #LLeva el control de los vertices visitados
        visitados = []
        padres = []
        stack = []
        stack.append(v)
        contador=0

        for i in range(0,self.tam):
            visitados.append(False)
            padres.append(None)

        while (len(stack)>0):
            w=stack.pop()
            if(not visitados[int(w)]):
                contador +=1
                g.aniadir_vertice(w,contador)
                if(padres[int(w)] is not None):
                    g.unir_vertices(padres[int(w)],w,0)
                visitados[int(w)] = True
                stack_aux = []
                vertices_vecinos = self.obtener_conocidos(w)
                for x in vertices_vecinos:
                    if(not visitados[int(x)]):
                        stack_aux.append(x)
                        padres[int(x)] = w
                while(len(stack_aux)>0):
                    stack.append(stack_aux.pop())
        return g


def prueba():

    g=Graph(True)
    g.aniadir_vertice("0",0)
    g.aniadir_vertice("1",0)
    g.aniadir_vertice("2",0)
    g.aniadir_vertice("3",0)
    g.aniadir_vertice("4",0)
    g.aniadir_vertice("5",0)
    g.aniadir_vertice("6",0)

    g.unir_vertices("0","1",0)
    g.unir_vertices("1","2",0)
    g.unir_vertices("2","3",0)
    g.unir_vertices("3","1",0)

    g.unir_vertices("0","4",0)
    g.unir_vertices("4","5",0)
    g.unir_vertices("5","6",0)
    g.unir_vertices("6","4",0)

    a=g.obtener_componentes_conexas("0")
    for x in a:
        print x.vertices
prueba()
