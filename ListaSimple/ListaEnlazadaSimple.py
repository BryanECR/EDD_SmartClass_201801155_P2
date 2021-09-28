from ListaSimple.NodoSimple import NodoSemestre, NodoYear

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

    def mostrarSemestres(self):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                print(aux.semestre)

                aux = aux.siguiente

            

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

    def getMeses(self,year):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.year == year:
                    return aux.meses
                aux = aux.siguiente
    
    def verificarYear(self,year):
        aux = self.inicio
        if self.vacia():
            return False
        while aux != None:
            if aux.year == year:
                return True
            aux = aux.siguiente
        return False

    def getYear(self,year):
        aux = self.inicio
        if self.vacia():
            return None
        while aux != None:
            if aux.year == year:
                return aux
            aux = aux.siguiente
        return None

    def mostrarYears(self):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                print("******* AÑO *******")
                print("Año: "+str(aux.year))
                print("******* MESES *******")
                aux.meses.mostrarMeses()
                print("********* SEMESTRE *********")
                aux.semestres.mostrarSemestres()

                aux = aux.siguiente
            
            