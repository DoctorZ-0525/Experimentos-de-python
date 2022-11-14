#lo que hacemos aqui e convinar varias listas
<<<<<<< HEAD

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
=======
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinacion = zip(paises,capitales)

for pais,capital in combinacion:
    print(f"La capital de {pais} es {capital}")
>>>>>>> 429d9ed2c1257b47feb6ca55d7bafdac901ca2d0
