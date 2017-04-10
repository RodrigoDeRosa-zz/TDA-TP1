from MatchingEstable.creadorArchivos import CreadorArchivos
from MatchingEstable.lectorArchivos import LectorArchivos

def main():
    creador = CreadorArchivos()
    creador.crearArchivo(100, 100, "MatchingEstable/files/m1.txt")
    #creador.crearArchivo(1000, 1000, "MatchingEstable/files/m2.txt")
    #creador.crearArchivo(10000, 10000, "MatchingEstable/files/m3.txt")
    #creador.crearArchivo(100000, 100000, "MatchingEstable/files/m4.txt")

    lector = LectorArchivos()
    E = [] #Lista de listas de estudiantes
    H = [] #Lista de listas de hospitales
    Q = [] #Lista de listas de vacantes
    (E, H, Q) = lector.initListas("MatchingEstable/files/m1.txt")

main()
