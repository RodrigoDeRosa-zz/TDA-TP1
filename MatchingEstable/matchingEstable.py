from creadorArchivos import CreadorArchivos
from lectorArchivos import LectorArchivos
from galeShapley import galeShapley
from galeShapley import galeShapleyVacants
import time

TEST1 = 10
TESTFILE1 = "files/m1.txt"

TEST2 = 100
TESTFILE2 = "files/m2.txt"

TEST3 = 500
TESTFILE3 = "files/m3.txt"

TEST4 = 1000
TESTFILE4 = "files/m4.txt"

TEST5 = 3000
TESTFILE5 = "files/m5.txt"

def main():
    creador = CreadorArchivos()
    lector = LectorArchivos()
    E = []
    H = []
    Q = []

    archivos = [ TESTFILE1, TESTFILE2, TESTFILE3, TESTFILE4, TESTFILE5 ]
    cantidades = [ TEST1, TEST2, TEST3, TEST4, TEST5 ]

    respuestas = ["yes", "no", "y", "n", "si", "s"]
    yes = ["yes", "y", "si", "s"]
    answer = raw_input("Imprimir resultados? [y/n]: ")
    while (answer.lower() not in respuestas):
        print "No es tan dificil: 'Si', 'No', 'Yes', 'y', 'n', 's'...."
        answer = raw_input("Imprimir resultados? [y/n]: ")
    if answer in yes:
        printCouples = True
    else: printCouples = False

    for i in xrange(len(archivos)):
        print "Prueba " + str(i+1) + "."
        print "Creando archivo de prueba " + str(archivos[i]) + "..."
        creador.crearArchivo(cantidades[i], cantidades[i], archivos[i])

        print "Leyendo archivo de prueba " + str(archivos[i]) + "..."
        (E, H, Q) = lector.initListas(archivos[i])
        print "Ejecutando algoritmo con " + str(cantidades[i]) + " hospitales y estudiantes..."
        init = time.time()
        resultados = galeShapleyVacants(E, H, Q)
        end = time.time()
        print "Tiempo transcurrido: " + str(end - init) + "s."

        if printCouples:
            for pareja in resultados:
                print "Hospital " + str(pareja[0]) + " matcheo con estudiantes:"
                print "\t\t" + str(pareja[1])
            print "\n"
        else: print "\n"

main()
