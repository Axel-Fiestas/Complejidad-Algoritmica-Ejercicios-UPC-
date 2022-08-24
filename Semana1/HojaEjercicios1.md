Hoja de Ejercicios 1          ![](Aspose.Words.dd84e5eb-66a9-44fc-aa96-5f27d44ed7ad.001.png)Complejidad Algorítmica - UPC![](Aspose.Words.dd84e5eb-66a9-44fc-aa96-5f27d44ed7ad.002.png)

**Ejercicio 1:**  Uso de arreglos (1) 

- Escriba un método generar(n) que genere un arreglo de tamaño n con todos sus elementos aleatorios entre 1 y 100. 
- Escriba un método mostrar(int[] t) que muestra todos los elementos  de un arreglo t. 
- Escriba un método reversa(int[] t) que invierte  el orden  de todos los elementos  de un arreglo t (sin crear arreglos auxiliares), 
- Escriba un método int minArreglo(int[] t) que devuelve el elemento más pequeño de un arreglo. 
- Escriba un método int mediaArreglo(int[] t) que devuelve la media aritmética de los elementos de un arreglo. 
- Escriba un método int[] ocurrencias(int[] t) que devuelve un nuevo arreglo s tal que s[i] es el número  de veces que el entero  i aparece  en t. 

¿Cuál es la complejidad de todos estos métodos? 

**Ejercicio 2:**  Uso de arreglos (2) 

- Cree un arreglo de 100 enteros. 
- Inicialice el arreglo de forma que la casilla i contenga el entero i. 
- Muestre el arreglo. 
- Analice la complejidad de este algoritmo. 

**Ejercicio 3:** Sudoku

Escriba un programa que pide al usuario de entrar una grilla de  sudoku1  completamente llena y verifique que esta grilla es correcta.

¿Cuál es la complejidad de este método? 

**Ejercicio 4:** Criba de Eratóstenes 

La  criba de  Eratóstenes2  es  un  algoritmo que  permite   hallar  todos  los  números  primos menores  que un número  natural dado  N.

El algoritmo  procede por eliminación: se trata de suprimir de un arreglo todos los múltiplos de los enteros de  2 a  N.  Comenzamos con  los múltiplos de  2, luego  cada vez tachamos los múltiplos del entero más pequeño restante hasta que el cuadrado de este sea mayor que el entero más grande en  la  lista.  Podemos detenernos  cuando el  cuadrado del  número entero más  pequeño es  más pequeño que  el entero más  grande, porque  en este  caso,  si hubiera no primos, ya  habrían sido rayados. 

Al final del proceso, todos  los enteros que no se han  rayado son números primos menores que N. Implemente la función int numeros\_primos(int n) que cuenta  el número  de números  primos menores que n usando  la criba de Eratóstenes. 

Analice la complejidad de este algoritmo. ![](Aspose.Words.dd84e5eb-66a9-44fc-aa96-5f27d44ed7ad.003.png)

1 https://es.wikipedia.org/wiki/Sudoku

2 https://es.wikipedia.org/wiki/Criba\_de\_Erat\’ostenes 

1
