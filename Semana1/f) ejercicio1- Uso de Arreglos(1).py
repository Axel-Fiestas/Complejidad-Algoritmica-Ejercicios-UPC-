#Escriba un método int[] ocurrencias(int[] t) que devuelve un nuevo arreglo s tal que s[i] es el
#número de veces que el entero i aparece en t.
import random

numeros=[0,7,7,1,2,3,1,1,1,1,1,1,10,10,10,10]

def apareceNumero(lista,numeroDado):
    contador=0
    for numero in lista:
        if(numeroDado==numero):
            contador+=1


    return contador


def ocurrencias(lista,numeroDado):

    i=apareceNumero(lista,numeroDado)
    listaNueva=[]

    for elemento in range(i):
        listaNueva.append(numeroDado)


    return listaNueva


print(ocurrencias(numeros,10))

#1 Ciclo For involucrado por tanto: Complejidad O(n)