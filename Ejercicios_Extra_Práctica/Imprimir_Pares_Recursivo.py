#Imprimir pares hasta N
#Escriba un algoritmo que reciba como entrada un número entero positivo N y que imprima todos los números
#pares desde 1 hasta N

def imprimirPares(numero):

    if(numero==0):
        return 0
    else:
        imprimirPares(numero - 1)
        if (numero % 2 == 0):
            print(numero)

#-----------------------------------------------------

def imprimirParesHastaNAux(numero):
    if(numero==0):
        return
    else:
        imprimirParesHastaNAux(numero-2)
        print(numero, end=" ")


def imprimirPares2(numero):

    numero-=numero%2
    imprimirParesHastaNAux(numero)


imprimirPares(15)