#Sacar la suma de 1 al numero  dado. Si nos dan el 5, devolverá un 5+4+3+2+1=15


def sumaRec(numero):

    if(numero==1):
        return 1
    else:
        return numero+sumaRec(numero-1)


print(sumaRec(5))