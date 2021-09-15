from ArbolAVL.NodoEstudiante import Node

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
        t1.height = self.maxi(self.heigh(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.heigh(t2.left), t1.height)+1
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
        return self._preorder(self.root)


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
        

    # Cosas
    def balance(self,nodo):
        if not nodo:
            return 0
        
        return nodo.height

    def balanceFactor(self, node):
        return self.height(node.right) - self.height(node.left)

    def getNodeMin(self, nodo):
        if nodo is None or nodo.left is None:
            return nodo
        return self.getNodeMin(nodo.left)


    # Eliminar
    def delete(self, value):
        self.root = self.__deleteNode(self.root, value)

    def __deleteNode(self, nodo, value):

        if value < nodo.value:
            nodo.left = self.__deleteNode(nodo.left, value)

        elif value > nodo.value:
            nodo.right = self.__deleteNode(nodo.right, value)

        else:
            if nodo.left is None:
                temp = nodo.right
                nodo = None
                return temp
            
            elif nodo.right is None:
                temp = nodo.left
                nodo = None
                return temp

            temp = self.getNodeMin(nodo.right)
            nodo.value = temp.value
            nodo.right = self.__deleteNode(nodo.right,temp.value)
        
        if nodo is None:
            return nodo

        nodo.height = 1 + self.maxi(self.height(nodo.left),self.height(nodo.right))

        balance = self.balance(nodo)

        if balance > 1 and self.balance(nodo.left) < 0:
            nodo.left = self.srl(nodo.left)
            return self.srr(nodo)
 
        if balance < -1 and self.balance(nodo.right) > 0:
            nodo.right = self.srr(nodo.right)
            return self.srl(nodo)
 
        return nodo
    

           
'''
#init
t = AVLTree()

#add
t.add(201801119,1,"Bryan","Sistemas","gmail","1234",7,22)
t.add(201801170,12,"Eduardo","Sistemas","gmail","1234",7,22)
t.add(201801115,123,"Caal","Sistemas","gmail","1234",7,22)
t.add(201801180,3,"Racanac","Sistemas","gmail","1234",7,22)
t.add(201801120,32,"Daniel","Sistemas","gmail","1234",7,22)
t.add(201801105,321,"Lopez","Sistemas","gmail","1234",7,22)
t.add(201801157,7,"Perez","Sistemas","gmail","1234",7,22)

#print traversals
print( t.graficar() )



#t.inorder()
#print()
#t.postorder()

#Graficar en preorder
'''