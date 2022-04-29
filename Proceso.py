from enum import Enum


class Proceso:
    def __init__(self, pid, llegada, duracion, prioridad):
        self._pid = pid
        self._llegada = llegada
        self._duracion = duracion
        self._prioridad = prioridad
        self._estado = Estado.Inactivo
        self._ubicacion = Ubicacion.Inactivo

    def get_pid(self):
        return self._pid

    def set_pid(self, pid):
        self._pid = pid

    def get_estado(self):
        return self._estado.value

    def set_estado(self, estado):
        self._estado = estado

    def get_ubicacion(self):
        return self._ubicacion.value

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def get_duracion(self):
        return self._duracion

    def set_duracion(self, duracion):
        self._duracion = duracion

    def get_llegada(self):
        return self._llegada

    def set_llegada(self, llegada):
        self._llegada = llegada

    def get_prioridad(self):
        return self._prioridad

    def set_prioridad(self, prioridad):
        self._prioridad = prioridad


class Estado (Enum):
    Inactivo = "Inactivo"
    Espera = "Espera"
    Ejecucion = "Ejecucion"
    Salida = "Salida"


class Ubicacion (Enum):
    Inactivo = "Inactivo"
    Espera = "Espera"
    CPU = "CPU"
    Memoria = "Memoria"
    Salida = "Salida"
