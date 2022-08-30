#De cuantas maneras se pueden sentar 3 personas en 3 sillas? Con backtracking

contador=0

def back(nivelDelArbol,NumeroDePersonasYSillas,pila,cola):

    if(nivelDelArbol==NumeroDePersonasYSillas):
        global contador
        contador+=1
        print(f"{contador}. {pila}")
    else:
        for j in range(nivelDelArbol,NumeroDePersonasYSillas,1):
            pila.append(cola.pop(0))

            back(nivelDelArbol+1,NumeroDePersonasYSillas,pila,cola)

            cola.append(pila.pop())


colaEjemplo=[]
colaEjemplo.append("naranja")
colaEjemplo.append("negro")
colaEjemplo.append("rojo")
#colaEjemplo.append("m")
pilaEjemplo=[]

i=0

back(i,len(colaEjemplo),pilaEjemplo,colaEjemplo)
