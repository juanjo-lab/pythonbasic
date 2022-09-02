#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:41:02 2017
Funciones referentes a la PRACTICA 2, Ejercicio 2
@author: carabias
"""
from scipy.fftpack import fft, fftshift
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import math

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
    
    
    
    # ---------------------------------------------------------------------------
    def inversor(x):
        """ 
            INVERSOR ESPECTRO
            Input:
                - x: Senal de entrada x de tipo numpy array
            Output:
                - y: Senal de salida obtenida como y(n) = x() * cos(pi*n), siendo 
                     n la muestra actual
        """
        
        y=np.zeros(len(x))
        for n in np.arange(len(x)):
            y[n]=x[n]*((-1)**n) 
        return y
    
    
    def denpower(x, fs):
       """ DENSIDAD ESPECTRAL DE POTENCIA
            Input:
                - x: Senal de entrada de tipo numpy array
                - fs: Frecuencia de muestreo
            Output:
                - DEP = abs(fft(x)*conj(fft(x)))/len(x)     DEP_X=denpower(x,fs)
        """
       DEP=abs(fft(x,10*len(x))/fs)**2;
       # f=np.arange(-fs/2,fs/2,fs/len(DEP))
       # DEP_FIG =plt.figure()
       # dep_fig = DEP_FIG.add_subplot(111)
       # dep_fig.plot(f,fftshift(DEP))
       # dep_fig.set_xlabel("freq Hz")
       # dep_fig.set_ylabel("Voltios V")
       # dep_fig.set_title("Densidad espectral de potencia")
       return DEP
    def espectro(x, fs):
       """ DENSIDAD ESPECTRAL DE POTENCIA
            Input:
                - x: Senal de entrada de tipo numpy array
                - fs: Frecuencia de muestreo
            Output:
                - DEP = abs(fft(x)*conj(fft(x)))/len(x)     DEP_X=denpower(x,fs)
        """
       DEP=abs(fft(x,10*len(x))/fs);
       #f=np.arange(-fs/2,fs/2,fs/len(DEP))
       # DEP_FIG =plt.figure()
       # dep_fig = DEP_FIG.add_subplot(111)
       # dep_fig.plot(f,fftshift(DEP))
       # dep_fig.set_xlabel("freq Hz")
       # dep_fig.set_ylabel("Voltios V")
       # dep_fig.set_title("Densidad espectral de potencia")
       return DEP
      
    
    def triangular(A, fo, fs,t_ini,t_fin):
        """ Genera senal triangular
        Input:
            - A: Amplitud
            - f0: Freq. Fundamental
            - fs: Frecuencia de muestreo (default 1500.0)
            - t_ini: Tiempo de inicio (default 0 segs)
            -t_fin: Tiempo de fin (default 5 segs)
        Output:
            - t: Vector de tiempos (en muestras)
            - tri: Senal triangular de salida
            
        PISTA: use la funcion signal.sawtooth (scipy)
        """
        ts = np.arange(abs((t_ini-t_fin))*fs)
        tri= (1+signal.sawtooth(2 *np.pi * fo *ts / fs ,width=0.5))*(A/2)
        # TRIP_FIG =plt.figure()
        # tri_fig = TRIP_FIG.add_subplot(111)
        # tri_fig.plot(ts/fs,tri)
        # tri_fig.set_xlabel("tiempo s")
        # tri_fig.set_ylabel("Voltios V")
        # tri_fig.set_title("señal triangular")
        return tri,ts
    
    
    def cuadrada(A, f0, fs, B, t_ini,t_fin):
        """ Genera senal triangular
        Input:
            - A: Amplitud
            - f0: Freq. Fundamental
            - fs: Frecuencia de muestreo (default 1500.0)
            - B: Ciclo de trabajo (en el rango [0,1])
            - t_ini: Tiempo de inicio (default 0 segs)
            -t_fin: Tiempo de fin (default 5 segs)
        Output:
            - t: Vector de tiempos (en muestras)
            - y: Senal triangular de salida
            
        PISTA: use la funcion fun_cuadrada del ejercicio1
        """ 
        T = 1.0 / f0
        while B > 1:
            B = float(input('Introduce un ciclo de trabajo menor.'))
    
        # Creacion de la funcion base
        n_unos = int(np.round(B * T * fs))
        n_ceros = int(np.round((1 - B) * T * fs))
        base = np.hstack((A * np.ones(n_unos), np.zeros(n_ceros)))
    
        t = np.arange(t_ini, t_fin, 1/fs)  # Vector de instantes de muestreo
        LT = t.size
        n_per = np.fix(LT / base.size)  # periodos completos de la base
        x = base
        for i in np.arange(0, n_per):
            x = np.hstack((x, base))
    
        x = x[0:LT]  # Se afina longitud del vector
    
        # Visualizacin de la senal resultante
        # fig1 = plt.figure()
        # subplot1 = fig1.add_subplot(211)
        # subplot1.plot(t, x); subplot1.axis([min(t), max(t), min(x) - .1, max(x) + 0.1])
        # subplot1.set_xlabel('Segundos'); subplot1.set_ylabel('Voltage')
        # subplot1.set_title('SENAL EN EL DOMINIO DEL TIEMPO')
        cua=x
        return cua, t
    
    def sintono(A, f0, fs, t_ini, t_fin):
        t = np.arange(t_ini, t_fin, 1/fs) 
        for i in np.arange(len(t)):
            x=2*math.pi*f0*t
            signal = np.sin(x)*A    
        return signal,t
    
    # # ----------------------   MAIN  -----------------------------
    
    opc=0
    while opc!=5:
        print('---------------SUB-MENU-------EX2---')
        print('1. TONO')
        print('2.TRIANGULO')
        print('3. CUADRADO')
        print('4. AUDIO')
        print('5. CERRAR SESION')
        
        
        opcion=float(input('Que opción desea'))
        
        if opcion==1 or opcion==2 or opcion==4 or opcion==3:
            
            # xinvert=inversor(x)#FORMULA DE INVERSO 
            # DEP_X=denpower(x,fs)#FORMULA DE DENSIDAD DE POTENCIA
            #PREGUNTAMOS POR LAS VARIABLES COMUNES 
            fs = float(input('Frecuencia de muestreo (Hz)? '))
            #fs=16000
            A = float(input('Amplitud (voltios)? '))
            f0 = float(input('Frecuencia de la senal (Hz)? '))
             
            t_ini = float(input('Inicio del intervalo de observacion (sg)? '))
            t_fin= float(input('Final del intervalo de observacion (sg)? '))
        
        if opcion==1:
            
    #REPRESENTAMOS EL TONO CON LAS VARIABLES QUE SE NOS EXIGE
    #                                      TONO, SENO
            [sin,t]=sintono(A, f0, fs, t_ini, t_fin)#llamamos a la funcion 
            fig1 = plt.figure()
            subplot1= fig1.add_subplot(411)
            subplot1.plot(t,sin)
            subplot1.set_xlabel('Tiempo(s)');subplot1.set_ylabel('Amplitud')#la representamos en el tiempo
            
            SINX= denpower(sin,fs)#calculamos su DEP
            subplot2 = fig1.add_subplot(412)
            f = np.linspace(-fs/2,fs/2,len(SINX))
            subplot2.plot(f,fftshift(SINX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia')#representamos en freq
            N = np.arange(len(sin))
            subplot3 = fig1.add_subplot(413)
            
            inv_sin= inversor(sin)
            subplot3.plot(N,inv_sin)
            subplot3.set_xlabel('n*TS'); subplot3.set_title('Inversor')
            
            SINX=espectro(sin,fs)
            subplot2 = fig1.add_subplot(414)
            f = np.linspace(-fs/2,fs/2,len(SINX))
            subplot2.plot(f,fftshift(SINX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Representacion del espectro')#representamos en freq
            plt.show()
    
    # #                                   TRIANGULO
        elif opcion==2:
            
            [tri,t]=triangular(A, f0, fs, t_ini, t_fin)#llamamos a la funcion 
            fig1 = plt.figure()
            subplot1= fig1.add_subplot(411)
            subplot1.plot(t,tri)
            subplot1.set_xlabel('Tiempo(s)');subplot1.set_ylabel('Amplitud')#la representamos en el tiempo
            
            TRIX= denpower(tri,fs)#calculamos su DEP
            subplot2 = fig1.add_subplot(412)
            f = np.linspace(-fs/2,fs/2,len(TRIX))
            subplot2.plot(f,fftshift(TRIX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia')#representamos en freq
            
            inv_tri=inversor(tri)
            N = np.arange(len(tri))
            subplot3 = fig1.add_subplot(413)
            subplot3.plot(N,inv_tri)
            subplot3.set_xlabel('n*TS'); subplot3.set_title('Inversor')
            
            TRIX=espectro(tri,fs)
            subplot2 = fig1.add_subplot(414)
            f = np.linspace(-fs/2,fs/2,len(TRIX))
            subplot2.plot(f,fftshift(TRIX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Representacion del espectro')#representamos en freq
            plt.show()
    
    
    
    # #                                   CUADRADO
        elif opcion==3:
            
            B = float(input('Introduce un ciclo de trabajo menor.'))
            [cua,t]=cuadrada(A, f0, fs,B, t_ini, t_fin)#llamamos a la funcion 
            fig1 = plt.figure()
            subplot1= fig1.add_subplot(411)
            subplot1.plot(t,cua)
            subplot1.set_xlabel('Tiempo(s)');subplot1.set_ylabel('Amplitud')#la representamos en el tiempo
            
            CUAX=denpower(cua,fs)#calculamos su DEP
            subplot2 = fig1.add_subplot(412)
            f = np.linspace(-fs/2,fs/2,len(CUAX))
            subplot2.plot(f,fftshift(CUAX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia')#representamos en freq
            
            inv_cua=inversor(cua)
            N = np.arange(t_ini,t_fin*fs,1)
            subplot3 = fig1.add_subplot(413)
            subplot3.plot(N,inv_cua)
            subplot3.set_xlabel('n*TS'); subplot3.set_title('Inversor')
            
            CUAX=espectro(cua,fs)
            subplot2 = fig1.add_subplot(414)
            f = np.linspace(-fs/2,fs/2,len(CUAX))
            subplot2.plot(f,fftshift(CUAX))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Representacion del espectro')#representamos en freq
            plt.show()
      
    
    # #                                   AUDIOREAD
        elif opcion ==4:
            
            fs,x =audioread("ursula.wav")
            
            invx =inversor(x)
            
            t = np.arange(0,float(len(x))/fs, 1.0/fs)
            fig1 = plt.figure()
            
            subplot1= fig1.add_subplot(211)
            subplot1.plot(t,x)
            subplot1.set_title("Señal de voz");subplot1.set_xlabel("Segundos")
            subplot1.set_ylabel("Amplitud")
            subplot2 = fig1.add_subplot(212)
            subplot2.hist(x,100)
            subplot2.set_title("Histograma de la senal de voz")
            subplot2.set_xlabel("Amplitud")
            plt.show()
        
        elif opcion==5:
            
            opc=5