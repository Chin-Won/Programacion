#Eliminar una clave de un diccionario

numeros=dict(a=2,b=5,c=7,d=8)
print(f'Diccionario inicial: {numeros}')

def eliminar_claves(diccionario):
    
    valor_eliminar=input('Ingrese la clave deseada a eliminar: ')

    if valor_eliminar in diccionario:
        del numeros[valor_eliminar]
    else:
        print('La clave deseada a eliminar no se encuentra en el diccionario')
    
eliminar_claves(numeros)
print(f'Diccionario final: {numeros}')