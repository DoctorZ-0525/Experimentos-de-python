def lista(num1,num2,*args,**kwargs):

    print(f"el primer numero es {num1}")
    print(f"el segundo numero es {num2}")

    for arg in args:
        print(f"arg = {arg}")



    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [200,555,342,5113,326,6324]
kwargs = {'x':'uno','y':'dos','z':'tres'}

lista(20,40,*args,**kwargs)
