#Cree un arreglo de 100 enteros.
#Inicialice el arreglo de forma que la casilla i contenga el entero i.
#Muestre el arreglo.
#Analice la complejidad de este algoritmo.

def crearLista():
    lista=[]
    for i in range(101):
        lista.append(i)

    return lista

def mostrarLista(lista):
    print(lista)


listaNumeros=crearLista()
mostrarLista(listaNumeros)

#1 Ciclo For involucrado por tanto: Complejidad O(n)
