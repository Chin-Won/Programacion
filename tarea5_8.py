#Escribe un programa en Python para verificar si un diccionario está vacío o no.

def vacio(diccionario):
    if diccionario:
        print('No está vacío')
    else:
        print('Está vacío')
        
dicVacio={}
dicNoVacio={'a':5}

vacio(dicVacio)
vacio(dicNoVacio)