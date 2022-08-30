
arreglo=[6,2,4,1,7,10,5]

def bubble_sort(arreglo):

    for i in range(len(arreglo)):
        for j in range(len(arreglo)):

            if(arreglo[i]<arreglo[j]):
                aux=arreglo[i]
                arreglo[i]=arreglo[j]
                arreglo[j]=aux


    return arreglo

print(bubble_sort(arreglo))

