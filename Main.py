from Proceso import *
from Ejecucion import *


P1 = Proceso("P1", 0, 10, 1)
P2 = Proceso("P2", 0, 10, 1)
P3 = Proceso("P3", 0, 10, 1)
P1.set_estado(Estado.Espera)
P2.set_estado(Estado.Salida)
P3.set_estado(Estado.Salida)

procesos = [P1, P2, P3]


Ejecucion(procesos)
