class NodoSemestre:
    def __init__(self,semestre):
        self.semestre = semestre
        self.siguiente = None

class NodoYear:
    def __init__(self, year, semestres, meses):
        self.year = year
        self.semestres = semestres
        self.meses = meses
        self.siguiente = None
