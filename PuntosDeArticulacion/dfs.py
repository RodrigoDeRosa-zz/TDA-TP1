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
        puntosDeArticulacion = []
        low = [0]*cantVert
        verticeAcutal = None

        k = 0
        for i in xrange(0, self.grafo.tam):

            vertice = stack.pop()
            
            if not visitados[int(vertice)]:
            
                k += 1
                result.aniadir_vertice(vertice, k)
                low[int(vertice)] = k
            
                if padres[int(vertice)] is not None:
                    result.unir_vertices(padres[int(vertice)], vertice, 0)

                visitados[int(vertice)] = True
                auxStack = []

                verticesVecinos = self.grafo.obtener_conocidos(vertice)
                for verticeVecino in verticesVecinos:
                
                    if not visitados[int(verticeVecino)]:
                
                        padres[int(verticeVecino)] = vertice
                        auxStack.append(verticeVecino)
                    
                    else:
                        if( padres[int(vertice)] != verticeVecino ):
                            low[int(vertice)] = min( low[int(vertice)], result.obtener_dato(verticeVecino) )
                    
                    if (verticeAcutal == vertice):

                        if( (low[int(verticeVecino)] >= result.obtener_dato(vertice) ) and (vertice not in puntosDeArticulacion)):    
                            puntosDeArticulacion.append(vertice)
                        low[int(vertice)] = min( low[int(vertice)], low[int(verticeVecino)] )
                
                while len(auxStack) > 0:
                    stack.append(auxStack.pop())  

                verticeAcutal = vertice          

        
        verticesVecinosDFS = result.obtener_conocidos(self.initVert)
        if ( (len(verticesVecinosDFS) >= 2)):
            #Todo vertice que es la raiz del DFS con dos hijos o mas
            #es punto de articulacion
            puntosDeArticulacion.append(self.initVert)

        return puntosDeArticulacion