#adivinado de numeros
#librerias utilizadas

from random import *

intentos = 1
numero = 0

print("Para evitar tener errores porque obviamente este programa los tiene ya que es algo para experimentar, ingresa los valores tal cual como se indica en el input, att: el creador")

user = input("Como te podemos llamar?: ")
print("\n")

#cuantos intentos deseas tener
numintentos = int(input(f"{user} Cuanto intentos quieres tener?: "))
print("\n")

#numero que quiero elegir
num1 = int(input("Dame el numero menor: "))
print("\n")
num2 = int(input("Dame el numero mayor: "))
print("\n")

#aleatoriedad del numero
aleatorio = randint(num1, num2)

print(aleatorio)
#Dialogo del comienzo del juego
print(f"{user} has elegido un  numero entre el numero {num1} y {num2}, cual crees que pueda ser")

#inicio del loop de verificación del numero
while intentos <= numintentos:
    numero = int(input("Dame un numero: "))
    intentos += 1
    #loop que verifica si el numero es menor al indicado y lo pinta en consola
    if numero < aleatorio:
        print("estas un poco por debajo ")
        print("\n")
    #si no es menor se verifica si es mayor a el numero aleatoio
    elif numero > aleatorio:
        print("estas un poco por encima")
        print("\n")
    elif numero == aleatorio:
        print(f"correcto {user} has acertado en un total de {intentos - 1}")
        break

#como el numero de intentos es mayor al establecido se termina el juego
if intentos == numintentos:
    print(f"{user} has superado el total de {intentos} buena suerte la proxima")