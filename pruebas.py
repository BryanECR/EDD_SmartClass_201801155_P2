import json
import json

with open('CursosEstudiante.txt') as f:
    data = json.load(f)

for i in data["estudiantes"]:
    print(i)