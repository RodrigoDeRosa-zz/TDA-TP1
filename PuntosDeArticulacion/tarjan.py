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

        grafoDFS = dfs.getGrafoDFS()

        #se obtienen los puntos de articulacion del DFS sin tener en cuenta la raiz
        puntosArticulacion = dfs.getPuntosDeArticulacion()

        verticesVecinosDFS = grafoDFS.obtener_conocidos(vertice)
        if ( (len(verticesVecinosDFS) >= 2)):
            #Todo vertice que es la raiz del DFS con dos hijos o mas
            #es punto de articulacion
            puntosDeArticulacion.append(vertice)

        return puntosArticulacion
