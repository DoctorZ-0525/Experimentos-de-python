#loops utilizacion del for
#VAR que necesito
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