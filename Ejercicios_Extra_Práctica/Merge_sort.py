
#Ordenamiento por mezcla

arregloEjemplo=[6,2,16,24,3,1,6,2,4,1,6,2,3,5,1]

parteIzquierda=arregloEjemplo[:len(arregloEjemplo)//2] #Esto toma parte izquierda
parteDerecha=arregloEjemplo[len(arregloEjemplo)//2:] #Esto toma parte derecha


def merge(arr,left_part,right_part):

    left_index = 0  # index del arreglo izquierdo
    right_index = 0  # index del arreglo derecho
    k = 0  # Indexador del arreglo merge

    while left_index < len(left_part) and right_index < len(right_part):

        if left_part[left_index] < right_part[right_index]:
            arr[k] = left_part[left_index]
            left_index += 1
            # k+=1
        else:
            arr[k] = right_part[right_index]
            right_index += 1
            # k+=1

        k += 1

    while left_index < len(left_part):
        arr[k] = left_part[left_index]
        left_index += 1
        k += 1

    while right_index < len(right_part):
        arr[k] = right_part[right_index]
        right_index += 1
        k += 1



def mergeSort(arr):

    if len(arr)>1:

        left_part= arr[:len(arr)//2]
        right_part= arr[len(arr)//2:]

        #parte recursiva
        mergeSort(left_part)
        mergeSort(right_part)

        merge(arr,left_part,right_part)

        #merge
        #left_index=0 # index del arreglo izquierdo
        #right_index=0# index del arreglo derecho
        #k=0 #Indexador del arreglo merge
#
        #while left_index<len(left_part) and right_index<len(right_part):
#
        #    if left_part[left_index]<right_part[right_index]:
        #        arr[k]=left_part[left_index]
        #        left_index+=1
        #        #k+=1
        #    else:
        #        arr[k]=right_part[right_index]
        #        right_index+=1
        #        #k+=1
#
        #    k+=1
#
        #while left_index < len(left_part):
        #    arr[k]=left_part[left_index]
        #    left_index+=1
        #    k+=1
#
        #while right_index<len(right_part):
        #    arr[k]=right_part[right_index]
        #    right_index+=1
        #    k+=1
#


mergeSort(arregloEjemplo)
print(arregloEjemplo)
