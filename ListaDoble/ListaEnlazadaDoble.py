from Nodo import NodoTD

class ListaEnlazadaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertarTareaDiaria(self,carnet, nombre, descripcion, fecha, hora, estado):
        if self.vacia():
            self.primero = self.ultimo = NodoTD(carnet, nombre, descripcion, fecha, hora, estado)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoTD(carnet, nombre, descripcion, fecha, hora, estado)
            self.ultimo.anterior = aux

    def mostrar(self):
        aux = self.primero
        while aux:
            print(aux.carnet)
            aux = aux.siguiente
