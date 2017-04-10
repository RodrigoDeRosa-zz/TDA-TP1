from PuntosDeArticulacion.lectorArchivos import LectorArchivos
from graph import Graph

TEST_FILE = "PuntosDeArticulacion/files/g1.txt"

def main():
    lector = LectorArchivos()

    grafo = lector.initGrafo(TEST_FILE)

    print len(grafo)

main()
