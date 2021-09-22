class NodoMatriz:
    def __init__(self, x, y, dato):
        self.x=x
        self.y=y
        self.dato=dato
        self.arriba=None
        self.abajo=None
        self.izquierda= None
        self.derecha = None

class NodoCabecera:
    def __init__(self,tipo, indice):
        self.tipo=tipo
        self.indice=indice
        self.siguiente=None
        self.derecha=None
        self.abajo=None
        
class NodoRaiz:
    def __init__(self):
        self.NodoFilas=None
        self.NodoColumnas=None