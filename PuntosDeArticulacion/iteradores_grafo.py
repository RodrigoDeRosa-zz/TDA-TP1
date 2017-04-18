import graph

class Bfs_iter(object):
    """
    Iterador de busqueda en anchura para grafos.
    """

    def __init__(self, grafo, raiz):
        """
        grafo: un objeto del tipo grafo.
        raiz: una string que es una clave del grafo.

        Si la raiz no pertenece al grafo, levanta excepcion.
        """

        if type(grafo) != graph.Graph:
            raise TypeError

        if not grafo.pertenece(raiz):
            raise IndexError

        self.grafo = grafo
        self.cola_visita = [raiz]

        self.distancia = {}
        self.visitado = {}
        self.padre = {}

        for vertice in grafo:
            self.distancia[vertice] = None
            self.visitado[vertice] = False
            self.padre[vertice] = None

        self.distancia[raiz] = 0
        self.visitado[raiz] = True

    def al_final(self):
        """
        Devuelve True si el iterador llego al final, False de lo contrario.
        """

        return len(self.cola_visita) == 0

    def ver_actual(self):
        """
        Devuelve un string que representa al vertice/nodo actual.
        Si el iterador esta al final, levanta excepcion.
        """

        return self.cola_visita[0]

    def siguiente(self):
        """
        Avanza hasta el proximo nodo.

        Si el iterador ya esta al final, levanta excepcion.
        """

        if self.al_final():
            raise IndexError

        padre = self.cola_visita.pop(0)

        for vertice in self.grafo.obtener_conocidos(padre):
            if self.visitado[vertice]:
                continue

            self.cola_visita.append(vertice)
            self.distancia[vertice] = self.distancia[padre] + 1
            self.visitado[vertice] = True
            self.padre[vertice] = padre

    def avanzar_hasta_el_final(self):
        """
        Avanza el iterador hasta el final.
        """

        while not self.al_final():
            self.siguiente()

    def obtener_distancia(self, clave):
        """
        clave: una string que es una clave del grafo.

        Si la clave fue visitada, devuelve la distancia desde el vertice/raiz
        hasta el vertice/nodo solicitado.

        Si la clave no pertenece al grafo, levanta excepcion.
        """

        if not self.grafo.pertenece(clave):
            raise IndexError

        return self.distancia[clave]

    def obtener_distancia(self, clave):
        """
        clave: una string que es una clave del grafo.

        Si la clave fue visitada, devuelve el padre del vertice/nodo solicitado
        segun el recorrido bfs seguido.

        Si la clave no pertenece al grafo, levanta excepcion.
        """

        if not self.grafo.pertenece(clave):
            raise IndexError

        return self.padre[clave]


