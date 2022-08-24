import random


#Escriba un método generar(n) que genere un arreglo de tamaño n con todos sus elementos
#aleatorios entre 1 y 100.


def generar(n):
    lista=[]
    for elemento in range(0,n):
        elemento=random.randint(1, 101)
        lista.append(elemento)

    return lista


print(generar(5))

#1 Ciclo For involucrado por tanto: Complejidad O(n)