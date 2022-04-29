from Proceso import *
from Screen import *


class Ejecucion:
    _inactivos = []
    _activos = []
    _finalizados = []
    _memoria = []
    _tiempo = 0
    _quantum = 0
    _cpuf = False
    sc = Screen()

    def __init__(self, procesos, maxQuantum=2):
        self._procesos = procesos
        self._maxQuantum = maxQuantum
        self.ejecucion()

    def ejecucion(self):
        self.filtrarProcesos(self._procesos)
        self.sc.tiempo(self._tiempo)
        self.sc.imprimirProcesos(self._activos, self._finalizados)
        if len(self._procesos) == len(self._finalizados):
            print("Finalizacion de todos los procesos")
        else:
            self.ejecucion()

    def filtrarProcesos(self, procesos):
        for p in procesos:
            estado = p.get_estado()
            if estado == "Inactivo":
                self._inactivos.append(p)
            elif estado == "Espera" or estado == "Ejecucion":
                self._activos.append(p)
            elif estado == "Salida":
                self._finalizados.append(p)
            else:
                print("Error")

    def sumarTiempo(self):
        time.sleep(3)
        self._tiempo += 1

    def cpu(self, proceso):
        proceso.set_ubicacion(Ubicacion.CPU)
        proceso.set_estado(Estado.Ejecucion)
        if proceso.get_duracion() <= 1:
            proceso.set_estado(Estado.Salida)
            proceso.set_ubicacion(Ubicacion.Salida)
            proceso.set_duracion(0)
            self._finalizados.append(proceso)
            self._cpuf = False
        else:
            self._cpuf = True
            proceso.set_duracion(proceso.get_duracion() - 1)
        self.sumarTiempo()