''' 
    from ArbolAVL.ArbolAVL import AVLTree
    from ListaDoble.ListaEnlazadaDoble import ListaTareasDiaria
    from ListaDoble.ListaEnlazadaDoble import ListaMeses
    from ListaSimple.ListaEnlazadaSimple import ListaSemestre,ListaYear
    from MatrizDispersa.Matrix import Matriz_ortogonal


    arbolEstudiantes = AVLTree()
    Tad1 = ListaTareasDiaria()
    Tad2 = ListaTareasDiaria()
    Tad3 = ListaTareasDiaria()
    Tad4 = ListaTareasDiaria()
    Tad5 = ListaTareasDiaria()
    matrix1 = Matriz_ortogonal()
    meses = ListaMeses()
    meses2 = ListaMeses()
    semestre = ListaSemestre()
    semestre2 = ListaSemestre()
    year = ListaYear()
    year2 = ListaYear()
    year3 = ListaYear()
    year4 = ListaYear()

    # Ingresar datos de estudiantes
    arbolEstudiantes.add("201801155","3629635920115","Bryan Caal","Ingenieria en Sistemas","caaal320@gmail.com","bryan1234",100,22)
    arbolEstudiantes.add("201901425","3502451230508","Emilia Miramontes","Ingenieria en Ciencias y Sistemas","abrahamz@outlook.com","roxodiciqi",205,21)
    arbolEstudiantes.add("201501786","7249529279753","Juan Curiel","Ingenieria Industrial","obrunelleschid@hotmail.com","zanolexima",245,24)
    arbolEstudiantes.add("201822186","9298434863898","Eloisa Rincón","Ingenieria Civil","epalleske9@gmail.org","toqelijanu",95,19)
    arbolEstudiantes.add("201704186","9298434865874","Eloisa chacon","Ingenieria Civil","awoodwin121@gmail.com","toqelijanu",77,22)

    # Crear Tareas Diarias
    Tad1.incertarTareaDiaria("201801155","Bryan Caal","EDD","Tarea Especial","12/09/2021","8:00","Incumplida")
    Tad1.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")
    Tad1.incertarTareaDiaria("201801155","Bryan Caal","Apli1","Tarea","15/08/2021","23:00","Proceso")

    Tad2.incertarTareaDiaria("201801155","Bryan Caal","EDD","Tarea Especial","12/09/2021","8:00","Incumplida")
    Tad2.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")

    Tad3.incertarTareaDiaria("201801155","Bryan Caal","EDD","Tarea Especial","12/09/2021","8:00","Incumplida")
    Tad3.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")
    Tad3.incertarTareaDiaria("201801155","Bryan Caal","Apli1","Tarea","15/08/2021","23:00","Proceso")

    Tad4.incertarTareaDiaria("201801155","Bryan Caal","EDD","Tarea Especial","12/09/2021","8:00","Incumplida")
    Tad4.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")
    Tad4.incertarTareaDiaria("201801155","Bryan Caal","Apli1","Tarea","15/08/2021","23:00","Proceso")

    Tad5.incertarTareaDiaria("201801155","Bryan Caal","EDD","Tarea Especial","12/09/2021","8:00","Incumplida")
    Tad5.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")
    Tad5.incertarTareaDiaria("201801155","Bryan Caal","Apli1","Tarea","15/08/2021","23:00","Proceso")
    Tad5.incertarTareaDiaria("201801155","Bryan Caal","COMPI1","P1","16/09/2021","9:00","Realizado")
    Tad5.incertarTareaDiaria("201801155","Bryan Caal","Apli1","Tarea","15/08/2021","23:00","Proceso")

    # Crear Matrix
    matrix1.insertar(1,1,Tad1)
    matrix1.insertar(2,5,Tad2)
    matrix1.insertar(5,1,Tad5)
    matrix1.insertar(5,16,Tad3)
    matrix1.insertar(22,16,Tad1)
    matrix1.insertar(10,5,Tad4)
    matrix1.insertar(15,1,Tad1)
    matrix1.insertar(15,15,Tad2)

    # Crear Meses
    meses.incertarMes("Mes 1")
    meses.agregarMatrix("Mes 1",matrix1)

    meses.incertarMes("Mes 5")
    meses.agregarMatrix("Mes 5",matrix1)

    meses.incertarMes("Mes 6")
    meses.agregarMatrix("Mes 6",matrix1)

    meses.incertarMes("Mes 7")
    meses.agregarMatrix("Mes 7",matrix1)

    meses.incertarMes("Mes 3")
    meses.agregarMatrix("Mes 3",matrix1)

    # Crear Semestre
    semestre.incertarSemestre("semestre 1")
    semestre.incertarSemestre("semestre 2")

    # Crear Años
    year.incertarYear("2018",semestre,meses)
    year.incertarYear("2019",semestre,meses)
    year.incertarYear("2020",semestre,meses)
    year.incertarYear("2021",semestre,meses)

    # Ingresar al arbol de estudiantes
    arbolEstudiantes.agregarYears("201801155",year)

    arbolEstudiantes.agregarYears("201901425",year)

    arbolEstudiantes.agregarYears("201501786",year)

    arbolEstudiantes.agregarYears("201822186",year)

    arbolEstudiantes.agregarYears("201704186",year)


    # Imprimir
    arbolEstudiantes.imprimir()

'''

def fechas(fecha,hora):
    datos = fecha.split("/")
    for i in range(len(datos)):
        print(datos[i])

    datos2 = hora.split(":")
    for i in range(len(datos2)):
        print(datos2[i])

fecha = "22/09/2021"
hora = "8:00"

fechas(fecha,hora)