#VARIABLES QUE UTILIZO
texto = "hola como estas"
a = "hola"
b = "como"
c = "estas"
d = "tu?"

#reemplazar partes de un texto:
resultado = texto.replace("a","c")

print(resultado)#visualizo el remplazo en el texto
print(len(texto))#visualizo cuantos datos tiene mi variable

e = " ".join([a,b,c,d]) #uno las variables separadas y creo na nueva variable con un texto

print(e)