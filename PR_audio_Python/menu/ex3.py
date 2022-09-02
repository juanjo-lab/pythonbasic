#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:37:20 2017
Funciones referentes a la PRACTICA 2, Ejercicio 3
@author: carabias
"""

from scipy.fftpack import fft, fftshift
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
from scipy.signal import freqz
def main():
    # ---------------  Funciones Auxiliares -------------------------------------
    def audioread(filename):
        """Similar to Matlab's function to read wav files"""
        [fs, audio] = wav.read(filename)
        print ("Audio reading complete")
        return fs, audio
    
    
    def audiowrite(filename, fs, x):
        """Similar to Matlab's function to write wav files"""
        wav.write(filename, fs, x)
        print ("Audio writing complete")
        return
    
    
    
    
    def audiorecord(duration, fs, nchan=2):
        """Similar to Matlab's function audiorecord to listen audio files"""
        input('Starting recording, Press enter to continue...')
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=nchan, dtype='float64')
        sd.wait()
        print ("Audio recording complete")
        return myrecording
    
    
    def myspectrogram(x, fs, windowsize=282, hopsize=80, fftsize=512):
        """Similar to Matlab's function spectrogram"""
        if len(x.shape)>1: # Several channels
            x = x[:,0] # Take the first (left)
            
        f, t, X = signal.spectrogram(x, fs=fs, window=signal.hamming(windowsize), noverlap=hopsize, nfft=fftsize, mode='psd')
        plt.figure()
        plt.pcolormesh(t, f, 10.0*np.log10(X+np.spacing(1)))
        plt.ylabel('Frequency [kHz]')
        plt.xlabel('Time [sec]')
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Power/frequency (dB/Hz)', rotation=270)
        plt.show()
        return f, t, X
    
    
    def butter_bandpass_filter(data, lowcut, highcut, fs, order=6):
        """Genera un filtro paso bandaInput:
                - data: Senal de entrada de tipo numpy array
                - lowcut: Frecuencia de corte inferior
                - high cut: Frecuencia de corte superior
                - fs: Frecuencia de muestreo
                - orden: numero coeficiones del filtro (default 6)
            Output:
                - y: Senal de salida obtenida como y(n) = x() * cos(pi*n), siendo n la muestra actual
        """
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        Wn=[low, high]
        b, a = signal.butter(order,Wn, btype='band')    
        y = signal.lfilter(b, a, data)
        
        
        plt.figure(1)
        plt.clf()
        w, h = freqz(b, a)
        plt.plot((nyq / np.pi) * w, abs(h), label="order = 6")
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Ganancia')
        plt.grid(True)
        plt.legend(loc='best')
        
        return y
    
    
    # ---------------------------------------------------------------------------
    
    def denpower(x, fs):
        """ DENSIDAD ESPECTRAL DE POTENCIA  -- Igual que en ejercicio 2
            Input:
                - x: Senal de entrada de tipo numpy array
                - fs: Frecuencia de muestreo
            Output:
                - y: Senal de salida obtenida como y(n) = x() * cos(pi*n), siendo n la muestra actual
        """
        y=abs(fft(x,10*len(x))/fs)**2;
        return y
    
    # ----------------------   MAIN  -----------------------------
    
    #                                                                                 APARTADO 3
    opc=0
    while opc!=6:
        print('---------------SUB-MENU-------EX2---')
        print('1. DENSIDAD ESPECTRAL DE LA SEÑAL GRABADA')
        print('2. SEÑAL VOCAL A')
        print('3. SEÑAL SORDA')
        print('4. HISTOGRAMA DE LA SEÑAL GRABADA')
        print('5. FILTRO BUTTER')
        print('6. SALIDA')
        
        
        opcion=float(input('Que opción desea'))
        
        if opcion==1:
                [fs,x]=audioread("todosjuntos_16bit_PCM.wav")
                
                X=denpower(x[:,0],fs)
                fig1=plt.figure()
                subplot2 = fig1.add_subplot(111)
                f = np.linspace(-fs/2,fs/2,len(X))
                subplot2.plot(f,fftshift(X))
                subplot2.set_xlabel('Frecuencia (Hz)')
                subplot2.set_title('Densidad Espectral de Potencia')#representamos en freq
                plt.show()
    
        elif opcion ==2:
    
                [fs,x]=audioread("a_16bit.wav")
                f, t, X=myspectrogram(x[:,0], fs, windowsize=282, hopsize=80, fftsize=512)
                X=denpower(x[:,0],fs)
                fig3=plt.figure()
                subplot2 = fig3.add_subplot(111)
                f = np.linspace(-fs/2,fs/2,len(X))
                subplot2.plot(f,fftshift(X))
                subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia(a)')#representamos en freq
                # Crea histograma
                fig5, ax = plt.subplots() 
                ax.hist(x[:,0])
                ax.set_title("histograma de A" )
                # Show plot 
                plt.show()
                
        elif opcion ==3:
                [fs,x]=audioread("s_16bt.wav")
                f, t, X=myspectrogram(x[:,0], fs, windowsize=282, hopsize=80, fftsize=512)
                X=denpower(x[:,0],fs)
                fig4=plt.figure()
                subplot2 = fig4.add_subplot(111)
                f = np.linspace(-fs/2,fs/2,len(X))
                subplot2.plot(f,fftshift(X))
                subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia(s)')#representamos en freq
                # Crea histograma
                fig6, sx = plt.subplots() 
                sx.hist(x[:,0])
                sx.set_title("histograma de S" )
                # Show plot 
                plt.show() 
                
    
        elif opcion ==4:
                [fs,x]=audioread("todosjuntos_16bit_PCM.wav")
                # Crea histograma
                fig5, ax = plt.subplots() 
                ax.hist(x[:,0])
                ax.set_title("histograma de todos los audios" )
                # Show plot 
                plt.show() 
    
        elif opcion==5:
                # filtro butter:
                lowcut= float(input('fc1? '))
                highcut= float(input('fc2? '))
                [fs,data]=audioread("ursula.wav")
                data=data/max(abs(data))
                data=data-np.mean(data)
                y=butter_bandpass_filter(data, lowcut, highcut, 44100, order=6)
                fig1 = plt.figure()
                subplot1= fig1.add_subplot(111)
                t=np.arange(0,len(data)/fs,1/fs)
                subplot1.plot(t,data,label="original")
                
                subplot1.plot(t,y,label="filtrada")
                subplot1.set_xlabel('Tiempo(s)')
                subplot1.set_ylabel('Amplitud')#la representamos en el tiempo
                plt.legend(loc='best')
                plt.show()
                
                filename=input("introduce el nombre del archivo filtrado")
                audiowrite(filename+".wav", fs, y)
        elif opcion==6:
                opc=6
