from Proceso import *
from Ejecucion import *

# Proceso - PID, llegada, duracion, prioridad
P1 = Proceso("P1", 1, 3, 1)
P2 = Proceso("P2", 1, 4, 2)
P3 = Proceso("P3", 1, 2, 1)
P4 = Proceso("P4", 1, 3, 3)
P5 = Proceso("P5", 2, 4, 4)
P6 = Proceso("P6", 6, 2, 3)
P7 = Proceso("P7", 8, 1, 2)
P8 = Proceso("P8", 9, 3, 3)
P9 = Proceso("P9", 12, 2, 1)
P10 = Proceso("P10", 20, 4, 4)

procesos = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

Ejecucion(procesos)
