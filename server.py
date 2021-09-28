from ListaDoble.ListaEnlazadaDoble import ListaMeses, ListaTareasDiaria
from ListaSimple.ListaEnlazadaSimple import ListaYear
from Analizador.Syntactic import user_list, task_list
from MatrizDispersa.Matrix import Matriz_ortogonal
from flask import Flask, jsonify, request
from Analizador.Syntactic import parser
from ArbolAVL.ArbolAVL import AVLTree


arbolEstudiantes = AVLTree()

app = Flask(__name__)

@app.route('/carga', methods=['POST'])
def carga():
    datos = request.get_json()

    if( datos["tipo"] == "estudiantes"):
        print("Cargando Estudiantes...")
        file = open(datos["path"],"r", encoding="utf-8")        
        mensaje = file.read()
        file.close()
        parser.parse(mensaje)

        d1 = user_list.getListEstudiantes()
        for i in d1:
            arbolEstudiantes.add(d1[i]["carnet"],d1[i]["dpi"],d1[i]["nombre"],d1[i]["carrera"],d1[i]["correo"],d1[i]["password"],d1[i]["creditos"],d1[i]["edad"])
            

        print("------------------------")
        d2 = task_list.getListTask()
        for i in d2:
            #inicializar las estructuras
            Estructurayear = ListaYear()
            Estructurames = ListaMeses()
            Estructuramatrix = Matriz_ortogonal()
            Estructurataresadiaria = ListaTareasDiaria()

            #separar los datos de las fechas para crear sus respectivas estructuras
            fecha = d2[i]["fecha"].split("/")
            hora = d2[i]["hora"].replace(":00","")
            year = int(fecha[2])
            mes = int(fecha[1])
            dia = int(fecha[0])
            hora = int(hora)

            #******************** METODO PARA CREAR ESTRUCUTRAS DESDE CERO *********************************
            estudiante = arbolEstudiantes.buscar(d2[i]["carnet"])
            if estudiante.years == None:
                #Se La lista de tareas diarias
                Estructurataresadiaria.incertarTareaDiaria(d2[i]["carnet"],d2[i]["nombre"],d2[i]["materia"],d2[i]["descripcion"],d2[i]["fecha"],d2[i]["hora"],d2[i]["estado"])

                #Se crea la Matrix y se incerta el nodo anteriormente creado3
                Estructuramatrix.insertar(dia,mes,Estructurataresadiaria)

                #se crea el mes y se incerta la matrix anteriormente creada
                Estructurames.incertarMes(mes)
                Estructurames.agregarMatrix(mes,Estructuramatrix)

                #se crea la lista de años y se le agrega el mes anteriormente creado
                Estructurayear.incertarYear(year,"pendiente",Estructurames)

                #se agrega el año anteriormente creado a los datos del estudiante
                arbolEstudiantes.agregarYears(d2[i]["carnet"],Estructurayear)

            ''' 
            #******************** NO EXISTE EL AÑO *************************
            elif estudiante.years.verificarYear(year) == False :
                #Se La lista de tareas diarias
                Estructurataresadiaria.incertarTareaDiaria(d2[i]["carnet"],d2[i]["nombre"],d2[i]["materia"],d2[i]["descripcion"],d2[i]["fecha"],d2[i]["hora"],d2[i]["estado"])

                #Se crea la Matrix y se incerta el nodo anteriormente creado3
                Estructuramatrix.insertar(dia,mes,Estructurataresadiaria)

                #se crea el mes y se incerta la matrix anteriormente creada
                Estructurames.incertarMes(mes)
                Estructurames.agregarMatrix(mes,Estructuramatrix)

                estudiante.years.incertarYear(year,"pendiente",Estructurames)

            #******************** EXISTE EL AÑO PERO NO EL MES ***********************************
            elif estudiante.years.verificarYear(year) == True:
                moths = estudiante.verifica

            #******************** EXISTE EL AÑO EL MES Y LA MATRIZ Y SOLO SE DESEA AGREGAR UNA TAREA A UN NODO ***********************************
            
                #verificar si el mes existe
            '''

            f = d2[i]["fecha"].split("/")

            print("Año: "+str(f[2]))
            print("mes: "+str(int(f[1])))
            print("Dia: "+str(int(f[0])))            
            print("hora: "+d2[i]["hora"].replace(":00",""))
            print("carnet: "+d2[i]["carnet"])
            print("nombre: "+d2[i]["nombre"])
            print("estado: "+d2[i]["estado"])

        for i in d2:
            print(d2[i]["estado"])

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
        estudiante = arbolEstudiantes.buscar(datos["carnet"])
        year = estudiante.years.getYear(datos["año"])
        year.meses.GraficarMatrix(datos["mes"])

    #Generar la Grafica de la lista de tareas en un dia especifico
    elif( datos["tipo"] == 2):
        print("metodo aun no creado")

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