class Screen:

    def __init__(self):
        self.nombre = "Screen"

    def procesoHead(self):
        print("Procesos")
        print("PID - ESTADO - UBICACION - DURACION")

    def procesoBody(self, proceso):
        print("{} - {} - {} - {}".format(proceso.get_pid(), proceso.get_estado(), proceso.get_ubicacion(), proceso.get_duracion()))