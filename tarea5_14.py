# Escribe un programa en Python para acceder al elemento de la clave de un 
# diccionario por índice. Salida esperada: física matemáticas química

diccionario = {'fisica': 85, 'matematicas': 90, 'calculo':20,'quimica': 88}

indices=[0,1,3]

def diccionrioIndice(diccionario,indices):
    lista=list(diccionario.keys())
    resultado=[]
    for i in indices:
        for j in range(len(diccionario)):
            if i==j:
                resultado.append(lista[i])
                
    return resultado


print(diccionrioIndice(diccionario,indices))