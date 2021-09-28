from MatrizDispersa.Matrix import Matriz_ortogonal
from ListaDoble.ListaEnlazadaDoble import ListaTareasDiaria


lista1 = ListaTareasDiaria()
lista2 = ListaTareasDiaria()
lista3 = ListaTareasDiaria()
lista4 = ListaTareasDiaria()
lista5 = ListaTareasDiaria()

matrix = Matriz_ortogonal()
#Incertar una tarea en la lista de tareas
lista1.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista1.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista1.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")

lista2.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista2.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista2.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista2.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista2.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")

lista3.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")

lista4.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")
lista4.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")

lista5.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")

#incertar la lista en la matrix
matrix.insertar(5,6,lista1)
matrix.insertar(9,10,lista2)
matrix.insertar(10,6,lista3)
matrix.insertar(10,5,lista4)
matrix.insertar(16,16,lista5)


#incertar otra tarea en el mismo nodo de la lista
matrix.graficar_matriz()


#buscar un nodo inexistente y uno existente
print(matrix.buscar(16,16))
print(matrix.buscar(1,1))

if matrix.buscar(16,16):
    lista = matrix.buscarAgregar(16,16)
    lista.incertarTareaDiaria("201801155","Bryan Caal","APLI1","Hacer tarea especial","12/05/80","8:00","incumplido")


matrix.graficar_matriz()
matrix.buscarGraficar(16,16)


'''
Verificar si el año existe, si no existe crearlo
si existe verificar si ya se creo el mes, sin no existe crearlo
si el mes existe verificar si ya se creo la matrix, si no crearla
si la matrix existe verificar si ya se creo el nodo, si no agregarlo
si el nodo ya se creo agregarlo
'''