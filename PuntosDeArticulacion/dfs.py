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

        return result

    def getPuntosDeArticulacion(self):
    
        cantVert = len(self.grafo.get_vertices().keys())
        visitados = [False]*cantVert
        padres = [None]*cantVert
        puntosDeArticulacion = []
        low = [0]*cantVert
        num = [0]*cantVert
        count = 0

        self.getPuntosDeArticulacionRec(self.initVert, visitados, padres, low, num, puntosDeArticulacion, count)

        return puntosDeArticulacion

    def getPuntosDeArticulacionRec(self, vertice, visitados, padres, low, num, puntosDeArticulacion, count):
        """
        Devuelve un grafo dirigido resultado de hacer un DFS en el grafo recibido,
        a partir del vertice indicado.
            - Grafo : Objeto de clase Graph.
            - Vertice : Vertice del grafo recibido.
        """

        visitados[int(vertice)] = True
        count += 1
        low[int(vertice)] = count
        num[int(vertice)] = count

        for verticeVecino in self.grafo.obtener_conocidos(vertice):

            if not visitados[int(verticeVecino)]:

                padres[int(verticeVecino)] = vertice
                self.getPuntosDeArticulacionRec(verticeVecino, visitados, padres, low, num, puntosDeArticulacion, count)

                if(padres[int(vertice)] != None) and (low[int(verticeVecino)] >= num[int(vertice)] ) and (vertice not in puntosDeArticulacion):    
                    puntosDeArticulacion.append(vertice)
                low[int(vertice)] = min( low[int(vertice)], low[int(verticeVecino)] )
                
            elif (padres[int(vertice)] != verticeVecino):
                low[int(vertice)] = min( low[int(vertice)], num[int(verticeVecino)] )


    # def getPuntosDeArticulacion(self):
    #     """
    #     Devuelve un grafo dirigido resultado de hacer un DFS en el grafo recibido,
    #     a partir del vertice indicado.
    #         - Grafo : Objeto de clase Graph.
    #         - Vertice : Vertice del grafo recibido.
    #     """
    
    #     result = Graph(True)
    #     cantVert = len(self.grafo.get_vertices().keys())
    #     visitados = [False]*cantVert
    #     padres = [None]*cantVert
    #     stack = [self.initVert]
    #     puntosDeArticulacion = []
    #     low = [0]*cantVert
    #     verticeActual = self.initVert

    #     k = 0
    #     while(len(stack) > 0):

    #         vertice = stack.pop()
            
    #         if not visitados[int(vertice)]:
            
    #             k += 1
    #             result.aniadir_vertice(vertice, k)
    #             low[int(vertice)] = k
            
    #             if padres[int(vertice)] is not None:
    #                 result.unir_vertices(padres[int(vertice)], vertice, 0)

    #             visitados[int(vertice)] = True
    #             auxStack = []

    #             verticesVecinos = self.grafo.obtener_conocidos(vertice)
    #             for verticeVecino in verticesVecinos:
                
    #                 if not visitados[int(verticeVecino)]:
                
    #                     padres[int(verticeVecino)] = vertice
    #                     auxStack.append(verticeVecino)
                    
    #                 else:
    #                     if( padres[int(vertice)] != verticeVecino ):
    #                         low[int(vertice)] = min( low[int(vertice)], result.obtener_dato(verticeVecino) )
    #                         auxStack.append(verticeActual)

    #                 # if (verticeActual == padres[int(verticeVecino)]):
    #                 #     if( (low[int(verticeVecino)] >= result.obtener_dato(vertice) ) and (vertice not in puntosDeArticulacion)):    
    #                 #         puntosDeArticulacion.append(vertice)
    #                 #     low[int(vertice)] = min( low[int(vertice)], low[int(verticeVecino)] )
                
    #             while len(auxStack) > 0:
    #                 stack.append(auxStack.pop())           

        
    #     verticesVecinosDFS = result.obtener_conocidos(self.initVert)
    #     if ( (len(verticesVecinosDFS) >= 2)):
    #         #Todo vertice que es la raiz del DFS con dos hijos o mas
    #         #es punto de articulacion
    #         puntosDeArticulacion.append(self.initVert)

    #     return puntosDeArticulacion