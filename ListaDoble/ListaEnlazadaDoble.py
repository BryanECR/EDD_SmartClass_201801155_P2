from NodoDoble import NodoTD, NodoMes

class ListaTareasDiaria():
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

    def mostrarTareasDiarias(self):
        aux = self.primero
        while aux:
            print(aux.carnet)
            aux = aux.siguiente
    


class ListaMeses():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertarMes(self,mes):
        if self.vacia():
            self.primero = self.ultimo = NodoMes(mes)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoMes(mes)
            self.ultimo.anterior = aux
    
    def mostrarMeses(self):
        aux = self.primero
        while aux:
            print(aux.mes)
            aux = aux.siguiente

