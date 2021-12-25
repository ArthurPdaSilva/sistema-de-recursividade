def tamanhoString(string):
    if(len(string) == 1):
        return 1
    else:
        return 1 + tamanhoString(string[1:])

def somarStringInt(string):
    if(len(string) == 1):
        return int(string)
    else:
        return int(string[0]) + somarStringInt(string[1:])

def letraString(palavra, letra):
    if(len(palavra) == 1):
        if(palavra == letra):
            return 1
        else:
            return 0
    else:
        if(palavra[0] == letra):
            return 1 + letraString(palavra[1:], letra)
        else:
            return 0 + letraString(palavra[1:], letra)

def multi(n1, n2):
    if(n2 == 1):
        return n1
    else:
        return n1 + multi(n1, n2-1)

def expo(n1, n2):
    if(n2 == 1):
        return n1
    else:
        return n1 * expo(n1, n2-1)

def listaMulti(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        return lista[0] * listaMulti(lista[1:])
    
def listaSoma(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        return lista[0] + listaMulti(lista[1:])

def maiorV(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        if(lista[0] > maiorV(lista[1:])):
            maior = lista[0]
        else:
            return maiorV(lista[1:])
        return maior

def menorV(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        if(lista[0] < menorV(lista[1:])):
            menor = lista[0]
        else:
            return menorV(lista[1:])
        return menor

def binarioValor(n1):
    if(n1 <= 1):
        return n1
    else:
        return (n1 % 2) + 10 * binarioValor(n1 // 2)

def decimalValor(n1):
    if(len(n1) == 1):
        return int(n1[0]) * 2 ** (len(n1) - 1)
    else:
        return int(n1[0]) * 2 ** (len(n1) - 1) + decimalValor(n1[1:])

def fibo(termo):
    if(termo <= 1):
        return termo
    else:
        return fibo(termo - 1) + fibo(termo - 2)

