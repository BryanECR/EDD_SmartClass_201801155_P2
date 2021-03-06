from ListaDoble.NodoDoble import NodoTD, NodoMes
import os

class ListaTareasDiaria():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertarTareaDiaria(self,carnet, nombre, materia, descripcion, fecha, hora, estado):
        if self.vacia():
            self.primero = self.ultimo = NodoTD(carnet, nombre, materia, descripcion, fecha, hora, estado)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoTD(carnet, nombre, materia, descripcion, fecha, hora, estado)
            self.ultimo.anterior = aux

    def getTareasDiarias(self):
        tareas = {}
        contador = 0
        aux = self.primero
        while aux:
            tareas[contador] = {"carnet":str(aux.carnet),"nombre":aux.nombre,"descripcion":aux.descripcion,"materia":aux.materia,"fecha":aux.fecha,"hora":aux.hora,"estado":aux.estado}
            contador+=1
            aux = aux.siguiente
        return tareas

    def ModificarTarea(self,carnet, nombre, materia, descripcion, fecha, hora, estado, posicion):
        aux = self.primero
        contador = 1
        while aux:
            if contador == posicion:
                aux.carnet = carnet
                aux.nombre = nombre
                aux.materia = materia
                aux.descripcion = descripcion
                aux.fecha = fecha 
                aux.hora = hora
                aux.estado = estado
            contador+=1
            aux = aux.siguiente

    def grafica(self):
        cadena = "digraph G {\n"
        contador = 0
        aux = self.primero
        while aux:
            cadena += "nodo"+str(contador)+"[shape=box label=\"Carnet: "+str(aux.carnet)+"\nNombre: "+aux.nombre+"\nDescripcion: "+aux.descripcion+"\nMateria: "+aux.materia+"\nFecha: "+aux.fecha+"\nHora: "+aux.hora+"\nEstado: "+aux.estado+"\"]\n"
            contador+=1
            aux = aux.siguiente

        for i in range(contador-1):
            cadena += "nodo"+str(i)+" -> nodo"+str(i+1)+" [dir=both]\n"

        cadena += "rankdir=LR;"
        cadena += "\n}"

        file = open("TareasDiarias.dot","w")
        file.write(cadena)
        file.close()
        os.system('dot -Tsvg TareasDiarias.dot -o TareasDiarias.svg')

        return cadena

    def sizeList(self):
        contador = 0
        aux = self.primero
        while aux:
            contador += 1
            aux = aux.siguiente

        return contador
    
class ListaMeses():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertarMes(self,mes):
        if self.vacia():
            self.primero = self.ultimo = NodoMes(mes)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoMes(mes)
            self.ultimo.anterior = aux

    def agregarMatrix(self,mes, matrix):
        aux = self.primero
        while aux:
            if mes == aux.mes:
                aux.matrix = matrix
            aux = aux.siguiente

    def getMatrix(self,mes):
        aux = self.primero
        while aux:
            if mes == aux.mes:
                return aux.matrix
            aux = aux.siguiente 

    # verificar si el mes que se esta buscando existe
    def verificarMes(self,mes):
        aux = self.primero
        if self.vacia():
            return False
        else:
            while aux:
                if mes == aux.mes:
                    return True
                aux = aux.siguiente
        return False

    def GraficarMatrix(self,mes):
        aux = self.primero
        while aux:
            if mes == aux.mes:
                aux.matrix.graficar_matriz()
            aux = aux.siguiente
    
    def mostrarMeses(self):
        aux = self.primero
        while aux:
            print("Mes: "+str(aux.mes))
            aux.matrix.imprimirMatrix()
            aux = aux.siguiente

