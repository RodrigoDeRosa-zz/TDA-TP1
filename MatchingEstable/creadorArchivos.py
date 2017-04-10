
TEST_FILE = "testFile.txt"

class CreadorArchivos(object):
    """
    Crea un archivo para las pruebas del problema de asignacion de residencias.
    Los archivos son del tipo:
        #1 - |E|
        #2-#(2+|E|) - mi ... mj ... m(|H|-1) [Desde m0]
        #(2+|E|) - |H|
        #(3+|E|)-#(3+|E|+|H|) - ni ... nj ... n(|E|-1) [Desde n0]
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
