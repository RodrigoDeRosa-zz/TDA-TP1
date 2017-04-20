from graph import Graph

class DFS(object):
    """
    Depth First Search para un grafo.
    """
    def __init__(self):
        pass

    def getGrafoDFS_con_tiempos(self, grafo, initVert, visitados):
        """
        Devuelve un grafo dirigido resultado de hacer un DFS en el grafo recibido,
        a partir del vertice indicado.
            - Grafo : Objeto de clase Graph.
            - Vertice : Vertice del grafo recibido.
        """
        g = Graph(True)
        padres = []
        stack = []
        stack.append(initVert)
        contador=0

        cantVert = len(grafo.get_vertices().keys())
        padres = [None]*cantVert

        while (len(stack)>0):
            w=stack.pop()
            if(not visitados[int(w)]):
                contador +=1
                g.aniadir_vertice(w,contador)
                if(padres[int(w)] is not None):
                    g.unir_vertices(padres[int(w)],w,0)
                visitados[int(w)] = True
                stack_aux = []
                vertices_vecinos = grafo.obtener_conocidos(w)
                for x in vertices_vecinos:
                    if(not visitados[int(x)]):
                        stack_aux.append(x)
                        padres[int(x)] = w
                while(len(stack_aux)>0):
                    stack.append(stack_aux.pop())

        return g, contador
