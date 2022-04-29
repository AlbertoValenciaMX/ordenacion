from Ajuste import *
from Proceso import *
from Screen import *


class Ejecucion:
    _inactivos = []
    _activos = []
    _finalizados = []
    _espera = []
    _memoria = []
    _tiempo = 0
    _quantum = 0
    _cpuf = False
    sc = Screen()

    def __init__(self, procesos, maxQuantum=2):
        self._procesos = procesos
        self._maxQuantum = maxQuantum
        self.inicio()

    def inicio(self):
        self.sumarTiempo()
        self.ingresoProcesos()
        if self._cpuf:
            self.salidaProcesos()
        else:
            self._procesos = self.ajusteProcesos(self._procesos)
            proceso = self.ultimoProceso()
            self.cpu(proceso)

    def sumarTiempo(self):
        time.sleep(1)
        self._tiempo += 1

    def ingresoProcesos(self):
        for p in self._procesos:
            if p.get_llegada() == self._tiempo:
                self._espera.append(p)
                p.set_estado(Estado.Espera)
                p.set_ubicacion(Ubicacion.Espera)

    def ajusteProcesos(self, procesos):
        return procesos

    def ultimoProceso(self):
        if self._memoria == []:
            if self._activos == []:
                self.inicio()
            else:
                self._memoria.append(self._espera.pop(0))
        return self._memoria.pop(0)

    def salidaProcesos(self):
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

    def cpu(self, proceso):
        proceso.set_ubicacion(Ubicacion.CPU)
        proceso.set_estado(Estado.Ejecucion)
        if proceso.get_duracion() > 1:
            self._cpuf = True
            proceso.set_duracion(proceso.get_duracion() - 1)
        else:
            proceso.set_estado(Estado.Salida)
            proceso.set_ubicacion(Ubicacion.Salida)
            proceso.set_duracion(0)
            self._finalizados.append(proceso)
            self._cpuf = False
            self.sc.imprimirProcesos(self._activos, self._finalizados)

