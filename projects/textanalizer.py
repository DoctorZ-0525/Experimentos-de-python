#analizador de textos
#OBJETIVOS CON ESTE PROGRAMA
#Anadir un texto ya sea un parrafo o renglon
#TEXTO DE PRUEBA
#Para ser exitoso, es necesario motivarte a pesar de estar python experimentando uno de esos días en los que tirarías la toalla. La vida tiene sus momentos buenos y sus momentos malos, pero hay que seguir ahí, implacable, al pie del cañón intentando seguir luchando por aquello que nos hace felices


#analizar

# 1- Cuantas veces aparece cada letra * (esta parte me toco guiarme y entender el codigo de ejemplo)
# 2- Cuantas palabras hay en total *
# 3- mostrar las PRIMERA y ULTIMA palabra*
# 4- mostra el texto de forma inversa *
# 5- encontrar la palabra "python" *

texto = input("Ingresa aqui tu texto: ") #AÑADIENDO TEXTO 
textorem = texto.lower()
letras = [] #variables para almacenas letras
palabras = textorem.split() #VARIABLE PARA SEPARAR PALABRAS DESDE CADA ESPACIO
print("\n") #salto de linea 
print("QUE LETRAS DESEAS ENCONTRAR EN EL TEXTO: ") #Que letra deseo encontrar

#letras que deseo encontrar
letras.append(input("Ingresa la primera letra: ".lower())) #INDICE 1 # lo que hacemos aqui es almacenar la letra en la list 
letras.append(input("Ingresa la segunda letra: ".lower())) #INDICE 2
letras.append(input("Ingresa la tercera letra: ".lower())) #INDICE 3

#cantidad de letras en el texto
cantidad1 = textorem.count(letras[0])
cantidad2 = textorem.count(letras[1])
cantidad3 = textorem.count(letras[2])

#resultados
print("RESULTADOS:")
print(f"TU TEXTO TIENE '{len(textorem)}' CARACTERES") #visualizo cuantos caracteres tiene mi texto

print(f"TU TEXTO TIENE '{len(palabras)}' PALABRAS") #Busco cuantas palabras tiene el texto


#visualizo cuantas veces se repiten las palabras que estoy buscando
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad3} veces")

python = "python" in textorem #busco python en el texto
print("la palabra python en el texto es:", python) #pinto si esta o no estas

#letras de inicio y fin
print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = textorem[0]
letra_final = textorem[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n") #salto de linea 
print("SI TU TEXTO ESTUVIERA INVERTIDO SE VERIA ASI: ")
print(textorem[::-1]) #invertir texto (dislexia) XD