from NodoEstudiante import Node

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad):
        self.root = self._add( carnet, dpi, nombre, carrera, correo, password, creditos, edad, self.root)
    
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
            tmp.left=self._add(carnet, tmp.left)
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
        tmp.left = srr(tmp.left)
        return srl(tmp)
    
    def drr(self, tmp):
        tmp.right = srl(tmp.right)
        return srr(tmp)

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.carnet,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(tmp.carnet,end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.carnet,end = ' ')
           

#init
t = AVLTree()

#add
t.add(5)
t.add(10)
t.add(20)
t.add(25)
t.add(30)
t.add(35)
t.add(50)

#print traversals
t.preorder()
print()
t.inorder()
print()
t.postorder()