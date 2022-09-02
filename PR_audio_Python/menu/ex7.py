#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:54:27 2017
Funciones referentes a la PRACTICA 2, Ejercicio 7
@author: carabias
"""
# pagina 23 word, filtro multi eco, pagina 15
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
from scipy.fftpack import fft,ifft

def main():
    # ---------------  Funciones Auxiliares -------------------------------------
    def audioread(filename):
        """Similar to Matlab's function to read wav files"""
        [fs, audio] = wav.read(filename)
        print ("Audio reading complete")
        return fs, audio
    
    def audioplay(x, fs):
        """Similar to Matlab's function soundsc to listen audio files"""
        sd.play(x, fs)
        sd.wait()
        return
    
    def audiowrite(filename, fs, x):
        """Similar to Matlab's function to write wav files"""
        wav.write(filename, fs, x)
        print ("Audio writing complete")
        return
    
    # ---------------------------------------------------------------------------
        
    # ----------------------   MAIN  -----------------------------
    
    # FRECUENCIA
    def tf(x):
        y=fft(x)
        return y
    def IDFT(p):
        y=ifft(p)
        y=y.real
        return y
    
    def impz(alpha,delay,fs,N):#respuesta al impulso
        # definimos cada cuantos 0 se encuentra nuestro eco, en funcion de cada cuanto introduzcamos de delay
        N_delay=int(fs*delay)
        # declaramos h Con el mismo numero de muestras que X, ahorrando el tener que normalizar
        h=np.zeros(N)
        # inicializamos el contador
        i=1
        while int(N_delay*i)<len(h):
            h[N_delay*i]=alpha**(i-1)#Como vemos, en el caso 1, vale 1, en el caso 2 vale alpha, en el 3 alpha**2 y asi sucesivamente
            i+=1  
        # plt.figure()
        # plt.plot(h)
        return h
    
    def eco(x, fs,delay,alpha):
        
        h=impz(alpha,delay,fs,len(x))
        H=tf(h)
        X=tf(x)    
        # plt.figure()
        # plt.plot(abs(H))    
        Y=X*H#se realiza la convolucion en el tiempo, que en este caso, al realizarlo en frecuencia, sabemos desde 1º de carrera que una convolucion en frecuencia es una multiplicacion
        y=IDFT(Y)
        # plt.figure()
        # plt.plot(y)
        
        return y
    
    opc=0
    
    filename=input("Por favor introduzca el nombre del archivo.wav que desea usar(debe estar en el mismo fichero que nuestra funcion) =")
    [fs,x] = audioread(filename+".wav")
    x=x*0.9/max(abs(x))#nos aseguramos que tiene los maximos por debajo de 1
    x=x-np.mean(x)#normalizamos nuestra señal de entrada a 0 
    
    while opc!=4:
        
        print('---------------SUB-MENU-------EX2---')
        print('1. BARRIDO EN RETARDOS')
        print('2. BARRIDO EN ALPHA')
        print('3. REPRESENTACION EN FRECUENCIA Y TEMPORAL DE NUESTRO IMPULSO')
        print('4. VOLVER AL MENU PRINCIPAL')
        
        opcion=float(input('Que opción desea'))
        
        if opcion==1:
            # plt.figure()
            # plt.plot(x)  
            delay=[0.001,0.005,0.02,0.05,0.1,0.2,0.5,2]
            for i in range(len(delay)):
                salida=eco(x,fs,delay[i],0.9)
                audiowrite("ej7_eco_delay_"+str((delay[i]))+"_.wav",fs,salida)
        
        elif opcion==2:
            #barrido de alpha
            alpha=[0.03, 0.1, 0.3, 0.5, 0.7, 0.85, 1, 1.5]
            for i in range(len(delay)):
                salida=eco(x,fs,0.05,alpha[i])
                audiowrite("ej7_eco_alpha_"+str((alpha[i]))+"_.wav",fs,salida)
            
        
        elif opcion==3:
            
            alpha=float(input("¿que valor de alpha desea? ="))
            h=impz(alpha,0.5,fs,len(x))
            fig=plt.figure()
            plt.plot(h)
            plt.title("representacion en el tiempo con (alpha)="+str(alpha))
            fig.show()
            plt.show()#sige sin dejarme plotear mientras esta ejecutando  :(
            H=tf(h)
            plt.figure()
            plt.plot(abs(H))
            plt.title("REPRESENTACION EN FREQ (alpha)="+str(alpha)) 
            plt.show()
            
        elif opcion==4:
            
            opc=4
            
    






