from random import *

aleatoria = randint(1, 100)

if aleatoria <= 50:
    print("True")
elif aleatoria >= 50:
    print("false")

#selector de nombres

nombres = list(input("Dime los nombres implicados separados por espacios: "))

resultado = choice(nombres)

print(resultado)
