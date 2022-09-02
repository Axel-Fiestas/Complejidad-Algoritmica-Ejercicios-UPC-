#Dado un texto t de n líneas, implementar un algoritmo “divide y vencerás” que cuente el número de palabras
#que contiene dicho texto

contador=0
listaCaracteresEspeciales=[" ",",","."]

textoAnalizar="Hey como estan señores. Jaja que loco PERO MIRALO asdsa asdsa vxzvcs efwq feqwr"

def merge(textoArray,left_part,right_part):

    global contador
    i=0
    j=0

    #VENCE
    while i<len(left_part) and j<len(right_part):

        if(left_part[i] not in listaCaracteresEspeciales):
            i+=1
            contador+=1

        if(right_part[j]not in listaCaracteresEspeciales):
            j+=1
            contador+=1

    while i<len(left_part):

        if(left_part[i]not in listaCaracteresEspeciales):
            i += 1
            contador += 1

    while j<len(right_part):

        if(right_part[j]not in listaCaracteresEspeciales):
            j += 1
            contador += 1

def contarPalabras(texto):

    textoArray=texto.split()

    #DIVIDE
    left_part=textoArray[:len(textoArray)//2]
    right_part=textoArray[len(textoArray)//2:]


    #CONQUISTA
    merge(textoArray,left_part,right_part)


contarPalabras(textoAnalizar)
print(contador)