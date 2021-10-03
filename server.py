from ListaDoble.ListaEnlazadaDoble import ListaMeses, ListaTareasDiaria
from ListaSimple.ListaEnlazadaSimple import ListaYear,ListaSemestre
from Analizador.Syntactic import user_list, task_list
from MatrizDispersa.Matrix import Matriz_ortogonal
from flask import Flask, jsonify, request
from Analizador.Syntactic import parser
from ArbolAVL.ArbolAVL import AVLTree
from ArbolB.ArbolB import BTree
import json

arbolEstudiantes = AVLTree()
b = BTree(5)

app = Flask(__name__)

def addTaskToStudent(informacion):
    datos = str(informacion["fecha"]).split("/")
    hour = int(informacion["hora"].replace(":00",""))
    year = int(datos[2]) 
    month = int(datos[1])
    day = int(datos[0])
    estudiante = arbolEstudiantes.buscar(informacion["carnet"])
    #print("carnet: "+informacion["carnet"]+" Año: "+str(year)+" Mes: "+str(month)+" Dia: "+str(day)+" hora: "+str(hour))

    try:
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
            arbolEstudiantes.agregarYears(informacion["carnet"],listYear)

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
    except:
        print("*** Error ***")
        print("Carnet: "+informacion["carnet"]+" Fecha: "+informacion["fecha"]+" Hora: "+informacion["hora"])


@app.route('/carga', methods=['POST'])
def carga():
    datos = request.get_json()

    if( datos["tipo"] == "estudiantes"):
        print("Cargando Estudiantes...")
        file = open(datos["path"],"r", encoding="utf-8")        
        mensaje = file.read()
        file.close()
        parser.parse(mensaje)

        # Creacion del arbol de los estudiantes
        d1 = user_list.getListEstudiantes()
        for i in d1:
            arbolEstudiantes.add(d1[i]["carnet"],d1[i]["dpi"],d1[i]["nombre"],d1[i]["carrera"],d1[i]["correo"],d1[i]["password"],d1[i]["creditos"],d1[i]["edad"])
            

        # Creacion de las estructras para los estudiantes
        d2 = task_list.getListTask()
        for i in d2:
            if arbolEstudiantes.verificarEstudiante(d2[i]["carnet"]):
                addTaskToStudent(d2[i])

    return jsonify({"message":"Informacion aceptada"})


@app.route('/reportes', methods=['GET'])
def reportes():
    datos = request.get_json()

    #Generar Grafica de Arbol de estudiantes
    if( datos["tipo"] == 0 ):
        arbolEstudiantes.preorder() 

    #Generar grafica de Matriz de tareas
    elif( datos["tipo"] == 1 ):
        #se tomaran los datos de carnet, año y mes
        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        #print("Estudiante"+estudiante.carnet)
        year = estudiante.years.getNodo(int(datos["año"]))
        #print("Año: "+str(year))
        mes = year.meses.GraficarMatrix(datos["mes"])
        #mes.graficar_matriz()
        return jsonify({"Grafica":"La Grafica se genero exitosamente"})


    #Generar la Grafica de la lista de tareas en un dia especifico
    elif( datos["tipo"] == 2):
        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        year = estudiante.years.getNodo(int(datos["año"]))
        mes = year.meses.getMatrix(datos["mes"])
        mes.buscarGraficar(datos["dia"],datos["hora"])
        return jsonify({"Grafica":"La Grafica se genero exitosamente"})


    #Generar Graficaa de arbol de cursos del pensum
    elif( datos["tipo"] == 3):
        print("Arbol B de cursos del pensum")
        print("*************** Arbol de Cusos del Pensum ***************")
        print(b)
        

    #Generar Graficaa de arbol de cursos de un semestre en especifico
    elif( datos["tipo"] == 4):
        datos = request.get_json()
        print("arbol B de cursos de un estudiante en especifico")
        # se Busca al estudiante y se retorna toda su informacion
        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        # Se busca en la lista de años el año buscado y se retorna la informacion de sus semestres
        if estudiante.years.verificarYear(int(datos["año"])):
            # se retorna la lista de semestres
            year = estudiante.years.getNodo(int(datos["año"]))
            # se imprime el arbol
            print("*************** Arbol de Cusos del Semestre ***************")
            year.semestres.getCursos(datos["semestre"])

        else:
            return jsonify({"mensaje":"El año que busca no existe"})

    return jsonify({"message":"Informacion aceptada"})    

@app.route('/estudiante', methods=['POST','PUT','GET'])
def estudiante():
    datos = request.get_json()
    if request.method == 'POST':
        arbolEstudiantes.add(datos["carnet"],datos["dpi"],datos["nombre"],datos["carrera"],datos["correo"],datos["password"],datos["creditos"],datos["edad"])
        return jsonify({"Message":"Agregado con exito"})
    
    elif request.method == 'PUT':
        arbolEstudiantes.modificar(datos["carnet"],datos["dpi"],datos["nombre"],datos["carrera"],datos["correo"],datos["password"],datos["creditos"],datos["edad"])
        return jsonify({"Message":"Modificado con exito"})

    info = arbolEstudiantes.buscar(datos["carnet"])
    return jsonify({"Carnet": info.carnet, "DPI": info.dpi, "Nombre": info.nombre, "Carrera": info.carrera, "Correo": info.correo, "Password": info.password, "Creditos": info.creditos, "Edad": info.edad})


@app.route('/recordatorios', methods= ['POST','PUT','GET'])
def recordatorios():
    datos = request.get_json()
    if request.method == 'POST':
        if(arbolEstudiantes.verificarEstudiante(datos["carnet"])):
            addTaskToStudent(datos)
            return jsonify({"Mensaje": "Recordatorio agregado exitosamente"})
        return jsonify({"Mensaje":"El carnet no existe en la base de datos"})

    elif request.method == 'PUT':
        fecha = datos["fecha"].split("/")
        day = int(fecha[0])
        month = int(fecha[1])
        year = int(fecha[2])
        hour = int(datos["hora"].replace(":00",""))

        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        actualyear = estudiante.years.getNodo(year)
        mes = actualyear.meses.getMatrix(month)
        tareas = mes.getLista(day,hour)
        tareas.ModificarTarea(datos["carnet"],datos["nombre"],datos["descripcion"],datos["materia"],datos["fecha"],datos["hora"],datos["estado"],datos["posicion"])

        return({"Mensaje":"Se Modifico Correctamente"})

    elif request.method == 'GET':
        fecha = datos["fecha"].split("/")
        day = int(fecha[0])
        month = int(fecha[1])
        year = int(fecha[2])
        hour = int(datos["hora"].replace(":00",""))

        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        actualyear = estudiante.years.getNodo(year)
        mes = actualyear.meses.getMatrix(month)
        tareas = mes.getLista(day,hour)

        return jsonify(tareas)



@app.route('/CursosPensum', methods=['POST'])
def CursosPensum():
    datos = request.get_json()
    print("Cargando Cursos del Pensum...")

    with open(datos["path"]) as f:
        datos = json.load(f)
        f.close()

    for curso in datos["cursos"]:
        b.insert(int(curso["codigo"]))

    return jsonify({"mensaje":"Arbol de cursos generado con exito"})
    

@app.route('/CursosEstudiante', methods=['POST'])
def CursosEstudiante():
    data = request.get_json()
    print("Cargando los Cursos del Estudiante...")
    #print(data["estudiantes"])
    # Se recorre la lista para incertar los cursos en los estudiantes
    for est in data["estudiantes"]:
        # Se verifica si el estudiante ya esta en el arbol
        estudiante = arbolEstudiantes.buscar(est["carnet"])
        # Se recorre la lista de años
        for year in est["años"]:
            # Se verifica si el año ya fue creado en la informacion del estudiante
            if estudiante.years.verificarYear(int(year["año"])):
                #se inicia la lista de semestre
                semestre = ListaSemestre()
                for sem in year["semestres"]:
                    # se incerta el nombre del semeste en la lista de semestres
                    semestre.incertarSemestre(sem["semestre"])
                    # se crea el arbol b para ingresarlo en la lista de semestre
                    arbolb = BTree(5)
                    # se recorre la lista de cursos para poderlos agregar a cada semestre
                    for curso in sem["cursos"]:
                        arbolb.insert(curso["codigo"])

                    semestre.setCursos(sem["semestre"],arbolb)
                    estudiante.years.setSemestres(int(year["año"]),semestre)

            # si el año no ha sido creado se crea
            else:
                estudiante.years.incertarYear(int(year["año"]))
                semestre = ListaSemestre()
                for sem in year["semestres"]:
                    # se incerta el nombre del semeste en la lista de semestres
                    semestre.incertarSemestre(sem["semestre"])
                    # se crea el arbol b para ingresarlo en la lista de semestre
                    arbolb = BTree(5)
                    # se recorre la lista de cursos para poderlos agregar a cada semestre
                    for curso in sem["cursos"]:
                        arbolb.insert(curso["codigo"])

                    semestre.setCursos(sem["semestre"],arbolb)
                    estudiante.years.setSemestres(int(year["año"]),semestre)     
    
    return jsonify({"mensaje":"Lectura de archivos hecho correctamente"})


if __name__ == '__main__':
    app.run(debug=True, port=3000)