# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 08:54:48 2020

@author: juanjo
"""
#APARTADO 3
#                                                                               EJERCICIO1
#Create a uniform subdivision of the interval -1.3 to 2.5                           1
#with 64 subdivisions
import numpy as np
import matplotlib.pyplot as plt
import math
fs=3.8/(64)
n=np.arange(-1.3,2.5,fs)

#Generate an array of length  3n  filled with the cyclic pattern 1, 2, 3.           2

A  =  np . zeros ((3,3 )) 
for i in range(3):
    for j in range(3):
        A[i,j]=j+1
#Create an array of the first 10 odd integers.                                      3
A=np.arange(1,20,2)

#Create a 10 x 10 arrays of zeros and then "frame" it with a border of ones.        4
A=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        if i==0:
            A[0,j]=1
        elif j==0:
            A[i,j]=1
        elif i==10-1:
            A[10-1,j]=1
        elif j==10-1:
            A[i,10-1]=1
#Create an 8 x 8 array with a checkerboard pattern of zeros and ones using a        5
# slicing+striding approach.
A=np.zeros((8,1))
C=np.zeros((8,8))
for i in range(len(A)):
    if i%2==0:
        A[i]=1
for j  in range(8):
    for i in range(8):
        C[j,i]=A[i,0]
        
        #◘SIN RESOLVER
#                                                                                   EJERCICO2
#Try using the dot function on a vector-vector, matrix-vector and matrix-           
# example. (This may seem simple but it's good to see how the results differ in     1
# each case.)

                         #sin resolver
#Create a plot of  x2⋅sin(1/x2)+x  on the interval  [−1,1]  using 250 points.       2
# Remember to label the axes!
x = np.linspace(-5, 5, 250)
y=(x**2)*np.sin(1/(x**2))+x
plt.figure()
plt.plot(x, y)
plt.xlabel("muestras")
plt.ylabel("amplitud")
plt.title("ejemplo 1")
plt.show()

#Create a semilogy plot of the relative difference of  1/(1+x2)  and  1/x2          3
#on the interval  [5,25] . (The relative difference of numbers  a  and  b 
# is given by  |1−a/b| . It provides a better sense of error relative to the 
#order of magnitudes of  a  and  b .)
x = np.linspace(5,25, 250)
y= (1/(1+x**2)) -  (1/x**2)
plt.figure()
plt.plot(x, y)
plt.show()
#It was mentioned that many common functions are availible in vectorized form.      4
#It turns out that Scipy also has many less common, special functions. Take a
# look at the extensive list here! Try looking for some interesting ones you 
#recognize (or maybe don't recognize!) and either plug in a few numbers or plot them.
#enlace= https://docs.scipy.org/doc/scipy/reference/special.html

#                                                                                 EJERCICO 3
#reate a color plot of  sin(x)sin(y)  on the interval  [−π,π]×[−π,π] .
x = np.linspace(-math.pi,math.pi)
y=np.linspace(-math.pi,math.pi)
c=np.linspace(-math.pi,math.pi)
for i in range(len(x)):
    y[i]=math.sin(x[i])
    c[i]=math.sin(y[i])

plt.figure()
plt.plot(x,c)
plt.show()
#Create a function which creates an  n×n  array with  (i,j) -entry equal to  i+j .    2
a=int(input("introduce para nuestra matriz nxn"))
Z = np.zeros((a,a))
for i in range(a):
    for j in range(a):
        Z[i,j]=i+j
        
#Evaluate  cos  and  sin  on the interval  [0,1]  and then stack the results    EJERCICIO 4
#into a tall array with rows being the  (cos(x),sin(x))  entries.                      1
x=np.linspace(0,1)
y=math.cos(x)
c=math.sin(x)
Z = np.zeros((2,len(y)))
for i in range(2):
    Z[1,j]=y[i]
    Z[2,j]=c[i]