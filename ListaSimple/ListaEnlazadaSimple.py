from NodoSimple import NodoSemestre, NodoYear

class ListaSemestre():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacia(self):
        return self.inicio == None

    def incertarSemestre(self,semestre):
        if self.vacia():
            self.inicio = self.fin = NodoSemestre(semestre)
        else:
            aux = self.fin
            self.fin = aux.siguiente = NodoSemestre(semestre)
            self.fin.siguiente = self.inicio

    def mostrarSemestres(self):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.inicio:
                print(aux.semestre)

                aux = aux.siguiente

            print(aux.semestre)
            

class ListaYear():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacia(self):
        return self.inicio == None

    def incertarYear(self,year,semestres,meses):
        if self.vacia():
            self.inicio = self.fin = NodoYear(year,semestres,meses)
        else:
            aux = self.fin
            self.fin = aux.siguiente = NodoYear(year,semestres,meses)
            self.fin.siguiente = self.inicio

    def mostrarYears(self):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.inicio:
                print(aux.year)
                aux = aux.siguiente
            
            print(aux.year)
            