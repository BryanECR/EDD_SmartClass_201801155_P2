class NodoSemestre:
    def __init__(self,semestre,arbol=None):
        self.semestre = semestre
        self.arbol = arbol
        self.siguiente = None

class NodoYear:
    def __init__(self, year, semestres=None, meses=None):
        self.year = year
        self.semestres = semestres
        self.meses = meses
        self.siguiente = None
