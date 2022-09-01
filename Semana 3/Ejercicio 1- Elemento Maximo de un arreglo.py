import random
#Escriba un algoritmo "simple" para calcular este problema
#Escriba un algoritmo "divide y vencerás" para calcular este problema


arregloEjemplo= [random.randint(1,20) for _ in range(10)]



def maxSimple(arreglo):

    numeroMayor=arreglo[0]

    for numero in arreglo:

        if numeroMayor<=numero:
            numeroMayor=numero


    return numeroMayor


def maxDivideYVenceras(arr,left,right):

    if(left==right):
        return arr[left]

    mid=(left+right)//2
    maxLeft=maxDivideYVenceras(arr,left,mid)
    maxRight=maxDivideYVenceras(arr,mid+1,right)

    if(maxLeft>=maxRight):
        return maxLeft
    else:
        if(maxRight>=maxLeft):
            return maxRight


print(arregloEjemplo)
print(maxDivideYVenceras(arregloEjemplo,0,len(arregloEjemplo)-1))
