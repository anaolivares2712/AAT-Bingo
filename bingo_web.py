from jinja2 import Template
from src.bingo import tests

template = Template(open("Html/plantilla.j2").read())
file = open("bingo.html", "w")
file.write(template.render(carton = tests()))
file.close()
print("Creando \"bingo.html\".")
