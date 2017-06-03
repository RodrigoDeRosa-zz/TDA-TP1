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

        #se obtienen los puntos de articulacion del DFS
        puntosArticulacion = dfs.getPuntosDeArticulacion()

        return puntosArticulacion
