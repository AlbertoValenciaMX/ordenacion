def procesoHead():
    print("Procesos")
    print("PID - ESTADO - UBICACION - DURACION")

def procesoBody(proceso):
    print("{} - {} - {} - {}".format(proceso.get_pid(), proceso.get_estado(), proceso.get_ubicacion(), proceso.get_duracion()))