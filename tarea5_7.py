#Escribe un programa en Python para eliminar duplicados del diccionario.
diccionario=dict(a=1,b=10,c=100,d=200,g=0,e=5,f=60,t=100,z=10)

def eliminar(diccionario):
    diccionarioNoDup={}
    for key,value in diccionario.items():
        if value not in diccionarioNoDup.values():
            diccionarioNoDup[key]=value
    
    return diccionarioNoDup

diccionarioNoDup=eliminar(diccionario)

print(diccionarioNoDup)