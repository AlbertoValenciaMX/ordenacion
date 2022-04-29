from Proceso import *
from Screen import *


class Ejecucion:
    espera = []
    activos = []
    finalizados = []

    def __init__(self, procesos):
        self._procesos = procesos
        self.inicio()

    def inicio(self):
        self.filtrarProcesos(self._procesos)

    def filtrarProcesos(self, procesos):
        for p in procesos:
            estado = p.get_estado()
            if estado == "Inactivo":
                self.espera.append(p)
            elif estado == "Espera" or estado == "Ejecucion":
                self.activos.append(p)
            elif estado == "Salida":
                self.finalizados.append(p)
            else:
                print("Error")
