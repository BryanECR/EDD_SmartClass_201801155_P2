from NodoCursos import NodoCursos

class ArbolB:

    def __init__(self):
        self.raiz = None
  
    def __agregar_recursivo(self, nodo, codigo,nombre,creditos,pre,obligatorio):
        if nodo is None:
            self.raiz = NodoCursos(codigo,nombre,creditos,pre,obligatorio)

        elif codigo < nodo.codigo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoCursos(codigo,nombre,creditos,pre,obligatorio)
            else:
                self.__agregar_recursivo(nodo.izquierda, codigo,nombre,creditos,pre,obligatorio)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoCursos(codigo,nombre,creditos,pre,obligatorio)
            else:
                self.__agregar_recursivo(nodo.derecha, codigo,nombre,creditos,pre,obligatorio)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.codigo, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.codigo, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.codigo, end=", ") 
    
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.codigo == busqueda:
            return nodo
        if busqueda < nodo.codigo:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, codigo,nombre,creditos,pre,obligatorio):
        self.__agregar_recursivo(self.raiz, codigo,nombre,creditos,pre,obligatorio)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)