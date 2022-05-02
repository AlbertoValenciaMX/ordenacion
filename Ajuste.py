class Ajuste:

    m1 = []
    m2 = []
    m3 = []
    m4 = []

    def __init__(self):
        self.nombre = "Ajuste"

    # programa que ajuste los procesos con FIFO
    def FIFO(self, proceso, memoria):
        self.filtroNivel(memoria)
        self.m1.append(proceso)
        return self.agruparMemoria()

    def LJF(self, proceso, memoria):
        self.filtroNivel(memoria)
        sorted(self.m2, key=lambda proceso: proceso.get_duracion())
        self.m2.insert(0, proceso)
        return self.agruparMemoria()

    def SJF(self, proceso, memoria):
        self.filtroNivel(memoria)
        sorted(self.m3, key=lambda proceso: proceso.get_duracion())
        self.m3.append(proceso)
        return self.agruparMemoria()

    def LIFO(self, proceso, memoria):
        self.filtroNivel(memoria)
        self.m4.insert(0, proceso)
        return self.agruparMemoria()

    def filtroNivel(self, memoria):
        self.m1 = []
        self.m2 = []
        self.m3 = []
        self.m4 = []
        for proceso in memoria:
            if proceso.get_prioridad() == 1:
                self.m1.append(proceso)
            elif proceso.get_prioridad() == 2:
                self.m2.append(proceso)
            elif proceso.get_prioridad() == 3:
                self.m3.append(proceso)
            elif proceso.get_prioridad() == 4:
                self.m4.append(proceso)

    def agruparMemoria(self):
        memoria = []
        memoria.extend(self.m1)
        memoria.extend(self.m2)
        memoria.extend(self.m3)
        memoria.extend(self.m4)
        return memoria
