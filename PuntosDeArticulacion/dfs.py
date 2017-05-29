from graph import Graph

class DFS(object):
    """
    Depth First Search para un grafo.
    """
    def __init__(self, vertice, grafo):
        self.initVert = vertice
        self.grafo = grafo

    def getGrafoDFS(self):
        """
        Devuelve un grafo dirigido resultado de hacer un DFS en el grafo recibido,
        a partir del vertice indicado.
            - Grafo : Objeto de clase Graph.
            - Vertice : Vertice del grafo recibido.
        """
        result = Graph(True)
        cantVert = len(self.grafo.get_vertices().keys())
        visitados = [False]*cantVert
        padres = [None]*cantVert
        stack = [self.initVert]

        k = 0
        for i in xrange(0, self.grafo.tam):
            vertice = stack.pop()
            if not visitados[int(vertice)]:
                k += 1
                result.aniadir_vertice(vertice, k)
                if padres[int(vertice)] is not None:
                    result.unir_vertices(padres[int(vertice)], vertice, 0)

                visitados[int(vertice)] = True

                auxStack = []
                verticesVecinos = self.grafo.obtener_conocidos(vertice)
                for verticeVecino in verticesVecinos:
                    if not visitados[int(verticeVecino)]:
                        auxStack.append(verticeVecino)
                        padres[int(verticeVecino)] = vertice
                while len(auxStack) > 0:
                    stack.append(auxStack.pop())

        return result, padres

    def getLowList(self, padres, grafoTemp):
        
        cantVert = len(self.grafo.get_vertices().keys())
        visitados = [False]*cantVert
        stack = [self.initVert]
        low = [0]*cantVert

        for i in xrange(0, self.grafo.tam):
            vertice = stack.pop()
            if not visitados[int(vertice)]:

                visitados[int(vertice)] = True

                auxStack = []
                verticesVecinos = self.grafo.obtener_conocidos(vertice)

                #se define el minimo low como el de si mismo
                low [int(vertice)] = grafoTemp.obtener_dato(vertice)

                for verticeVecino in verticesVecinos:
                    
                    if not visitados[int(verticeVecino)]:
            
                        distanciaVecino = grafoTemp.obtener_dato(verticeVecino)
                        low[int(vertice)] = min(low[int(vertice)], low[int(verticeVecino)])
                        
                        auxStack.append(verticeVecino)
                    
                    elif (verticeVecino != padres[int(vertice)]):
                            distanciaVecino = grafoTemp.obtener_dato(verticeVecino)
                            low[int(vertice)] = min(low[int(vertice)], distanciaVecino)        

                while len(auxStack) > 0:
                    stack.append(auxStack.pop())

        return low

    def getPuntosDeArticulacion (self, padres, grafoTemp, low):
            
        cantVert = len(self.grafo.get_vertices().keys())
        visitados = [False]*cantVert
        stack = [self.initVert]
        puntosDeArticulacion = []

        for i in xrange(0, self.grafo.tam):
            vertice = stack.pop()
            if not visitados[int(vertice)]:

                visitados[int(vertice)] = True

                auxStack = []
                verticesVecinos = self.grafo.obtener_conocidos(vertice)

                for verticeVecino in verticesVecinos:
                    if not visitados[int(verticeVecino)]:

                        auxStack.append(verticeVecino)

                        if ( (len(verticesVecinos) >= 2) and (padres[int(vertice)] == None) and (vertice not in puntosDeArticulacion)):
                            #Todo vertice que es raiz con dos hijos o mas
                            #es punto de articulacion
                            puntosDeArticulacion.append(vertice)

                        if( (padres[int(vertice)] != None) and (low[int(verticeVecino)] >= grafoTemp.obtener_dato(vertice)) and (vertice not in puntosDeArticulacion)):    
                            puntosDeArticulacion.append(vertice)

                while len(auxStack) > 0:
                    stack.append(auxStack.pop())

        return puntosDeArticulacion