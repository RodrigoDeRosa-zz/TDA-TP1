import random

TEST_FILE = "files/testFile.txt"
MAX_VACANTES = 10

class CreadorArchivos(object):
    """
    Crea un archivo para las pruebas del problema de asignacion de residencias.
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

    def crearArchivo(self, E, H, filePath = TEST_FILE):
        """
        Crea el archivo de prueba.
        Parametros:
            - E {int} Cantidad de estudiantes
            - H {int} Cantidad de hospitales
        """

        try:
            archivo = open(filePath, "w");
        except IOError:
            raise ValueError, "Error al abrir el archivo!"

        archivo.write(str(E) + "\n") #Se agrega la cantidad de estudiantes
        self.agregarPreferencias(archivo, E, H) #Se agregan las preferencias de los estudiantes
        archivo.write(str(H) + "\n") #Se agrega la cantidad de hospitales
        self.agregarPreferencias(archivo, H, E) #Se agregan las preferencias de los hospitales
        self.agregarVacantes(archivo, H) #Se agrega la cantidad de vacantes de cada hospital

        archivo.close()


    def generarListaAleatoria(self, n):
        """
        Genera una lista aleatoria de eneteros desde el 0 hasta n, sin repetir,
        y la devuelve.
            - n {int} Cota superior
        """
        lista = []
        for i in xrange(0, n):
            lista.append(str(i))
        random.shuffle(lista)
        return lista

    def agregarPreferencias(self, archivo, n, m):
        """
        Agrega las n lineas al archivo recibido con preferencias aleatorias sobre
        m elementos.
            - archivo {file} Archivo a escribir
            - n {int} Cantidad de lineas
            - m {int} Cantidad de elementos sobre los cuales decidir preferencia
        """
        for i in xrange(0, n):
            preferencias = self.generarListaAleatoria(m)
            linea = " ".join(preferencias)
            archivo.write(linea + "\n")

    def agregarVacantes(self, archivo, H):
        """
        Agrega una linea al archivo recibido con la cantidad de vacantes de los
        H hospitales, separadas por espacios.
            - archivo {file} Archivo a escribir
            - H {int} Cantidad de hospitales
        """
        vacantes = []
        for i in xrange(0, H):
            vacantes.append(str(random.randint(1, MAX_VACANTES)))
        linea = " ".join(vacantes)
        archivo.write(linea + "\n")
