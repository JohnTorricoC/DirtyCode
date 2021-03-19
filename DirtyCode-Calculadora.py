def calculadora(r):
    n2=int(input("Digito 2: "))
    if r == 's':
        res=n1+n2
        print("Resultado de la operacion obtenido! ====> ")
        return print(res)
    elif r == 'r' :
        res=n1-n2
        print("Resultado de la operacion obtenido! ====> ")
        return print(res)
    elif r == 'm' :
        res=n1*n2
        print("Resultado de la operacion obtenido! ====> ")
        return print(res)
    elif r == 'd' :
        res=n1/n2
        print("Resultado de la operacion obtenido! ====> ")
        return print(res)

   
r= input("Operacion: ")
n1=int(input("Digito 1: "))
calculadora(r)