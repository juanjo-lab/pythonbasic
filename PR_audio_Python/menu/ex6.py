#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:54:27 2017
Funciones referentes a la PRACTICA 2, Ejercicio 6
@author: carabias
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

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
    
    def barridoretardo(filename):
        delay=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200,500]
        fs, x = audioread(filename+".wav")
        #normalizamos
        x=x*0.2/max(abs(x))
        x=x-np.mean(x)
        
        for i in range(len(delay)):
            ceros = np.zeros(int(fs*delay[i]/1000.0))
            haas = np.vstack((np.hstack((x, ceros)), np.hstack((ceros, x)))).T
            # audioplay(haas,Clackson fs)
            audiowrite(filename+"_" + str(int(delay[i])) + '_.wav', fs, haas)
        return
    
    
    def audiowrite(filename, fs, x):
        """Similar to Matlab's function to write wav files"""
        wav.write(filename, fs, x)
        print ("Audio writing complete")
        return
    
    # ---------------------------------------------------------------------------
        
    # ----------------------   MAIN  -----------------------------
    
    filename=input("introduce el nombre del archivo que se le va a realizar el barrido de retardos")
    barridoretardo(filename)