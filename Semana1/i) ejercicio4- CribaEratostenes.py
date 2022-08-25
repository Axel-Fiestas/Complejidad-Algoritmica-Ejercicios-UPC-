
def generarLista(n):
    lista=[]
    for i in range(2,n):
        lista.append(i)

    return lista

def suprimirPares(lista):
    listaAuxiliar = []

    for numero in lista:
        if (numero%2==0 and numero!=2):
            pass
        else:
            listaAuxiliar.append(numero)
    lista = listaAuxiliar
    return lista


def esMultiplo(numeroRecibido,multiplo):

    numeroAuxiliar=multiplo

    for i in range(numeroRecibido):

        if(numeroAuxiliar>numeroRecibido):
            return False
        else:
            pass

        numeroAuxiliar=multiplo*i

        if(numeroRecibido==numeroAuxiliar):
            return True
        else:
            pass


def suprimirMultiplos(lista,multiplo):

    listaAuxiliar=[]

    for numero in lista:
        if(esMultiplo(numero,multiplo) and numero!=multiplo):
            pass
        else:
            listaAuxiliar.append(numero)

    lista=listaAuxiliar

    return lista


def verificar(numeroPequeno,numeroGrande):

    numeroPequenoAlCuadrado=numeroPequeno*numeroPequeno

    if(numeroPequenoAlCuadrado>numeroGrande):
        return True
    else:
        return False


def cribaEratostenes(n):

    listaEratostenes=generarLista(n)
    listaEratostenes=suprimirPares(listaEratostenes)
    tamanioLista=len(listaEratostenes)

    listaAux=[]

    for i in range(tamanioLista):
        if(verificar(listaEratostenes[i+1],listaEratostenes[tamanioLista-1])):
            break
        listaAux=suprimirMultiplos(listaEratostenes,listaEratostenes[i+1])

    return listaAux

#No me salió F :,v

print(cribaEratostenes(30))





