#este tipo de loops se repite mientraas se cumpla una condicion

#determinandes de loops: pass, continue, break

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == ("a"):
        break
    print(letra)

#INTERRUCTOR DE FLUJO
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero <= 0:
        break
    print(numero)

#DIVISIBILIDAD
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -=1
    else:
        numero -=1