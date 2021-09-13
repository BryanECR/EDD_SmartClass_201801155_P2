class NodoCursos:
    def __init__(self,codigo,nombre,creditos,pre,obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.pre = pre
        self.obligatorio = obligatorio
        self.izquierda = None
        self.derecha = None