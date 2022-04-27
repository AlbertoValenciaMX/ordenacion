from Proceso import *
from Screen import *

sc = Screen()

P1 = Proceso("P1", 0, 10, 1)
P2 = Proceso("P2", 0, 10, 1)
P3 = Proceso("P3", 0, 10, 1)
P1.set_estado(Estado.Espera)
P2.set_estado(Estado.Inactivo)
P3.set_estado(Estado.Salida)

procesos = [P1, P2, P3]

espera = []
activos = []
finalizados = []


for p in procesos:
    estado = p.get_estado()
    if estado == "Inactivo":
        espera.append(p)
    elif estado == "Espera" or estado == "Ejecucion":
        activos.append(p)
    elif estado == "Salida":
        finalizados.append(p)
    else:
        print("Error")

sc.procesoHead()

for p in activos:
    sc.procesoBody(p)

for p in finalizados:
    sc.procesoFoot(p)

