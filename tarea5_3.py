#Convertir dos listas en un diccionario.
l1=['a','b','c','d']
l2=[1,2,3,4,]

def dictForLists(keys,values):
    diccionario={}
 
    for i in range(len(keys)):
            diccionario[keys[i]]=values[i]
       
    return diccionario

diccionarioListas=dictForLists(l1,l2)

print(diccionarioListas)