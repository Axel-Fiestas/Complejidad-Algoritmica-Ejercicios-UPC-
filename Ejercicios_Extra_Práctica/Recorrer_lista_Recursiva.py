#Recorrer una lista de forma recursiva

listaEjemplo=[0,1,2,3,4,5]


def recorrer(lista,indice):

    if(indice<len(lista)):
        print(lista[indice])
        recorrer(lista, indice+1)

recorrer(listaEjemplo,0)