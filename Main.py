from Proceso import *
from Screen import *

sc = Screen()
P1 = Proceso("P1", "Ejecucion", "CPU", 10, 0, 1)
P2 = Proceso("P2", "Espera", "Memoria", 5, 0, 2)

sc.procesoHead()
sc.procesoBody(P1)
sc.procesoBody(P2)