#Escriba un algoritmo que reciba como entrada dos números enteros M y N, e imprima
#la secuencia de números impares que existen entre ambos números(incluyéndolos).
#El valor de M debe ser menor que el de N

def imprimir_impares(M,N):

    if(M==N):
        if (M % 2 != 0):
            print(M)
    else:
        if (M % 2 != 0):
            print(M, end=" ")
        M += 1
        imprimir_impares(M,N)


imprimir_impares(5,100)