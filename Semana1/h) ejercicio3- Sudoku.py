filas=9
columnas=9

def dibujarTablero(matriz):

    print("\tSUDOKU\t")

    for i in range(filas):

        if(i%3==0):print("------------------")

        for j in range(columnas):

            if(j==2 or j==5 or j==8):print(matriz[i][j], end='|')
            else:print(matriz[i][j],end=" ")
        print(" ")

def devolverTableroRellenado():
    matrizNueva=[]
    for i in range(filas):
        matrizNueva.append([])
        for j in range(columnas):
            valor=input("Fila {}, Columna {}: ".format(i+1,j+1))
            matrizNueva[i].append(valor)

    return matrizNueva

def revisarNumeroExistenteEnFila(matriz,numero,fila):

    contador=0
    for j in range(columnas):
        if(matriz[fila][j]==numero):
            contador+=1

    if(contador>1):
        return True
    else:
        return False

def revisarNumeroExistenteEnColumna(matriz,numero,columna):
    contador=0
    for i in range(filas):
        if(matriz[i][columna]==numero):
            contador+=1

    if(contador>1):
        return True
    else:
        return False


def revisarSudoku(matriz):

    for i in range(filas):
        for j in range(columnas):

            apareceEnFila=revisarNumeroExistenteEnFila(matriz,matriz[i][j],i)
            apareceEnColummna=revisarNumeroExistenteEnColumna(matriz,matriz[i][j],j)

            if(apareceEnFila or apareceEnColummna):
                return "Sudoku Incorrecto"
            else:
                pass

    return "Sudoku Correcto"


matrizEjemplo=devolverTableroRellenado()
dibujarTablero(matrizEjemplo)
print(revisarSudoku(matrizEjemplo))

#2 for anidados manisfetados como funciones dentro de 2 for anidados -> Orden Polinomico O(n^4)