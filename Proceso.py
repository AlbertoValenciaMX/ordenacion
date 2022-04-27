class Proceso:
    def __init__(self, pid, estado, ubicacion, duracion):
        self._pid = pid
        self._estado = estado
        self._ubicacion = ubicacion
        self._duracion = duracion

    def get_pid(self):
        return self._pid

    def set_pid(self, pid):
        self._pid = pid

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def get_duracion(self):
        return self._duracion

    def set_duracion(self, duracion):
        self._duracion = duracion