from graph import Graph
from dfs import DFS

class Kosaraju(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def setGrafo(self, grafo):
        self.grafo = grafo

    def getComponentesConexas(self):
        """Devuelve una lista con grafos sin uniones que contienen los
        vertices de cada componente conexa"""
        #obtengo una lista de tuplas de vertices ordenada por tiempos de finalizado
        dfs = DFS() #Creador de grafos dfs

        orden = self.obtener_lista_vertices_numerado(dfs)

        #Invertimos el grafo original
        g_invertido = self.grafo.invertir()

        #Recorremos el grafo invertido en orden calculado
        componentes =[]

        cantVert = len(g_invertido.get_vertices().keys())
        visitados = [None]*cantVert

        #segundo DFS utilizando el orden obtenido en forma de pila
        #condicion de corte: que nos quedemos sin nodos para recorrer
        while(len(orden) > 0):
            x = orden.pop()[1]
            if (not visitados[int(x)]):
                grafo_aux, tiempo = dfs.getGrafoDFS_con_tiempos(g_invertido, x, visitados)
                componentes.append(grafo_aux.vertices)

        return componentes

#------ FUNCIONES AUXILIARES ------#

    def obtener_lista_vertices_numerado(self, dfs):
        """Funcion que nos devuelve una lista ordenada que contiene
        la numeracion como clave de cada vertice
        Recibe un objeto dfs para recorrer el grafo"""

        lista = []

        for x in self.grafo.vertices:
            cantVert = len(self.grafo.get_vertices().keys())
            visitados = [None]*cantVert
            grafo_aux, tiempo = dfs.getGrafoDFS_con_tiempos(self.grafo, x, visitados)
            lista.append((tiempo,x))

        #para optimizar usar itemgetter
        lista.sort(key=lambda tup: (tup[0], tup[1]))

        return lista
