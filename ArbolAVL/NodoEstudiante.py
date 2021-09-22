class Node:
    def __init__(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad, years=None):
        self.carnet  = carnet
        self.dpi  = dpi
        self.nombre  = nombre
        self.carrera  = carrera
        self.correo  = correo
        self.password  = password
        self.creditos  = creditos
        self.edad  = edad
        self.years = years
        self.left   = None
        self.right  = None
        self.height = 0