from ListaDoble.ListaEnlazadaDoble import ListaMeses, ListaTareasDiaria
from ListaSimple.ListaEnlazadaSimple import ListaYear
from Analizador.Syntactic import user_list, task_list
from MatrizDispersa.Matrix import Matriz_ortogonal
from flask import Flask, jsonify, request
from Analizador.Syntactic import parser
from ArbolAVL.ArbolAVL import AVLTree


arbolEstudiantes = AVLTree()

app = Flask(__name__)

def addTaskToStudent(informacion):
    datos = str(informacion["fecha"]).split("/")
    hour = int(informacion["hora"].replace(":00",""))
    year = int(datos[2]) 
    month = int(datos[1])
    day = int(datos[0])
    estudiante = arbolEstudiantes.buscar(informacion["carnet"])
    print("carnet"+informacion["carnet"]+" Año: "+str(year)+" Mes: "+str(month)+" Dia: "+str(day)+" hora: "+str(hour))

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
            addTaskToStudent(d2[i])

    elif( datos["tipo"] == "recordatorio"):
        print("Recordatorio")

    elif( datos["tipo"] == "cursos"):
        print("cursos del pensum")


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
        try:
            estudiante = arbolEstudiantes.buscar(datos["carnet"])
            year = estudiante.years.getNodo(datos["año"])
            mes = year.meses.GraficarMatrix(datos["mes"])
            mes.graficar_matriz()
            return jsonify({"Grafica":"La Grafica se genero exitosamente"})
        except:
            return jsonify({"Error":"Se Produjo un error al generar la grafica"})

    #Generar la Grafica de la lista de tareas en un dia especifico
    elif( datos["tipo"] == 2):

        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        year = estudiante.years.getYear(datos["año"])
        mes = year.meses.GraficarMatrix(datos["mes"])
        mes.graficar_matriz()
        mes.buscarGraficar(datos["dia"],datos["hora"])
        return jsonify({"Grafica":"La Grafica se genero exitosamente"})


    #Generar Graficaa de arbol de cursos del pensum
    elif( datos["tipo"] == 3):
        print("nada aun")

     #Generar Graficaa de arbol de cursos de un semestre en especifico
    elif( datos["tipo"] == 4):
        print("nada aun")

    return jsonify({"message":"Informacion aceptada"})    

@app.route('/estudiante', methods=['POST','UPDATE','GET'])
def estudiante():
    datos = request.get_json()
    if request.method == 'POST':
        arbolEstudiantes.add(datos["carnet"],datos["dpi"],datos["nombre"],datos["carrera"],datos["correo"],datos["password"],datos["creditos"],datos["edad"])
        return jsonify({"Message":"Agregado con exito"})
    
    elif request.method == 'UPDATE':
        arbolEstudiantes.modificar(datos["carnet"],datos["dpi"],datos["nombre"],datos["carrera"],datos["correo"],datos["password"],datos["creditos"],datos["edad"])
        return jsonify({"Message":"Modificado con exito"})

    info = arbolEstudiantes.buscar(datos["carnet"])
    return jsonify({"Carnet": info.carnet, "DPI": info.dpi, "Nombre": info.nombre, "Carrera": info.carrera, "Correo": info.correo, "Password": info.password, "Creditos": info.creditos, "Edad": info.edad})




if __name__ == '__main__':
    app.run(debug=True, port=3000)