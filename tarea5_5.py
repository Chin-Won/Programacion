#Valores máximo y mínimo de un diccionario.

diccionario=dict(a=1,b=10,c=100,d=200,g=0,e=5,f=60)

def buscarValores(diccionario):
    valores=diccionario.values()
    maximo=0
    minimo=0
    for values in valores:
        if values>=maximo:
            maximo=values
        elif values<=minimo:
            minimo=values
    maxMin=(maximo,minimo)        
    return maxMin

maximoMinimo=buscarValores(diccionario)

print(maximoMinimo)