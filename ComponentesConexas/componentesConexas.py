from graph import Graph
from lectorArchivos import LectorArchivos
from kosaraju import Kosaraju
import time

GRAFO1 = "files/d1.txt"
GRAFO2 = "files/d2.txt"
GRAFO3 = "files/d3.txt"
GRAFO4 = "files/d4.txt"
GRAFO5 = "files/d5.txt"
GRAFO6 = "files/d6.txt"

def main():

    lector = LectorArchivos()
    archivos = [GRAFO1, GRAFO2, GRAFO3, GRAFO4, GRAFO5, GRAFO6]
    aristas = ["20", "250", "2500", "25000", "250000", "2500000"]

    respuestas = ["yes", "no", "y", "n", "si", "s"]
    yes = ["yes", "y", "si", "s"]
    answer = raw_input("Imprimir componentes conexas? [y/n]: ")
    while (answer.lower() not in respuestas):
        print "No es tan dificil: 'Si', 'No', 'Yes', 'y', 'n', 's'...."
        answer = raw_input("Imprimir componentes conexas? [y/n]: ")
    if answer in yes:
        printVuln = True
    else: printVuln = False

    for archivo in archivos:
        print "-----------------------------------------"
        print "Leyendo archivo '" + archivo + "'..."
        grafo = lector.initGrafo(archivo, True)

        kosaraju = Kosaraju(grafo)

        print "Calculando componentes conexas del grafo con " + str(10**(archivos.index(archivo)+1)) + " vertices y " + aristas[archivos.index(archivo)] + " aristas..."
        init = time.time()
        componentesConexas = kosaraju.getComponentesConexas()
        end = time.time()
        print "Tiempo transcurrido: " + str(end-init) + "s."

        print str(len(componentesConexas)) + " Componentes Conexas encontradas."
        if printVuln:
            print "Conjunto de vertices de cada Componente Conexa:"
            print " ~",
            for x in componentesConexas:
                print x.keys()
        else: print "\n"

main()
