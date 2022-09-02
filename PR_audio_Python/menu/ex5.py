#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:54:27 2017
Funciones referentes a la PRACTICA 2, Ejercicio 5
@author: carabias
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import math 

def main():
    # ---------------  Funciones Auxiliares -------------------------------------
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
    
    def sintono(A, f0, fs, t_ini, t_fin):
        t = np.arange(t_ini, t_fin, 1/fs) 
        x=2*math.pi*f0*t
        signal = np.sin(x)*A
        return signal
    # ---------------------------------------------------------------------------
        
    # ----------------------   MAIN  -----------------------------
    fs = 22100
    A = 0.8
    t_ini = 0
    t_fin= 2
    tono_1=[]
    tono_2=[]
    opc=0
    while opc!=4:
        print('---------------SUB-MENU-------EX2---')
        print('1. GENERAR TONO 1')
        print('2. GENERAR TONO 2')
        print('3. SUMAR TONOS (se escuchara al termuinar la suma)')
        print('4. SALIDA')
        
        opcion=float(input('Que opción desea'))
        if opcion==1:
            
            f_1=float(input("frecuencia del primer tono"))
            tono_1=sintono(A, f_1, fs, t_ini, t_fin)
            audiowrite("ej5_"+str(f_1)+"Hz_0.8V.wav", fs, tono_1)
            print("tono guardado")
        
        elif opcion==2:
    
            f_2=float(input("frecuencia del segundo tono"))
            tono_2=sintono(A/5, f_2, fs, t_ini, t_fin)
            audiowrite("ej5_"+str(f_2)+"Hz_85V.wav", fs, tono_2)
            print("tono2 guardado")
        elif opcion==3:
            tono_3=tono_1+tono_2
            audioplay(tono_3,fs)
        elif opcion ==4:
            opc=4