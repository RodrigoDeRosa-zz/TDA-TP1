class LectorArchivos(object):
    """
    Lee un archivo para las pruebas del problema de asignacion de residencias.
    Los archivos son del tipo:
        #1 - |E|
        #2-#(2+|E|) - mi ... mj ... m(|H|-1) [Desde m0]
        #(2+|E|) - |H|
        #(3+|E|)-#(3+|E+|H|) - ni ... nj ... n(|E|-1) [Desde n0]
        #(4+|E|+|H|) - x0 ... xi ... x(|H|)
        Con:
            |E| : cantidad de estudiantes.
            |H| : cantidad de hospitales.
            mi : hospital i.
            ni : estudiante i.
            xi : cantidad de vacantes del hospital i
    """
    def __init__(self):
        pass

    def borrarBarraN(self, lista):
        ultimo = len(lista) - 1
        lista[ultimo] = lista[ultimo][:len(lista[ultimo])-1] #Se saca el \n del ultimo valor

    def guardarListas(self, destino, lineas):
        """
        Crea una lista a partir de las lineas recibidas en la lista origen.
            - destino {list} Lugar donde van todas las listas
            - lineas {list} Lista con todas las lineas como elementos individuales
        """
        for linea in lineas:
            total = linea.split(' ') #Se obtiene la lista de valores

            self.borrarBarraN(total)

            lista = []
            for i in xrange(0, len(total)):
                lista.append(int(total[i])) #Se guardan los valores
            destino.append(lista)

    def initListas(self, filePath):
        """
        Crea las listas a partir del archivo en la direccion recibida.
        """
        try:
            archivo = open(filePath, "r")
        except IOError:
            raise ValueError, "Error al abrir archivo!"

        E = []
        H = []
        Q = []

        lineas = archivo.readlines() #Lista con todas las lineas del archivo
        archivo.close()

        #Las primer linea es |E| y no se usa asi que se omite
        cantidadLineas = len(lineas)
        e = int(lineas[0])
        q = int(lineas[(cantidadLineas-1)/2])

        estudiantes = lineas[1 : q + 1] #Se resta |H| y Q y se divide por 2 (porque |E| == |H|)
        self.guardarListas(E, estudiantes)
        hospitales = lineas[ q + 2 : cantidadLineas - 1] #Ahora se toman solo los hospitales
        self.guardarListas(H, hospitales)

        vacantes = lineas[cantidadLineas-1 : cantidadLineas]
        self.guardarListas(Q, vacantes)

        return (E, H, Q[0])
