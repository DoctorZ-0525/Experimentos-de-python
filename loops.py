#loops utilizacion del for
#VAR que necesito
print("CODIGO #1")
list_nombres = ["julian","andrea","camila","camilo"]

letra = input("letra del nombre que deseas buscar: ") #input (ingreso la informacon que busco)

for nom in list_nombres: #por cada nombre en la lista en la lista de nombres
    if nom.startswith(letra): #si comienza con /alguna letra
        print(nom) #pintar el nombre que corresponde a la letra de inicio
    else: #si no comienza por ninguna letra
        print(f"No comienza con la {letra}") #pinto los nombres en la lista que no empiezen con la letra requerida

#for nombre in list_nombres:
   # num_nombre = list_nombres.index(nombre) + 1
    #print(f"Hola nombre {num_nombre}: {nombre}") 
print("\n")
#DESMEMBREDOR DE TEXTO
print("CODIGO #2")
palabra = input("ingresa la palabra que deceas desarmar: ") #ingreso mi texto (no tengo que transformarlo porque sigue siendo un string)

for letra in palabra: #por cada letra que alla en palabra, imprimire la letra que corresponde
    print(letra)