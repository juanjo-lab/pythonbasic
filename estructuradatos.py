# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:35:05 2020

@author: Sr. Juan José
"""

import numpy as np
#                                                                                                       Basic Data Structures
#Create a function which takes a list of integers and prints whether the entry is positive, negative or zero.      EJERCICIO 1
#                                                                                                                       1                
items1  =  [ 1 ,  0 ,  -4 ,  3 ,  -7 ] 
a=len(items1)
for i in range(a):
    if items1[i]>0:
        print("positivo")
    elif items1[i] == 0:
        print("cero")
    elif items1[i]<0:
        print("negativo")
print()

#Modify this function so that instead of printing "positive", "negative" or 
#"zero", it returns the list of corresponding strings. (Can you make this more
# general? Instead of taking a number to the string "postive", "negative" or "zero",
# what if I want the squares of the numbers? Or each number incremented by one? 
#How would you allow for this?                                                                                          2
items1  =  [ 1 ,  0 ,  -4 ,  3 ,  -7 ] 
salir = False
opcion = 0
 
while not salir:
 
    print("1.-imprimir la cadena")
    print("2.-devolver el cuadrado de la cadena")
    print("3.-aumentar la cadena en 1")
    print("4.-disminuir la cadena en 1")
    print("5.-salir")
    opcion=int(input("introduzca que prefiere:"))
 
    if opcion == 1:
        for i in range(a):
            if items1[i]>>0:
                print(str(items1[i]) + "   positivo")
            elif items1[i] == 0:
                print(str(items1[i])+"    cero")
            elif items1[i]<<0:
                print(str(items1[i])+"   negativo")
                print()
    elif opcion == 2:
        print ("Opcion 2")
        for i in range(a):
                items1[i]=items1[i]**2
                print(str(items1[i]))
    elif opcion == 3:
        for i in range(a):
                items1[i]=items1[i]+1
                print(str(items1[i]))
    elif opcion ==4:
        for i in range(a):
                items1[i]=items1[i]-1
                print(str(items1[i]))
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Fin")


#Escribe una función que tome una lista de números y devuelva                       3
# la suma de los cubos de todos los elementos.
b=0
aa=[]
a=int(input(("Cuantos numeros desea introducir")))
for i in range(a):
    aa.insert(i,int(input("introduzca un numero numero")))
sum(aa)
print("el resultado es "+str(a))

#Write a function which finds the largest item in a list of numbers.                4

lista= [2,4,-1,9,10,3,20,6,2,9,9,2,3] 
a=0
for i in range(len(lista)):
    if lista[i]>a:
        a=lista[i]
print("el numero mas grande es"+str(a))

#Write a function which returns a list but in reverse order.                        5

lista= [2,4,-1,9,10,3,20,6,2,9,9,2,3] 
aux_lista=[]
a=len(lista)
for i in range(a):
    aux_lista.insert(i,lista[a-i])
    print(str(aux_lista[i]))


#                                                                               EJERCICIO2
#   Suppose that I'm playing a card game like poker. What are some possible 
#ways I could represent my current hand in the game                                 1

A = np.array([
    [1., 4., 2.],
    [5., 2., 1.],
    [6., 2., 1.],
    ])

x = np.array([1., 2., 3.])
np.dot(x, A)

                     

#Create a short list of friends' birthdays like we had above. Print a sorted        2 
#version of this list. Notice the way Python sorts these? Now, write a
# function which creates a new birthday list but with the order
# of the name and the birthday swapped. Print out a sorted
# version of this list. Notice the difference?
birthdays = [
    ('James', 'Aug 25'),
    ('Tommy', 'Sept 12'),
    ('Jason', 'Jun 13'),
    ('Lexi', 'Feb 1'),
]
sorted(birthdays)

#Create a list of the numbers 1 to 10. Create a new list                            3
# which consists of 
#the consecutive pairs of numbers in the list. For example,
# [(1, 2), (2, 3),(3, 4), ..., (9, 10)]
lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)]
lista3=[]
for i in range(len(lista1)):
    lista3.insert(i,(lista1[i],lista1[i+1]))
    
#Write a function which takes two tuples of (x1, y1) and (x2, y2) pairs and         4
#returns the "vector sum" (x1+x2, y1+y2). This suggests that we may try to
# implement an entire collection of support functions for vector algebra.
# Indeed, this kind of data abstraction is another crucial approach to 
# building programs!
x=0
y=0
a=0
b=0
for (x,y) in lista3:
    a=x+a
    b=y+b
lista4=[(a,b)]
#                                                                               EJERCICIO3
#Write a dictionary which translates an abbreviation for                        
#each day of the week to a corresponding day number. For example:                   1
week = {
    '1': 'Lunes',
    '2': 'Martes',
    '3': 'Miercoles',
    '4':'Jueves',
    '5':'Viernes',
    '6':'Sabado',
    '7':'domingo'
}

for num,day in week.items():
    print(str(num)+" -> "+str(day))
#Using a dictionary, compute the numbers of times each word occurs.                 2
ejemplo=['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']
dog=0
pencil=0
fence=0
apple=0
comprobante=['dog', 'pencil', 'fence', 'apple' ]
for i in range(len(ejemplo)):
    if comprobante[0] == ejemplo[i]:
        dog=dog+1
    elif comprobante[1]==ejemplo[i]:
        pencil=pencil+1
    elif comprobante[2]==ejemplo[i]:
        fence=fence+1
    elif comprobante[3]==ejemplo[i]:
        apple=apple+1

i=0;
print("la palabra "+str(comprobante[i])+" se repite "+str(dog))
i=i+1
print("la palabra "+str(comprobante[i])+" se repite "+str(pencil))
i=i+1
print("la palabra "+str(comprobante[i])+" se repite "+str(fence))
i=i+1
print("la palabra "+str(comprobante[i])+" se repite "+str(apple))
#Using this, print out the two most frequently occuring items.                      3
#(Hint: Try converting the dictionary to a list of key-value pairs 
#(or value-key pairs) and sort it.)

#                                                                               Ejercicio 4
#Write a function which computes the symmetric difference of two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) 
print(z)
#Suppose you have a list of numbers like:                                           2
#[1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]
#How could you use a set data structure to remove 
#all the duplicates from the list?
lista=[1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]
aux_lista=[]
for i in range(len(lista)):
    aux_lista.insert(0,lista[0])
    for j in range(len(aux_lista)):
        
     if aux_lista[j] != lista[i]:
      aux_lista.insert(j,lista[i])
    