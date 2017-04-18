from MatchingEstable.creadorArchivos import CreadorArchivos
from MatchingEstable.lectorArchivos import LectorArchivos
from MatchingEstable.galeShapley import galeShapley
from MatchingEstable.galeShapley import galeShapleyVacants
import time

TEST1 = 10
TEST2 = 100
TEST3 = 500

def main():
    creador = CreadorArchivos()
    print "Creating test files..."
    print "\tTest file 1..."
    creador.crearArchivo(TEST1, TEST1, "MatchingEstable/files/m1.txt")
    print "\t\t\tDONE"
    print "\tTest file 2..."
    creador.crearArchivo(TEST2, TEST2, "MatchingEstable/files/m2.txt")
    print "\t\t\tDONE"
    print "\tTest file 3..."
    creador.crearArchivo(TEST3, TEST3, "MatchingEstable/files/m3.txt")
    print "\t\t\tDONE\n"
    #creador.crearArchivo(100000, 100000, "MatchingEstable/files/m4.txt")

    lector = LectorArchivos()
    E = [] #Lista de listas de estudiantes
    H = [] #Lista de listas de hospitales
    Q = [] #Lista de listas de vacantes

    print "Reading test file 1..."
    (E, H, Q) = lector.initListas("MatchingEstable/files/m1.txt")
    print "\t\t\tDONE"
    print "Test 1: m = n = " + str(TEST1)
    init = time.time()
    galeShapleyVacants(E, H, Q)
    test1Time = time.time() - init
    print "Time elapsed: " + str(test1Time) + " seconds.\n"

    print "Reading test file 2..."
    (E, H, Q) = lector.initListas("MatchingEstable/files/m2.txt")
    print "\t\t\tDONE"
    print "Test 2: m = n = " + str(TEST2)
    init = time.time()
    galeShapleyVacants(E, H, Q)
    test2Time = time.time() - init
    print "Time elapsed: " + str(test2Time) + " seconds.\n"

    print "Reading test file 3..."
    (E, H, Q) = lector.initListas("MatchingEstable/files/m3.txt")
    print "\t\t\tDONE"
    print "Test 3: m = n = " + str(TEST3)
    init = time.time()
    galeShapleyVacants(E, H, Q)
    test3Time = time.time() - init
    print "Time elapsed: " + str(test3Time) + " seconds.\n"

    print "Time relation: "
    print "\tTest 2 took " + str(test2Time / test1Time) + " times more than Test 1 with " + str(TEST2 - TEST1) + " more elements."
    print "\tTest 3 took " + str(test3Time / test2Time) + " times more than Test 2 with " + str(TEST3 - TEST2) + " more elements."

main()
