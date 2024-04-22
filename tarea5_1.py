#Multiplicar los elementos de un diccionario

diccionario={
"a":4,
"b":9,
"c":3,
"d":11
}
resultado=1
for numero in diccionario.values():
    resultado*=numero

print(resultado)
