from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/carga', methods=['POST'])
def carga():
    datos = request.get_json()

    if( datos["tipo"] == "estudiantes"):
        print("Cargando Estudiantes...")
        file = open(datos["path"],"r", encoding="utf-8")
        mensaje = file.read()
        print(mensaje)

    elif( datos["tipo"] == "recordatorio"):
        print("Recordatorio")

    elif( datos["tipo"] == "cursos"):
        print("cursos del pensum")


    return jsonify({"message":"Informacion aceptada"})
    

if __name__ == '__main__':
    app.run(debug=True, port=3000)