from ArbolAVL.ArbolAVL import AVLTree
import os

class Graficar():
    def graficar(cadena,titulo):
        file = open(titulo+".dot","w")
        file.write("digraph G {\n"+cadena+"\n}")
        file.close()
        os.system('dot -Tsvg '+titulo+'.dot -o '+titulo+'.svg')


t = AVLTree()

t.add(201801119,1,"Bryan","Sistemas","gmail","1234",7,22)
t.add(201801170,12,"Eduardo","Sistemas","gmail","1234",7,22)
t.add(201801115,123,"Caal","Sistemas","gmail","1234",7,22)
t.add(201801180,3,"Racanac","Sistemas","gmail","1234",7,22)
t.add(201801120,32,"Daniel","Sistemas","gmail","1234",7,22)
t.add(201801105,321,"Lopez","Sistemas","gmail","1234",7,22)
t.add(201801157,7,"Perez","Sistemas","gmail","1234",7,22)

cadena = t.preorder()

Graficar.graficar(cadena,"Estudiantes")

t.modificar(201801157,7,"Gonzales","Industrial","gmail","1234",7,25)

cadena = t.preorder()

Graficar.graficar(cadena,"Estudiantes2")

buscado = t.buscar(201801180)

print("Nombre: "+buscado.nombre)