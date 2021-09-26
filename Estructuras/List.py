from Estructuras.NodeS import NodeS

class List:
    def __init__(self):
        self.First = None
        self.Last = None

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next()

        return counter

    def isEmpty(self):
        return self.First is None

    def getListEstudiantes(self):
        contador = 0
        d1 = {}
        aux = self.First
        while aux is not None:
            d1[contador] = {"carnet":aux.Carnet,  "dpi":aux.DPI,"nombre":aux.Nombre, "carrera":aux.Carrera , "correo":aux.Correo,"password":aux.Password,"creditos":aux.Creditos,"edad":aux.Edad}
            #print(aux.Carnet + " - " + aux.Nombre + "-" + aux.DPI + "-" + aux.Descripcion + "-" + aux.Correo)
            contador+=1
            aux = aux.Next
        
        return d1

    def getListTask(self):
        contador = 0
        d1 = {}
        aux = self.First
        while aux is not None:
            d1[contador] = {"carnet":aux.Carnet,"nombre":aux.Nombre, "descripcion":aux.Descripcion , "fecha":aux.Fecha,"hora":aux.Hora,"estado":aux.Estado}
            #print(aux.Carnet + " - " + aux.Nombre + "-" + aux.DPI + "-" + aux.Descripcion + "-" + aux.Correo)
            contador+=1
            aux = aux.Next
        
        return d1

    def insertValue(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado):
        new_node = NodeS(carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado)

        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node

