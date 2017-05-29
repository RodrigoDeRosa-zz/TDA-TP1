from graph import Graph
from dfs import DFS

class Tarjan(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def setGrafo(self, grafo):
        self.grafo = grafo

    def getPuntosDeArticulacion(self):
        #Se toma el primer vertice del grafo
        vertice = self.grafo.get_vertices().keys()[0]

        #Creador de grafos dfs
        dfs = DFS(vertice, self.grafo) 

        #se obtiene el DFS del grafo. Este guarda en el valor de cada vertice un 
        #tiempo de descubrimiento. Tambien se obtiene una lista con los padres 
        #de cada vertice
        grafoDFS, padres = dfs.getGrafoDFS()

        #se obtiene una lista con el lowpoint de cada vertice 
        lowList = dfs.getLowList(padres, grafoDFS)

        #se obtienen los puntos de articulacion del grafo original
        puntosArticulacion = dfs.getPuntosDeArticulacion(padres, grafoDFS, lowList)

        return puntosArticulacion
