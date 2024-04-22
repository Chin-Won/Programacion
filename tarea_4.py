#Hacer un diccionario con el nombre de 10 alumnos de preparatoria con las calificaciones

Calificaciones={
    "Max":8,
    "Noe":9,
    "Alonso":7,
    "Ruth":8,
    "Vanessa":9,
    "Luz":10,
    "Emiliano":9,
    "Fernando":6,
    "Keylany":9,
    "Gali":6

}

alumno=(input("Escriba el nombre del alumno:"))
lista=Calificaciones.keys()

for i in lista:
    if alumno==Calificaciones[i]:
        print(Calificaciones[i])