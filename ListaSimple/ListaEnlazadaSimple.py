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

    def setCursos(self,semestre,arbolb):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.semestre == semestre:
                    aux.arbol = arbolb
                aux = aux.siguiente

    def getCursos(self,semestre):
        aux = self.inicio

        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.semestre == semestre:
                    return aux.arbol
                aux = aux.siguiente

            

class ListaYear():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacia(self):
        return self.inicio == None

    def incertarYear(self,year):
        if self.vacia():
            self.inicio = self.fin = NodoYear(year)
        else:
            aux = self.fin
            self.fin = aux.siguiente = NodoYear(year)

    #Verifica si existe el año que se esta buscando
    def verificarYear(self,year):
        aux = self.inicio
        if self.vacia():
            return False
        while aux != None:
            if aux.year == year:
                return True
            aux = aux.siguiente
        return False

    #agregar semestres
    def setSemestres(self,year,semestre):
        aux = self.inicio
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.year == year:
                    aux.semestres = semestre
                aux = aux.siguiente

    #agregar semestres
    def getSemestres(self,year):
        aux = self.inicio
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.year == year:
                    return aux.semestres
                aux = aux.siguiente

    #agregar meses
    def agregarMeses(self,year,meses):
        aux = self.inicio
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.year == year:
                    aux.meses = meses
                aux = aux.siguiente

    # Retorna el Nodo
    def getNodo(self,year):
        aux = self.inicio
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux != None:
                if aux.year == year:
                    return aux
                aux = aux.siguiente

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
            
            