#funciones en python, en fin es raro pero nada mas es para aprender
#

def saludar(nombre): #al parecer en las funciones en el contenid de estas tambien se puede ingresar un valor puesto por el usuario
    print("hola " + nombre)

saludar(input("cual es tu nombre: ")) #llamo a la funcion y ingreso un valor el cual va a tomar la variable "nombre" que esta dentro de la funcion previamente definica

def multiplicar(numero1,numero2):
    multi = numero1 * numero2
    return multi

resultado = multiplicar(int(input("PRIMER NUMERO: ")),int(input("SEGUNDO NUMERO: ")))

print(resultado)

palabra = input("cual es tu nombre: ")

def invertir_palabra(palabra):
    
    palabra1 = palabra[::-1]
    palabra1 = palabra.upper()
    
    return palabra1
