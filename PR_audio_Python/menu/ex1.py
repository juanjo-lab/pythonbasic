#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:27:18 2017
Funciones referentes a la PRACTICA 2, Ejercicio 1
@author: carabias
"""

from scipy.fftpack import fft, fftshift, ifft
import matplotlib.pyplot as plt
import numpy as np

def main():  
    def fun_cuadrada():
        """Esta funcion permite la generacion de una senal cuadrada periodica asi como  su posterior filtrado al objeto de
        comprobar el efecto de este sobre la senal original. El filtrado se ha realizado directamente en el dominio de la
        frecuencia eliminando las componentes indeseadas.
        """
    
        fs = float(input('Frecuencia de muestreo (Hz)? '))
        a = float(input('Inicio del intervalo de observacion (sg)? '))
        b = float(input('Final del intervalo de observacion (sg)? '))
        F = float(input('Frecuencia de la senal cuadrada (Hz)? '))
        T = 1.0 / F
    
        B = float(input('Ciclo de trabajo (en tanto por uno)? '))
        while B > 1:
            B = float(input('Introduce un ciclo de trabajo menor.'))
    
        A = float(input('Amplitud (voltios)? '))
    
        # Creacion de la funcion base
        n_unos = int(np.round(B * T * fs))
        n_ceros = int(np.round((1 - B) * T * fs))
        base = np.hstack((A * np.ones(n_unos), np.zeros(n_ceros)))
    
        t = np.arange(a, b, 1/fs)  # Vector de instantes de muestreo
        LT = t.size
        n_per = np.fix(LT / base.size)  # periodos completos de la base
        x = base
        for i in np.arange(0, n_per):
            x = np.hstack((x, base))
    
        x = x[0:LT]  # Se afina longitud del vector
    
        # Visualizacin de la senal resultante
        fig1 = plt.figure()
        subplot1 = fig1.add_subplot(211)
        subplot1.plot(t, x); subplot1.axis([min(t), max(t), min(x) - .1, max(x) + 0.1])
        subplot1.set_xlabel('Segundos'); subplot1.set_ylabel('Voltage')
        subplot1.set_title('SENAL EN EL DOMINIO DEL TIEMPO')
    
        # fft
        fftx = fft(x)
        DEP = np.abs(fftx * np.conj(fftx))/LT
    
        subplot2 = fig1.add_subplot(212)
        subplot2.plot(np.linspace(-fs/2, fs/2, LT), fftshift(DEP))
        subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia')
        plt.show()
    
        # Filtrado
        Fc = 1
        while Fc > 0:
            Fc = float(input('Frecuencia de corte del filtro paso-bajo (Hz)? (0 to EXIT). '))
            M = round(Fc / fs * LT)
            Filtro = np.hstack((np.ones(int(M) + 1), np.zeros(int(LT) - (2 * int(M) + 1)), np.ones(int(M))))
    
            fig2 = plt.figure()
            subplot1 = fig2.add_subplot(411 )
            subplot1.plot(t, x); subplot1.axis([min(t), max(t), min(x) - .1, max(x) + 0.1])
            subplot1.set_xlabel('Segundos'); subplot1.set_ylabel('Voltage')
            subplot1.set_title('SENAL EN EL DOMINIO DEL TIEMPO')
    
            subplot2 = fig2.add_subplot(412)
            subplot2.plot(np.linspace(-fs / 2, fs / 2, LT), fftshift(DEP))
            subplot2.set_xlabel('Frecuencia (Hz)'); subplot2.set_title('Densidad Espectral de Potencia')
    
            subplot3 = fig2.add_subplot(413)
            subplot3.plot(np.arange(-fs / 2, fs / 2, fs / (LT)), fftshift(Filtro))
            subplot3.plot(np.arange(-fs / 2, fs / 2, fs / (LT)), fftshift(abs(fftx) * Filtro / LT), 'r')
            subplot3.set_title('Filtro (azul) y salida del filtro (rojo)')
    
            subplot4 = fig2.add_subplot(414)
            subplot4.plot(t, np.real(ifft(fftx * Filtro)))
            subplot4.set_xlabel('Tiempo')
            subplot4.set_title('Salida del filtro (hasta ' + str(np.fix(Fc / F)) + ' F0)')
            plt.show()
        return x,fs
            
    
    # # ----------------------   MAIN  -----------------------------
    # if __name__ == "__main__":
    [x,fs]=fun_cuadrada()