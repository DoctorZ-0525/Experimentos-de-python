import random

def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)

def evaluar_jujador(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <=6:
        return f"La suma de tus dados es {suma_dados} Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}, tienes buena chanse"
    else:
        return f"La suma de tus dados{suma_dados} es la suma ganadora"
