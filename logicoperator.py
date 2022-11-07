#frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#palabra1 = "éxito"
#mi_bool = palabra1 not in frase and palabra2 not in frase
#print(mi_bool)

#TOMA DE DECISIONES

comida = input("Que comida te gusta: ") #ingreso tipo de comida

if comida == "agua": #si lo que ingreso es agua "no es comida"
    print("eso no es comida")
elif comida == "pan": #pero si lo ingreso es pan "es comida"
    print("eso si es comida")
else: #sino es ninguna de las 2 es porque "no tienes comida"
    print("no tienes comida")

#EDADES 
edad = int(input("Que edad tienes: ")) #ingreso la edad- la transformo en numero(int)
calificacion = int(input("Cual es tu calificación: ")) #tambien ingreso un numero y lo transformo en int

if edad < 18: #verifico la edad
    print("eres menor de edad")
    if calificacion > 3: #verifico si paso la materia o no en 
        print("has aprobado la materia")
else: #si no es mayor de 18 años pinto que es "mayor de edad"
    print("eres mayor de edad")
    if calificacion > 3: #y si aprobo o no
        print("has aprobado")