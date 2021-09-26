from Analizador.Syntactic import parser
from Analizador.Syntactic import user_list, task_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('Estudiantes.txt',"r", encoding="utf-8")
    mensaje = f.read()
    # print(mensaje)
    f.close()
    # parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
    parser.parse(mensaje)

    d1 = user_list.getListEstudiantes()

    for i in d1:
        print(d1[i]["nombre"])

    print("------------------------")
    d2 = task_list.getListTask()

    for i in d2:
        print(d2[i]["estado"])