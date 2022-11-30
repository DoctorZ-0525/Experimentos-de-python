def devolver_distintos(a,b,c):

    sumar = a+b+c
    lista = [a,b,c]

    if sumar > 15:
        return max(lista)
    elif suma <10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(19,15,1))
