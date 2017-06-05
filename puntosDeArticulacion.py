from lectorArchivos import LectorArchivos
from graph import Graph
from tarjan import Tarjan
import time

GRAFO1 = "files/g1.txt"
GRAFO2 = "files/g2.txt"
GRAFO3 = "files/g3.txt"
GRAFO4 = "files/g4.txt"
GRAFO5 = "files/g5.txt"
GRAFO6 = "files/g6.txt"

def main():
    lector = LectorArchivos()
    archivos = [GRAFO1, GRAFO2, GRAFO3, GRAFO4]#, GRAFO5, GRAFO6]

    respuestas = ["yes", "no", "y", "n", "si", "s"]
    yes = ["yes", "y", "si", "s"]
    answer = raw_input("Imprimir vertices vulnerables? [y/n]: ")
    while (answer.lower() not in respuestas):
        print "No es tan dificil: 'Si', 'No', 'Yes', 'y', 'n', 's'...."
        answer = raw_input("Imprimir vertices vulnerables? [y/n]: ")
    if answer in yes:
        printVuln = True
    else: printVuln = False

    for archivo in archivos:
        print "-----------------------------------------"
        print "Leyendo archivo '" + archivo + "'..."
        grafo = lector.initGrafo(archivo)

        tarjan = Tarjan(grafo)

        print "Calculando puntos de articulacion en grafo con " + str(10**(archivos.index(archivo)+1)) + " vertices y aristas..."
        init = time.time()
        puntosArticulacion = tarjan.getPuntosDeArticulacion()
        end = time.time()
        print "Tiempo transcurrido: " + str(end-init) + "s."

        print str(len(puntosArticulacion)) + " Puntos de articulacion encontrados."
        percentage = (float(len(puntosArticulacion)) / float(10**(archivos.index(archivo)+1)))*100
        print "%s%% de los vertices son vulnerables." % percentage
        if printVuln:
            print "Vertices vulnerables:"
            print " ~",
            for i in xrange(0, len(puntosArticulacion)-1):
                print puntosArticulacion[i] + ", ",
            print puntosArticulacion[len(puntosArticulacion)-1] + "\n"
        else: print "\n"
        
main()
