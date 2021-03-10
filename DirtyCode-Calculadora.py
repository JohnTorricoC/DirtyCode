def calculadora(r):
    
    n1=int(input("Digito 1: "))
    n2=int(input("Digito 2: "))
    if r == 's':
        res=n1+n2
    elif r == 'r' :
        res=n1-n2
    elif r == 'm' :
        res=n1*n2
    elif r == 'd' :
        res=n1/n2
    return res

r= input("Operacion: ")
print(calculadora(r))