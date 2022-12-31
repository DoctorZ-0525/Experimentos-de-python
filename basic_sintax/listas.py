
#VARIABLES QUE UTILIZO
lista1 = [1,2,4,"hola","como estas", 1.5] #la slistas en python pueden tener cualquier tipo de dato
lista2 = [1.6, 1.7, 1.8]
lista3 = lista1 + lista2 #las listas tambien se pueden unir en una variable


#las listas tambien se pueden indexar:
resultado = lista1[1:] #se puede pintar cualquier tipo de dato cuando se pida


lista1.append(1.6) #a diferencia de los strings, en las listas tambien se puede agregar datos
eliminar = lista1.pop() #con este metodo elimianmos elementos de las listas

#las listas tambien se pueden unir como por ejemplo:
#creo una nueva lista

print(lista1 + lista2)
print(resultado)
print(lista1)
print(type(lista1))
print(eliminar)