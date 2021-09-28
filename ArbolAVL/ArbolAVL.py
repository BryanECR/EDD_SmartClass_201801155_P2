from ArbolAVL.NodoEstudiante import Node
import os

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad):
        self.root = self._add(carnet, dpi, nombre, carrera, correo, password, creditos, edad, self.root)
    
    def _add(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad, tmp):
        if tmp is None:
            return Node( carnet, dpi, nombre, carrera, correo, password, creditos, edad)        
        elif carnet>tmp.carnet:
            tmp.right=self._add(carnet, dpi, nombre, carrera, correo, password, creditos, edad, tmp.right)
            if (self.height(tmp.right)-self.height(tmp.left))==2:
                if carnet>tmp.right.carnet:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            
            tmp.left = self._add(carnet, dpi, nombre, carrera, correo, password, creditos, edad, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if carnet<tmp.left.carnet:
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1

        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = self.srr(tmp.left)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.right = self.srl(tmp.right)
        return self.srr(tmp)

    #traversals

    def preorder(self):
        cadena = self._preorder(self.root)
        file = open("Estudiantes.dot","w")
        file.write("digraph G {\n"+cadena+"\n}")
        file.close()
        os.system('dot -Tsvg Estudiantes.dot -o Estudiantes.svg')


    def _preorder(self, tmp):
        cadena = ""
        if tmp:
            #print(tmp.carnet,end = ' ')
            if tmp.left != None:
                cadena += str(tmp.carnet)+"[label=\""+str(tmp.carnet)+"\n"+tmp.nombre+"\" shape=box]\n"
                cadena += str(tmp.left.carnet)+"[label=\""+str(tmp.left.carnet)+"\n"+tmp.left.nombre+"\" shape=box]\n"
                cadena += str(tmp.carnet)+" -> "+str(tmp.left.carnet)+"\n"
            
            if tmp.right != None:
                cadena += str(tmp.carnet)+"[label=\""+str(tmp.carnet)+"\n"+tmp.nombre+"\" shape=box]\n"
                cadena += str(tmp.right.carnet)+"[label=\""+str(tmp.right.carnet)+"\n"+tmp.right.nombre+"\" shape=box]\n"
                cadena += str(tmp.carnet)+" -> "+str(tmp.right.carnet)+"\n"

            cadena += self._preorder(tmp.left)
            cadena += self._preorder(tmp.right)
        
        return cadena

    # Buscar
    def buscar(self,busqueda):
        return self.__buscar(self.root, busqueda)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.carnet == busqueda:
            return nodo
        if busqueda < nodo.carnet:
            return self.__buscar(nodo.left, busqueda)
        else:
            return self.__buscar(nodo.right, busqueda)

    # Modificar
    def modificar(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad):
        self.__modificar(self.root, carnet, dpi, nombre, carrera, correo, password, creditos, edad)

    def __modificar(self, nodo, carnet, dpi, nombre, carrera, correo, password, creditos, edad):
        if nodo is None:
            return None

        if nodo.carnet == carnet:
            nodo.dpi = dpi
            nodo.nombre = nombre
            nodo.carrera = carrera
            nodo.correo = correo
            nodo.password = password
            nodo.creditos = creditos
            nodo.edad = edad
        if carnet < nodo.carnet:
            return self.__modificar(nodo.left, carnet, dpi, nombre, carrera, correo, password, creditos, edad)

        else:
            return self.__modificar(nodo.right, carnet, dpi, nombre, carrera, correo, password, creditos, edad)
    
    #Agregar Lista de años
    def agregarYears(self, carnet,years):
        self.__agregarYears(self.root, carnet, years)

    def __agregarYears(self, nodo, carnet, years):
        if nodo is None:
            return None
        if nodo.carnet == carnet:
            nodo.years = years
        if carnet < nodo.carnet:
            return self.__agregarYears(nodo.left, carnet, years)
        else:
            return self.__agregarYears(nodo.right, carnet, years)


    # Imprimir datos
    def imprimir(self):
        print("************* ARBOL *************")
        self._imprimir(self.root)

    def _imprimir(self, tmp):
        if tmp:
            print("Carnet: "+tmp.carnet)
            print("DPI: "+tmp.dpi)
            print("Nombre: "+tmp.nombre)
            print("Carrera: "+tmp.carrera)
            print("Correo: "+tmp.correo)
            print("Password: "+tmp.password)
            print("Creditos: "+str(tmp.creditos))
            print("Edad: "+str(tmp.edad))
            tmp.years.mostrarYears()
            self._imprimir(tmp.left)            
            self._imprimir(tmp.right)

    #Retornar la lista de años
    def getYears(self,carnet):
        return self.__getYears(self.root, carnet)

    def __getYears(self, nodo, carnet):
        if nodo is None:
            return None
        if nodo.carnet == carnet:
            return nodo.years
        if carnet < nodo.carnet:
            return self.__getYears(nodo.left, carnet)
        else:
            return self.__getYears(nodo.right, carnet)


