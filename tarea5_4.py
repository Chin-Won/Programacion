#Escribe un programa en Python para ordenar un diccionario dado por clave.

diccionario={
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

diccionarioOrdenadoAlfabetico=dict(sorted(diccionario.items()))
diccionarioOrdenadoNumerico=dict(sorted(diccionario.items(),key=lambda x:x[1], reverse=True))

print(diccionarioOrdenadoAlfabetico)
print(diccionarioOrdenadoNumerico)