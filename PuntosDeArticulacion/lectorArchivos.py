from graph import Graph

class LectorArchivos(object):
    """
    Se encarga de abrir y leer los archivos de prueba, crea un grafo a partir de los datos leidos.
    """

    def __init__(self):
        pass

    def initGrafo(self, filePath, digraph = False):
        """
        Crea el grafo para la prueba a partir del archivo que esta en el path indicado.
            - filePath {string} Direccion del archivo.
        El archivo debe ser del tipo: (#k, numero de linea k)
            #1 - |V|
            #2 - |E|
            #3...#n - Vi Vj <--- Vertices que estan unidos, indicados por numeros separados
                                por un espacio
        """
        grafo = Graph(digraph)

        try:
            archivo = open(filePath, "r")
        except IOError:
            raise ValueError, "Error al abrir archivo!"

        lineas = archivo.readlines() #Lista con todas las lineas del archivo
        archivo.close()

        #Las primeras dos lineas son |V| y |E| y no se usan asi que se omiten
        lineas = lineas[2:]
        for linea in lineas:
            vertices = linea.split(' ') #Se obtienen los vertices
            vertices[1] = vertices[1][:len(vertices[1])-1] #Se saca el \n del segundo vertice
            for i in xrange(0, 2):
                grafo.aniadir_vertice(vertices[i], None) #Se guardan los dos vertices
            grafo.unir_vertices(vertices[0], vertices[1], 0)

        return grafo
