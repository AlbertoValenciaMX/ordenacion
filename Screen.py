import time


class Screen:

    def __init__(self):
        self.nombre = "Screen"

    def imprimirProcesosActivos(self, activos, espera, finalizados):
        print("Procesos en espera: {}".format(len(espera)))
        for p in activos:
            self.procesoBody(p)
        self.procesoHead()
        for p in activos:
            self.procesoBody(p)
        self.procesosFoot(finalizados)

    def imprimirProcesos(self, activos, finalizados):
        self.procesoHead()
        for p in activos:
            self.procesoBody(p)
        self.procesosFoot(finalizados)

    def procesoHead(self):
        print("Procesos")
        print("PID - ESTADO - UBICACION - DURACION")

    def procesoBody(self, proceso):
        print("{} - {} - {} - {}".format(proceso.get_pid(),
              proceso.get_estado(), proceso.get_ubicacion(), proceso.get_duracion()))

    def procesosFoot(self, procesos):
        print("Salida")
        for index, p in enumerate(procesos):
            print("PID #{} - {}".format(index+1, p.get_pid()))

    def tiempo(self, tiempo):
        print("Tiempo: {}".format(tiempo))

    def quantum(self, quantum):
        print("Quantum: {}".format(quantum))
