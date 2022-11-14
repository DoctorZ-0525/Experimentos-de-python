#lo que hacemos aqui e convinar varias listas

#creamos 2 listas diferentes

#VAR UTILIZADAS

nombres = ["julian", "andres", "valeria"]
edades = [16,17,18]
ciudades = ["medellin", "cali", "bogota"]

combinados = list(zip(nombres,edades,ciudades))


#Basicamente lo que hacemos es formar un pequeño texto en el cual indiquemos
#que "por cada nombre,edad y ciudad" pintar esta informacion en un texto descriptivo

for nombres,edades,ciudades in combinados:
    print(f"{nombres} tiene {edades} y vive en {ciudades}")
