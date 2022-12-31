#entendiendo la logica de los condicionales :)
name = input("Cual es tu primer nombre: ")
apellido = input("cual es tu apellido: ")
age = input("cuantos años tienes: ")


if name == "julian":
    print("nombre correcto")
else:
    print("no puedes seguir")

if apellido == "almario":
    print("apellido correcto")
else:
    print("no puedes ingresar")

if age == "18":
    print("ACCESO CONCEDIDO")
else:
    print("ACCESO DENEGADO")
