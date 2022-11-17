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

intentos = 0
numero = 0
usuario = input("Nombre del jugador: ")
aleatorio = randint(1,100)


print("Tengo un numero del 1 al 100 cual crees que pueda ser.")

while intentos < 8:
    numero = int(input("Dame un numero: "))
    intentos += 1

    if numero > aleatorio:
        print("estas un poco por arriba")

    elif numero < aleatorio:
        print("estas un poco por debajo")

    else:
        print(f"{usuario} has acertardo con un total de {intentos}")
        break
    
if intentos ==  8:
    print(f"{usuario} ya llegaste a los {intentos} intentos")
