from graph import Graph

class DFS(object):
    """
    Depth First Search para un grafo.
    """
    def __init__(self):
        pass

    def getGrafoDFS(self, grafo, initVert):
        """
        Devuelve un grafo dirigido resultado de hacer un DFS en el grafo recibido,
        a partir del vertice indicado.
            - Grafo : Objeto de clase Graph.
            - Vertice : Vertice del grafo recibido.
        """
        result = Graph(True)
        cantVert = len(grafo.get_vertices().keys())
        visitados = [False]*cantVert
        padres = [None]*cantVert
        stack = [initVert]

        k = 0
        for i in xrange(0, grafo.tam):
            vertice = stack.pop()
            if not visitados[int(vertice)]:
                k += 1
                result.aniadir_vertice(vertice, k)
                if padres[int(vertice)] is not None:
                    result.unir_vertices(padres[int(vertice)], vertice, 0)

                visitados[int(vertice)] = True

                auxStack = []
                verticesVecinos = grafo.obtener_conocidos(vertice)
                for verticeVecino in verticesVecinos:
                    if not visitados[int(verticeVecino)]:
                        auxStack.append(verticeVecino)
                        padres[int(verticeVecino)] = vertice
                while len(auxStack) > 0:
                    stack.append(auxStack.pop())

        return result
