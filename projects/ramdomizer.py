#project 2
#ramdomizer

#CONDICIONES A CUMPLIR
# 1- Preguntar en nombre del usuario
# 2- Decir "tengo un numero del 1 al 100 guardado cual crees que es?"
# 3- El jujador tendra 8 intentos para este reto y por cada intento fallifo decir si esta cerca o no
# 4- decirle al jugador si acerto el numero y en cuantos intentos lo realizo, ademas se le dara que numero era
# 5- sino lo asierta decir que lo vuelva a intentar
# plus+ - decirle al jujador si desea continuar jugando

from random import *


usuario = input("Nombre del jugador: ")
aleatorio = randint(1,100)

#INGRESA EL PRIMER NUMERO

print("Tengo un numero del 1 al 100 cual crees que pueda ser.")
numero1 = int(input("primer numero: "))

if numero1 == aleatorio:
    print(f"Acertaste, te tomo 1 intento y el numero era {aleatorio}")
elif numero1 <= aleatorio:
    print("estas un poco por debajo")
elif numero1 >= aleatorio:
    print("estas un poco por encima")

#INGRESA EL SEGUNDO NUMERO

print("esto es una prueba")
