from graph import Graph
from dfs import DFS

class Tarjan(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def setGrafo(self, grafo):
        self.grafo = grafo

    def getPuntosDeArticulacion(self):
        vertice = self.grafo.get_vertices().keys()[0] #Se toma el primer vertice del grafo

        dfs = DFS() #Creador de grafos dfs

        grafoDFS = dfs.getGrafoDFS(self.grafo, vertice)
        puntosArticulacion = []

        for vertice in grafoDFS.get_vertices().keys():
            if len(grafoDFS.obtener_conocidos(vertice)) >= 2:
                #Todo vertice con dos hijos o mas en un arbol DFS
                #es punto de articulacion
                puntosArticulacion.append(vertice)

        return puntosArticulacion
