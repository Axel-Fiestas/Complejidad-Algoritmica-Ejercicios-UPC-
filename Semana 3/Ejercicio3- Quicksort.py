# Implementar el algoritmo Quicksort

arrayExample = [5, 2, 6, 1, 4,4,4]


def swap(arr,left, right):

    aux = arr[left]
    arr[left] = arr[right]
    arr[right]=aux


def partition(arr,left,right):

    pivot=arr[left]
    indexI=left+1
    indexD=right

    while True:

        while indexI<= indexD and arr[indexI]<=pivot:
            indexI+=1

        while indexI<= indexD and arr[indexD]>=pivot:
            indexD-=1

        if indexD<indexI:
            break
        else:
            swap(arr,indexI,indexD)
            #arr[indexI],arr[indexD]=arr[indexD],arr[indexI] #SWAP

    #UNA VEZ TERMINADO SE INTERCAMBIA EL PIVOTE POR EL ELEMENTO QUE SE ENCUENTRA EN LA POSICIÓN INDEXD
    swap(arr,left,indexD)
    #arr[left],arr[indexD]=arr[indexD],arr[left]

    return indexD


def quicksort(arr, left, right):

    if left < right:

        indexPivot = partition(arr, left, right)
        quicksort(arr, left, indexPivot- 1)
        quicksort(arr, indexPivot+1, right)



quicksort(arrayExample, 0, len(arrayExample) - 1)
print(arrayExample)
