from ArbolAVL.ArbolAVL import AVLTree
from ListaDoble.ListaEnlazadaDoble import ListaMeses,ListaTareasDiaria
from ListaSimple.ListaEnlazadaSimple import ListaYear
from MatrizDispersa.Matrix import Matriz_ortogonal

estudiantes = AVLTree()
# Creacion de estudiantes
estudiantes.add("201801155","1","Bryan Caal","Sistemas","caal320","1234",105,22)
estudiantes.add("201801143","2","Eduardo Racanac","Sistemas","caal320","1234",200,24)
estudiantes.add("201801176","3","Efrain Lopez","Sistemas","caal320","1234",77,19)
estudiantes.add("201801135","4","Carlos Perez","Sistemas","caal320","1234",77,19)
estudiantes.add("201801150","5","Naruto Uzumaki","Sistemas","caal320","1234",77,19)
estudiantes.add("201801163","6","Monkey Luffy","Sistemas","caal320","1234",77,19)
estudiantes.add("201801180","7","Monkey Luffy","Sistemas","caal320","1234",77,19)

#Funcion

def addTaskToStudent(informacion):
    datos = str(informacion["fecha"]).split("/")
    hour = int(informacion["hora"].replace(":00",""))
    year = int(datos[2]) 
    month = int(datos[1])
    day = int(datos[0])
    estudiante = estudiantes.buscar(informacion["carnet"])
    #print("carnet"+informacion["carnet"]+" Año: "+str(year)+" Mes: "+str(month)+" Dia: "+str(day)+" hora: "+str(hour))

    #Se confirma si el estudiante tiene la lista de años creada
    if estudiante.years == None:
        # Como el estudiante no tiene años creado se crean todas las estructuras para agregar la estrucutra de años
        tareas = ListaTareasDiaria()
        tareas.incertarTareaDiaria(informacion["carnet"],informacion["nombre"],informacion["materia"],informacion["descripcion"],informacion["fecha"],informacion["hora"],informacion["estado"])
        matrix = Matriz_ortogonal()
        matrix.insertar(day,hour,tareas)
        mes = ListaMeses()
        mes.incertarMes(month)
        mes.agregarMatrix(month,matrix)
        listYear = ListaYear()
        listYear.incertarYear(year)
        listYear.agregarMeses(year,mes)
        estudiantes.agregarYears(informacion["carnet"],listYear)

    # Si el estudiante tiene la Estructura de años ya hecha entonces se agregan los nuevos datos
    elif estudiante.years != None:
        # Verificamos si el año existe
        if estudiante.years.verificarYear(year):
            actualYear = estudiante.years.getNodo(year)
            # Verificar si el mes existe en ese año, si existe se agrega informacion
            if actualYear.meses.verificarMes(month):
                actualmatrix = actualYear.meses.getMatrix(month)
                # Verifico si el nodo de la matrix esta en uso
                if actualmatrix.buscar(day,hour):
                    tareas = actualmatrix.buscarAgregar(day,hour)
                    tareas.incertarTareaDiaria(informacion["carnet"],informacion["nombre"],informacion["materia"],informacion["descripcion"],informacion["fecha"],informacion["hora"],informacion["estado"])

                # Si el nodo esta en uso se crea y se incerta en la matriz
                else:
                    tareas = ListaTareasDiaria()
                    tareas.incertarTareaDiaria(informacion["carnet"],informacion["nombre"],informacion["materia"],informacion["descripcion"],informacion["fecha"],informacion["hora"],informacion["estado"])
                    actualmatrix.insertar(day,hour,tareas)

            # Si el mes no existe se crea
            else:
                tareas = ListaTareasDiaria()
                tareas.incertarTareaDiaria(informacion["carnet"],informacion["nombre"],informacion["materia"],informacion["descripcion"],informacion["fecha"],informacion["hora"],informacion["estado"])
                matrix = Matriz_ortogonal()
                matrix.insertar(day,hour,tareas)
                actualYear.meses.incertarMes(month)

        # Si el año no existe
        else:
            tareas = ListaTareasDiaria()
            tareas.incertarTareaDiaria(informacion["carnet"],informacion["nombre"],informacion["materia"],informacion["descripcion"],informacion["fecha"],informacion["hora"],informacion["estado"])
            matrix = Matriz_ortogonal()
            matrix.insertar(day,hour,tareas)
            mes = ListaMeses()
            mes.incertarMes(month)
            mes.agregarMatrix(month,matrix)
            estudiante.years.incertarYear(year)
            estudiante.years.agregarMeses(year,mes)


    
diccionario1 = {"carnet":"201801180","nombre":"TAREA MATE","materia":"Mate","descripcion":"algo","fecha":"02/05/2021","hora":"7:00","estado":"incumplida"}
addTaskToStudent(diccionario1)
diccionario2 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Pendiente"}
addTaskToStudent(diccionario2)
diccionario3 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario3)
diccionario4 = {"carnet":"201801180","nombre":"Tarea Fisica","materia":"Fisica","descripcion":"algo","fecha":"16/10/2019","hora":"10:00","estado":"Pendiente"}
addTaskToStudent(diccionario4)
diccionario5 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario5)
diccionario6 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario6)
diccionario7 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario7)
diccionario8 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario8)
diccionario9 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario9)
diccionario10 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario10)
diccionario11 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario11)
diccionario12 = {"carnet":"201801180","nombre":"Tarea Logica","materia":"Logica","descripcion":"algo","fecha":"08/05/2021","hora":"7:00","estado":"Finalizada"}
addTaskToStudent(diccionario12)


estudiante = estudiantes.buscar("201801180")
year = estudiante.years.getNodo(2021)
mes = year.meses.getMatrix(5)
mes.graficar_matriz()
mes.buscarGraficar(8,7)


