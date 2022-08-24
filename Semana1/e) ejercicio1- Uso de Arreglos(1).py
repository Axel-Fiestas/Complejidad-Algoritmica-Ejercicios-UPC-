#Escriba un método int mediaArreglo(int[] t) que devuelve la media aritmética de los elementos de un arreglo


numeros=[14,16,12,12,10,18,20,14]

def mediaArreglo(lista):

    tamanioLista=len(lista)
    suma=0

    for elemento in lista:
        suma+=elemento

    media=suma/tamanioLista

    return media

print(mediaArreglo(numeros))

#1 Ciclo For involucrado por tanto: Complejidad O(n)
