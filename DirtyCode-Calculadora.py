def extraerDatos(expresion):
    return int(expresion[0]), int(expresion[2]), str(expresion[1])
def calculadora(nro1,nro2,operador):
    resultado = nro1
    if operador =='+':
        resultado+=nro2
    elif operador == '-':
        resultado-=nro2
    elif operador == '*':
        resultado*=nro2
    elif operador == '/':
        resultado/=nro2
    else:
        print("")
        resultado=None
    return resultado    
print("Ingrese su Operacion:")
operacion=input().split()
Nro1,Nro2,operador=extraerDatos(operacion)
print(f"El resultado es: {calculadora(Nro1,Nro2,operador)}")
