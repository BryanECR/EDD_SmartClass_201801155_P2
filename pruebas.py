import builtins


class Node:
    def __init__(self, value,nombre):
        self.value  = value
        self.nombre = nombre
        self.left   = None
        self.right  = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value,nombre):
        self.root = self._add(value, nombre, self.root)
    
    def _add(self, value, nombre, tmp):
        if tmp is None:
            return Node(value,nombre)        
        elif value>tmp.value:
            tmp.right=self._add(value, nombre, tmp.right)
            if (self.height(tmp.right)-self.height(tmp.left))==2:
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, nombre, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<tmp.left.value:
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
        self._preorder(self.root)


    def _preorder(self, tmp):
        if tmp:
            #print(tmp.carnet,end = ' ')
            print(str(tmp.value)+"[label=\""+str(tmp.value)+"\n"+tmp.nombre+"\" shape=box]")
            if tmp.left != None:
                print(str(tmp.left.value)+"[label=\""+str(tmp.left.value)+"\n"+tmp.left.nombre+"\" shape=box]")
                print(str(tmp.value)+" -> "+str(tmp.left.value))
            
            if tmp.right != None:
                print(str(tmp.right.value)+"[label=\""+str(tmp.right.value)+"\n"+tmp.right.nombre+"\" shape=box]")
                print(str(tmp.value)+" -> "+str(tmp.right.value))

            self._preorder(tmp.left)
            self._preorder(tmp.right)
        

    # Buscar

    def buscar(self,busqueda):
        return self.__buscar(self.root, busqueda)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.value == busqueda:
            return nodo
        if busqueda < nodo.value:
            return self.__buscar(nodo.left, busqueda)
        else:
            return self.__buscar(nodo.right, busqueda)

    # Modificar

    def modificar(self, value, nombre):
        self.__modificar(self.root, value, nombre)

    def __modificar(self, nodo, value, nombre):
        if nodo is None:
            return None
        if nodo.value == value:
            nodo.nombre = nombre
        if value < nodo.value:
            return self.__modificar(nodo.left, value, nombre)
        else:
            return self.__modificar(nodo.right, value, nombre)

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

        
    
           

#init
t = AVLTree()

#add
t.add(35,"Francisco")
t.add(20,"Caal")
t.add(50,"Carlos")
t.add(5,"Bryan")
t.add(25,"Racanac")
t.add(30,"Daniel")
t.add(10,"Eduardo")


t.preorder()
print("******************************")
t.delete(10)
t.preorder()
print("******************************")
t.add(3,"otro")
t.preorder()







