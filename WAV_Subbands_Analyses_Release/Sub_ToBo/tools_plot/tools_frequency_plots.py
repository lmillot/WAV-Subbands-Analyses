#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script_name :       tools_frequency_plots.py

creation date:      05/08/2024, 14h05
modification date:  09/10/2024, 22h28

@author: Laurent Millot
"""


import matplotlib.pyplot as plt
import numpy as np


# ----------
def plot_linear_spectrum(sig_array, sample_rate, filename, the_path, 
                         x_limits=[0, 22050], the_language=""):
    """  
    plot_linear_spectrum(sig_array, sample_rate, filename, the_path,
                         x_limits, the_language)
    
    Calculates and plots the linear magnitude of the spectrum using the
    defined parameters.

    Parameters :
    ------------
    sig_array : numpy array
        array of the monophonic signal to be studied
        
    sample_rate : int
        sample rate in Hertz of the studied signal
        
    filename : string
        filename for the plot of the linear spectrum
        
    the_path : pathlib.PATH
       path for the plot of the linear spectrum
       
    x_limits: list of integers
        list defining the left and right frequencies to plot.
        default list: x_limits = [0, 22050]

    the_language : string
        if equal to "french" the labels and titles are written in French, 
        otherwise in English

    Returns :
    ---------
    None.
    """
    if sig_array is None or sample_rate is None:
        return

    # Calculation of the FFT of the signal
    the_length = len(sig_array)
    T = 1.0 / sample_rate
    
    amp_spec_array = np.fft.fft(sig_array)
    freq_array = np.fft.fftfreq(the_length, T)[: the_length//2]

    # Calculation of the linear magnitude of the spectrum
    amp_spec_array = 2.0 / the_length * np.abs(amp_spec_array[: the_length//2])

    # Plot of the linear magnitude of the spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(freq_array, amp_spec_array, color='blue')
    
    if the_language == "french":
        plt.title('Spectre d\'amplitude (linear) : ' + filename[:-4])
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude')

    else:
        plt.title('Magnitude spectrum (linear) : ' + filename[:-4])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (linear)')
        
    if x_limits[1] > sample_rate:
        x_limits[1] = sample_rate

    plt.xlim(x_limits)
    plt.grid(True)
    
    # save the plot
    if x_limits[0] == 0 and x_limits[1] == sample_rate // 2:
        fig_name = "lin_spec_" + filename[:-4] + ".pdf"

    else:
        fig_name = "lin_spec_" + filename[:-4] + "_zoom_"\
                + str(x_limits[0]) + "Hz_" + str(x_limits[1]) + "Hz.pdf"


    plt.savefig(the_path / fig_name)

    # show the plot after saving or there will be nothing saved in the file
    plt.show()


# ----------
def plot_dB_spectrum(sig_array, sample_rate, filename, the_path, 
                     x_limits=[0, 22050], the_language="", 
                     min_value=1e-10):
    """  
    plot_dB_spectrum(sig_array, sample_rate, filename, the_path, x_limits,
                     the_language, min_value)
    
    Calculates and plots the dB magnitude of the spectrum using
    the defined parameters and a linear axis for the frequencies.

    Parameters :
    ------------
    sig_array : numpy array
        array of the monophonic signal to be studied
        
    sample_rate : int
        sample rate in Hertz of the studied signal
        
    filename : string
        filename for the plot of the linear spectrum
        
    the_path : pathlib.PATH
       path for the plot of the linear spectrum
       
    x_limits: list of integers
        list defining the left and right frequencies to plot.
        default list: x_limits = [0, 22050]
       
    the_language : string
        if equal to "french" the labels and titles are written in French, 
        otherwise in English
       
    min_value : float, optional
        minimal clipping value for the magnitude used to avoid the problem
        of the singularity of the logarithm for zero value
        
    Returns :
    ---------
    None.
    """
    if sig_array is None or sample_rate is None:
        return

    # Calculation of the FFT of the signal
    the_length = len(sig_array)
    T = 1.0 / sample_rate
    
    dB_amp_spec_array = np.fft.fft(sig_array)
    freq_array = np.fft.fftfreq(the_length, T)[: the_length//2]

    # Calculation of the magnitude of the spectrum in dB
    dB_amp_spec_array = 2.0 / the_length \
        * np.abs(dB_amp_spec_array[: the_length//2])

    dB_amp_spec_array = 20 * np.log10(dB_amp_spec_array.clip(min_value))

    # Plot of the magnitude of the spectrum in dB
    plt.figure(figsize=(10, 6))
    plt.plot(freq_array, dB_amp_spec_array, color='blue')
    
    if the_language == "french":
        plt.title('Spectre d\'amplitude (dB): ' + filename[:-4])
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude (dB)')

    else:
        plt.title('Magnitude spectrum (dB): ' + filename[:-4])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')
        
    if x_limits[1] > sample_rate:
        x_limits[1] = sample_rate // 2

    plt.xlim(x_limits)
    plt.grid(True)
    
    # save the plot    
    if x_limits[0] == 0 and x_limits[1] == sample_rate // 2:
        fig_name = "dB_spec_" + filename[:-4] + ".pdf"

    else:
        fig_name = "dB_spec_" + filename[:-4] + "_zoom_"\
                + str(x_limits[0]) + "Hz_" + str(x_limits[1]) + "Hz.pdf"
     
    plt.savefig(the_path / fig_name)

    # show the plot after saving or there will be nothing saved in the file
    plt.show()


# ----------
def plot_logx_dB_spectrum(sig_array, sample_rate, filename, 
                          the_path, x_limits=[0, 22050], the_language="", 
                          min_value=1e-10):
    """
    plot_logx_dB_spectrum(sig_array, sample_rate, filename, the_path, 
                          x_limits, the_language, min_value)
         
    Calculates and plots the dB magnitude of the spectrum using
    the defined parameters and a logarithmic axis for the frequencies.

    Parameters :
    ------------
    sig_array : numpy array
        array of the monophonic signal to be studied
    
    sample_rate : int
        sample rate in Hertz of the studied signal
    
    filename : string
        filename for the plot of the linear spectrum
    
    the_path : pathlib.PATH
        path for the plot of the linear spectrum
           
    x_limits: list of integers
        list defining the left and right frequencies to plot.
        default list: x_limits = [0, 22050]
        
    the_language : string
        if equal to "french" the labels and titles are written in French, 
        otherwise in English
   
    min_value : float, optional
        minimal clipping value for the magnitude used to avoid the problem
        of the singularity of the logarithm for zero value
    
    Returns :
    ---------
    None.
        """
    if sig_array is None or sample_rate is None:
        return

    # Calculation of the FFT of the signal
    the_length = len(sig_array)
    T = 1.0 / sample_rate

    half_length = the_length // 2

    freq_array = np.fft.fftfreq(the_length, T)[: half_length]

    # Plot of the magnitude of the spectrum in dB
    plt.figure(figsize=(10, 6))
    
    dB_amp_spec_array = np.fft.fft(sig_array)

    # Calculation of the magnitude of the spectrum in dB
    dB_amp_spec_array = 2.0 / the_length \
        * np.abs(dB_amp_spec_array[: half_length])

    dB_amp_spec_array = 20 * np.log10(dB_amp_spec_array + min_value)
    
    plt.semilogx(freq_array, dB_amp_spec_array, color='blue')

    if the_language == "french":
        plt.title('Spectre d\'amplitude (dB): ' + filename[:-4])
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude (dB)')

    else:
        plt.title('Magnitude spectrum (dB): ' + filename[:-4])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')

    if x_limits[1] > sample_rate:
        x_limits[1] = sample_rate // 2
        
    plt.xlim(x_limits)
    plt.grid(True)
    
    # save the plot
    if x_limits[0] == 0 and x_limits[1] == sample_rate // 2:
        fig_name = "logx_dB_spec_" + filename[:-4] + ".pdf"

    else:
        fig_name = "logx_dB_spec_" + filename[:-4] + "_zoom_"\
            + str(x_limits[0]) + "Hz_" + str(x_limits[1]) + "Hz.pdf"
    
    plt.savefig(the_path / fig_name)

    # show the plot after saving or there will be nothing saved in the file
    plt.show()


# ----------
def plot_dB_spectra(IRs_array, IRs_number, sample_rate, 
                    analysis_name, the_path, x_limits=[0, 22050], 
                    the_language="", min_value=1e-10):
    """  
    plot_dB_spectra(IRs_array, IRs_number, sample_rate, analysis_name, 
                    the_path, x_limits, the_language, min_value)
    
    Calculates and plots the dB magnitude of the spectrum using
    the defined parameters and a linear axis for the frequencies.

    Parameters :
    ------------
    IRs_array : numpy array
        array of the monophonic impulse responses (IRs) to be studied
        
    IRs_number : integer
        number of impulse responses studied in the same time
        
    sample_rate : int
        sample rate in Hertz of the studied signal
        
    analysis_name : string
        name of the filters' set under study
        
    the_path : pathlib.PATH
       path for the plot of the linear spectrum
       
    x_limits: list of integers
        list defining the left and right frequencies to plot.
        default list: x_limits = [0, 22050]
       
    the_language : string
        if equal to "french" the labels and titles are written in French, 
        otherwise in English
       
    min_value : float, optional
        minimal clipping value for the magnitude used to avoid the problem
        of the singularity of the logarithm for zero value
        
    Returns :
    ---------
    None.
    """
    if IRs_array is None or sample_rate is None:
        return

    # Calculation of the FFT of the signal
    the_length = len(IRs_array[0, :])
    T = 1.0 / sample_rate
    
    half_length = the_length // 2

    freq_array = np.fft.fftfreq(the_length, T)[: half_length]

    # Plot of the magnitude of the spectrum in dB
    plt.figure(figsize=(10, 6))
    
    for k in range(IRs_number):
        dB_amp_spec_array = np.fft.fft(IRs_array[k, :])

        # Calculation of the magnitude of the spectrum in dB
        dB_amp_spec_array = 2.0 / the_length \
            * np.abs(dB_amp_spec_array[: half_length])

        dB_amp_spec_array = 20 * np.log10(dB_amp_spec_array + min_value)
        
        is_odd = np.mod(k, 2)
        
        if is_odd == 1:
            plt.plot(freq_array, dB_amp_spec_array, color='blue')
        else:
            plt.plot(freq_array, dB_amp_spec_array, color='red')
    
    if the_language == "french":
        plt.title('Spectre d\'amplitude (dB): ' + analysis_name)
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude (dB)')

    else:
        plt.title('Magnitude spectrum (dB): ' + analysis_name)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')

        
    plt.xlim(x_limits)
    plt.grid(True)
    
    # save the plot
    if x_limits[0] == 0 and x_limits[1] >= sample_rate // 2:
        fig_name = "dB_spectra_" + analysis_name + ".pdf"

    else:
        fig_name = "dB_spectra_" + analysis_name + "_zoom_"\
            + str(x_limits[0]) + "Hz_" + str(x_limits[1]) + "Hz.pdf"
        
    plt.savefig(the_path / fig_name)

    # show the plot after saving or there will be nothing saved in the file
    plt.show()


# ----------
def plot_logx_dB_spectra(IRs_array, IRs_number, sample_rate, 
                         analysis_name, the_path, x_limits=[0, 22050], 
                         the_language="", min_value=1e-10):
    """  
    plot_logx_dB_spectra(IRs_array, IRs_number, sample_rate, analysis_name, 
                         the_path, x_limits, the_language, min_value)
    
    Calculates and plots the dB magnitude of the spectrum using
    the defined parameters and a logarithmic axis for the frequencies.

    Parameters :
    ------------
    IRs_array : numpy array
        array of the monophonic impulse responses (IRs) to be studied
        
    IRs_number : integer
        number of impulse responses studied in the same time
        
    sample_rate : int
        sample rate in Hertz of the studied signal
        
    analysis_name : string
        name of the filters' set under study
        
    the_path : pathlib.PATH
       path for the plot of the linear spectrum
       
    x_limits: list of integers
        list defining the left and right frequencies to plot.
        default list: x_limits = [0, 22050]
       
    the_language : string
        if equal to "french" the labels and titles are written in French, 
        otherwise in English
       
    min_value : float, optional
        minimal clipping value for the magnitude used to avoid the problem
        of the singularity of the logarithm for zero value
        
    Returns :
    ---------
    None.
    """
    if IRs_array is None or sample_rate is None:
        return

    # Calculation of the FFT of the signal
    the_length = len(IRs_array[0, :])
    T = 1.0 / sample_rate
    
    half_length = the_length // 2

    freq_array = np.fft.fftfreq(the_length, T)[: half_length]

    # Plot of the magnitude of the spectrum in dB
    plt.figure(figsize=(10, 6))
    
    for k in range(IRs_number):
        dB_amp_spec_array = np.fft.fft(IRs_array[k, :])

        # Calculation of the magnitude of the spectrum in dB
        dB_amp_spec_array = 2.0 / the_length \
            * np.abs(dB_amp_spec_array[: half_length])

        dB_amp_spec_array = 20 * np.log10(dB_amp_spec_array + min_value)
        
        is_odd = np.mod(k, 2)
        
        if is_odd == 1:
            plt.semilogx(freq_array, dB_amp_spec_array, color='blue')
        else:
            plt.semilogx(freq_array, dB_amp_spec_array, color='red')
    
    if the_language == "french":
        plt.title('Spectre d\'amplitude (dB): ' + analysis_name)
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude (dB)')

    else:
        plt.title('Magnitude spectrum (dB): ' + analysis_name)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')

        
    plt.xlim(x_limits)
    plt.grid(True)
    
    # save the plot
    if x_limits[0] == 0 and x_limits[1] >= sample_rate // 2:
        fig_name = "logX_dB_spectra_" + analysis_name + ".pdf"

    else:
        fig_name = "logX_dB_spectra_" + analysis_name + "_zoom_"\
            + str(x_limits[0]) + "Hz_" + str(x_limits[1]) + "Hz.pdf"
        
    plt.savefig(the_path / fig_name)

    # show the plot after saving or there will be nothing saved in the file
    plt.show()


