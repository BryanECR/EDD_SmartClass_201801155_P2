class NodoTD:
    def __init__(self,carnet, nombre, descripcion, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.siguiente = None
        self.anterior = None

