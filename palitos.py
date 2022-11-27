#Quien es el rey con palitos

#ingresamos la lista de palitos
palitos = ["-","--","---","----"]

#mezclamos los palitos
def mezclar(lista):
    shuffle(lista)
    return lista


#intentos y comprobamos que el valor sea igual al que se le pide al usuario
def prueba_suerte():
    intentos = ""

    while intentos not in ["1","2","3","4"]:
        intentos = input("ELige un numero del 1 al 4: ")
    return int(intentos)

#comprobamos los intentos

def 
