#verificar si la persona es acta para conducir
#pero pudiendo reutilizar el codigo de forma mas eficiente

print("Bienvenido a el analizador de edades para conducir")
print("\n")

user = input("nos puedes decir cual es tu nombre: ")

print("\n")

print(f"bueno {user} para poder darte un resultado tenemos que tomar algunos datos para definir si puedes o no conducir")

edad = int(input(f"{user} cuantos años tienes: "))

if edad >= 18:

    gafas = input("utilizas gafas? ")
    if gafas == "si":
        carnet = input(f"{user} tienes cardet de conducir s/n: ")
        if carnet == "si":
            print(f"{user} reunes los requisitos para poder conducir")
        else:
            print(f"{user} debes hacer tu curso para poder conducir")
    else:
        print(f"{user} no puedes conducir")
        print("\n")
        print(f"{user} vuelve cuando utilices gafas")

else:
    print(f"{user} eres muy pequeño para conducir")
    print("vulve cuando seas un poco mas grande")