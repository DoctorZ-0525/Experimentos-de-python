#SI QUIERES EJECUTAR EL CODIGO DE FORMA CORRECTA PUEDES COMENTAR EL CODIGO QUE NO NECESITAS O SIMPLEMETEN CORTAR EL CODIGO QUE NO NECESITAS Y EJECUTARLO :) 

#Verificador de tamaño de numero
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es menor que {num1}")
else:
    print(f"{num1} y {num2} son igualez")


#VERIFCAR SI PUEDO CONDUCIR
edad = int(input("Que edad tienes: "))
tiene_licencia = input("Tienes licencia: ").lower()

if edad < 18:
    print("Debes tener 18 años, pero si eres menor de edad debes contrar con permiso de tus padres")
    if tiene_licencia == "si":
        print("Si puedes conducir pero eres menor de edad")
    elif tiene_licencia == "no":
        print("No puedes conducir. Necesitas contar con 18 años y una licencia")
elif edad >= 18:
    print("Puedes conducir")
    if tiene_licencia == "si":
        print("puedes conducir")
    elif tiene_licencia == "no":
        print("No puedes conducir. Necesitas contar con una licencia")