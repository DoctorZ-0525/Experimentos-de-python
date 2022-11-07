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
print("QUE PALABRA DESEAS ENCONTRAR EN EL TEXTO: ") #Que deseo encontrar
letras = []
#VAR de palabra que deceo encontrar
letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))
#cantidad de letras en el texto
cantidad1 = textorem.count(letras[0])
cantidad2 = textorem.count(letras[1])
cantidad3 = textorem.count(letras[2])


#resultados
print("TU TEXTO TIENE",len(textorem),"LETRAS") #visualizo cuantos caracteres tiene mi texto
#visualizo cuantas veces se repiten las palabras que estoy buscando
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad3} veces")

python = "python" in textorem #busco python en el texto
print("la palabra python en el texto es:", python) #pinto si esta o no estas

#letras de inicio y fin
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = textorem[0]
letra_final = textorem[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("SI TU TEXTO ESTUVIERA INVERTIDO SE VERIA ASI")
print(textorem[::-1]) #invertir texto (dislexia) XD