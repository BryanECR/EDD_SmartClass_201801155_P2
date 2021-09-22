class NodoMes:
    def __init__(self,mes,matrix = None):
        self.mes = mes
        self.matrix = matrix
        self.siguiente = None
        self.anterior = None

class NodoTD:
    def __init__(self,carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.siguiente = None
        self.anterior = None