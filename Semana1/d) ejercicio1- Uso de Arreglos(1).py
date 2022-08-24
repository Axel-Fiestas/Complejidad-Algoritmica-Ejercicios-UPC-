#Escriba un método int minArreglo(int[] t) que devuelve el elemento más pequeño de un arreglo.

numeros=[6,10,3,8,10,8,2]

def minArreglo(lista):

    numeroMenor=lista[0]

    for numero in lista:

        if(numeroMenor>=numero):
            numeroMenor=numero

    return numeroMenor


print(minArreglo(numeros))

#1 Ciclo For involucrado por tanto: Complejidad O(n)
