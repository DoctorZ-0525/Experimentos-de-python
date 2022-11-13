#nombre = "Juian"
#apellido = "Almario"
#edad = 17
#mas = 1

#print(f"Mi nombre comppleto es {nombre} {apellido}") #aqui pinto mi nombre y lo uno con mi apellido
#print(f"mi edad es {edad+mas} a") #aqui pondo mi edad pero solo con las variables seleccionadas

#tambien podria hacer esto para que sea mas general insertando los valores y luego pintarlos como aqui:

#ingreso valores
#nombre = input("Ingresa tu primer nombre: ")
#apellido = input("ingresa tu primer apellido: ")

#pinto el resultado de forma ordenada con (f) para entender mejor el codigo
#print(f"Tu nombre completo es: {nombre} {apellido}")


#bolleanos this simple
#<
#>
#==
#>=<
#!=
#y = 30 <= 20

#print(y)

#################################################################################################

#ENUMERATOR

lista = ["a","b","c","d","e"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

#el eunumerador se puede hacer de una forma mas elegante

lista1 = ["a","b","c","d","e"]

for indice,item in enumerate(lista1):
    print(indice,item)