#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:54:27 2017
Funciones referentes a la PRACTICA 2, Ejercicio 4
@author: carabias
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import math
def main():
    # ---------------  Funciones Auxiliares -------------------------------------
    
    
    def audiowrite(filename, fs, x):
        """Similar to Matlab's function to write wav files"""
        wav.write(filename, fs, x)
        print ("Audio writing complete")
        return
    def audioplay(x, fs):
        """Similar to Matlab's function soundsc to listen audio files"""
        sd.play(x, fs)
        sd.wait()
        return
    
    def audioread(filename):
        """Similar to Matlab's function to read wav files"""
        [fs, audio] = wav.read(filename)
        print ("Audio reading complete")
        return fs, audio
    
    def sintono(A, f0, fs, N):
        t=np.arange(0,N/fs,1/fs)
        x=2*math.pi*f0*t
        signal = np.sin(x)*A
        return signal,t
    # ---------------------------------------------------------------------------
    
    # ----------------------   MAIN  -----------------------------
    opc=0
    while opc!=3:
        print('---------------SUB-MENU-------EX2---')
        print('1. GENERAR TONO')
        print('2. REALIZAR BARRIDOS EN FRECUENCIA Y AMPLITUD(aviso: realiza todos los barridos y lleva bastante tiempo)')
        print('3. SALIDA')
        
        
        opcion=float(input('Que opción desea'))
        if opcion==1:
            fs = 44100
            A = float(input('Amplitud (voltios)? '))
            f0 = float(input('Frecuencia de la senal (Hz)? '))
             
            t_ini = float(input('Inicio del intervalo de observacion (sg)? '))
            t_fin= float(input('Final del intervalo de observacion (sg)? '))
            N=abs((t_fin-t_ini)*fs)
            [tono,t]=sintono(A, f0, fs, N)
            audioplay(tono,fs)
            fig2 = plt.figure()
            subplot1 = fig2.add_subplot(111)
            subplot1.plot(t,tono)
            subplot1.set_xlabel('Segundos')
            subplot1.set_ylabel('Voltage')
            subplot1.set_title('SENAL EN EL DOMINIO DEL TIEMPO')
            plt.show()
            filename=input("introduce el nombre del archivo")
            
            audiowrite(filename+".wav", fs, tono)
            
        elif opcion==2:
    #barridos
            f=np.array([100,500,2000,4000,8000,12000])
            A=np.array([1,0.5,0.1,0.05,0.01,0.005])
            for i in range(len(f)):
               for j in range(len(A)):
                    [tono,t]=sintono(A[j],f[i], 44100, 44100)
                    audiowrite("ej4_"+str(f[i])+"Hz_"+str(A[j])+"V.wav", 44100, tono)
        elif opcion==3:
            opc=3



for i in range(len()):
    print("---------------------------------------")
    print("paciente: "+i.toString())          
        print("nombre"+paciente())
                
                
