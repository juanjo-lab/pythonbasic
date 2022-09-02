## training exercises
#Juan Jose martinez camara
## A. Basics (4 ptos) ----------------------------------------------------------------
# 1. Imprime por pantalla todas las potencias de dos menores o iguales que 2048, utilizando un bucle while

i=0
n=0
while i < 2048:
    i=2**n
    print(2**n)
    n=n+1
print()


# 2. Imprime por pantalla las primeras 15 potencias de dos 

[2**i for i in range(15)]

# 3. A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista que contiene aquellos valores de la primera que tambien estan en la 
# segunda e imprimela por pantalla. Es decir, calcula la interseccion de ambas listas. 

numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94, 95]
for i in range(len(numeros1)):
    for j in range(len(numeros2)):
        if numeros1[i]==numeros2[j]:
            n=numeros1[i]
            print(n) 
        
# 4. Recibe una lista de enteros y calcula la media aritmetica 

a=0
enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 98, 100]
a=sum(enteros)/len(enteros)  
print(a)

# 5. Imprime por pantalla la secuencia [0, 2, 4, ... 200] 

[i+2 for i in range(199)]

# 6. Imprime por pantalla la secuencia [86, 84, 82, ... 14]

a=86
[a-2 for i in range(86,14,-2)]

# 7. Implemente una funcion que recibe una lista de enteros y devuelve otra lista con aquellos que son pares y >= 113 [Solucion]

enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 116, 114]
list(enteros)
def list(numeros):
    numerospar=[]
    for i in range(len(numeros)):
        if numeros[i] >113 and numeros[i]%2==0:
            numerospar.append(numeros[i])
    return numerospar

# 8. Implemente una funcion que calcula el factorial de un numero

a=int(input("introduce el valor que desea= "))
def factorial(a):
    c=a
    b=1
    for x in range(c):
            b=a*b
            a=a-1
            print("el factorial de "+str(c)+"es"+str(b))
    return b

## B. Numpy (4 ptos) -------------------------------------------------------------------

import numpy as np

# 1. Crear un vector con valores dentro del rango 10 a 49

Z=np.arange(10,49)

# 2. Crear una matriz 3x3 con valores de 0 a 8

tabla=np.empty((3,3))
for i in range(3):
    for j in range(3):
        tabla[i,j]=i*3+j

# 3. Encontrar los indices que no son ceros del array [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0].

indices=[1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
for i in range(len(indices)):
    if indices[i]!=0:
        print("los indices  que no son cero del array son :"+str(i))
# 4. Crear una matriz de 5x5 con valores en las filas que vayan de 0 a 4.

tabla_2=np.empty((5,5))
for i in range(5):
    for j in range(5):
        tabla_2[i,j]=j

# 5. Cree un array cuyos elementos sean los enteros pares en [1,100] y en orden decreciente.

import numpy as np
Z=np.arange(100,1,-2)

# 6. Cree un array con 10 elementos en [-2,2] y equidistantes entre ellos. 

Z=np.linspace(-2,2)

# 7. Ordene el array dado por los elementos (0, 1, 15, 8, 9, 17) de menor a mayor.

Z=[0, 1, 15, 8, 9, 17]
Z.sort()

# 8. Simule el lanzamiento de un dado de 6 caras 100 veces. Devuelva el numero de veces que sale cada cara. 

A = np.random.randint(1, 6, 100)
num1,num2,num3,num4,num5,num6=0,0,0,0,0,0
for i in range(len(A)):
    if A[i]==1:
        num1=num1+1
    elif A[i]==2:
            num2=num2+1
    elif A[i]==3:
                num3=num3+1
    elif A[i]==4:
                    num4=num4+1
    elif A[i]==5:
                        num5=num5+1
    elif A[i]==6:
                            num6=num6+1


## C. Matplotlib (2 ptos)---------------------------------------------------------------

import math
import matplotlib.pyplot as plt

# 1. Realice una gráfica de la función coseno para 100 valores de ángulo entre [-pi, pi]. Muéstrelo por pantalla. 
x= np.linspace(-math.pi,math.pi,100)
y= np.cos(x)
plt.figure()
plt.plot(x,y)
plt.show()

# 2. Grafique la función y = x^2 + 2 para 50 valores de x en [-1, 1]. Muéstrelo por pantalla. 
x=np.linspace(-1,1,50)
y=x**2+2
plt.figure()
plt.plot(x,y)
plt.show()


