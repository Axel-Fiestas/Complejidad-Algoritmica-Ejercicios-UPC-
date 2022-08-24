#Escriba un método reversa(int[] t) que invierte el orden de todos los elementos de un arreglo t
#(sin crear arreglos auxiliares)

frutas=["pera","manzana","platano","fresa","mango"]
numeros=[1,2,3]

def invetir(lista):

    tamanioLista=len(lista)

    for i in range(tamanioLista):

        if(i>=tamanioLista/2):
            break
        else:
            primerElemento=lista[i]
            ultimoElemento=lista[tamanioLista-1-i]

            lista[i]=ultimoElemento
            lista[tamanioLista-i-1]=primerElemento

    return lista

print(invetir(frutas))

#1 Ciclo For involucrado por tanto: Complejidad O(n)