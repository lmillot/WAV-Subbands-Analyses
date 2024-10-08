# -*- coding: utf-8 -*-
"""
name:       tools_filters_ids_filters_no_plot.py

creation date:      14/10/2016, 15h51
modification date:  28/09/2024, 13h11

@author: Millot Laurent
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import kaiserord, firwin, freqz

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls
import Sub_ToBo.tools_wav.tools_wav_write as wvwrtTls


# ----------
def determine_Kaiser_parameters(ripple_dB, width_Hz, nyquist_rate=22050):

    width = width_Hz / nyquist_rate

    ir_length, beta = kaiserord(ripple_dB, width)

    # force an odd number of coefficients
    if ir_length % 2 == 0:
        ir_length = ir_length - 1

    return ir_length, beta


# ----------
def calculate_spectrum_max(ir_array, nyquist_rate, left_cutoff, 
                           right_cutoff, fft_length=2**15):

    _, y_array = freqz(ir_array, worN=fft_length)
    y_array = np.absolute(y_array)

    max_y = max(y_array)

    return max_y


# ----------
def plot_gain(ir_array, the_path, nyquist_rate, left_cutoff, right_cutoff, 
              I_plot=False, fft_length=2**15, clip_value=1e-10):

    w_array, y_array = freqz(ir_array, worN=fft_length)
    y_array = np.abs(y_array)

    max_y = max(y_array)

    ir_array = ir_array / max_y

    y_array = 20 * np.log10(y_array.clip(clip_value) / max_y)
    
    if I_plot:
        plt.figure(0)
        plt.plot(w_array/ np.pi * nyquist_rate, y_array, linewidth=2)
        plt.xlabel("Frequency (Hz)'")
        plt.title("Gain (relative dB)")

        plt.ylim(-120.0, 10.0)
        
        if left_cutoff == 0:
            plt.xlim(0, right_cutoff * 1.2)
        else:
            if right_cutoff == nyquist_rate:
               plt.xlim(left_cutoff * 0.9, nyquist_rate)
            else:
                plt.xlim(left_cutoff * 0.9, right_cutoff * 1.1)
        plt.grid(True)
        
        plt.savefig(the_path, format="pdf")
        
        plt.show()

    return max_y


# ----------
def determine_lowpass_filter(ir_length, beta, left_cutoff, right_cutoff,
                             nyquist_rate=22050):

    cutoff = left_cutoff / nyquist_rate
    ir_array = firwin(ir_length, cutoff, window=("kaiser", beta))

    max_value = calculate_spectrum_max(ir_array, nyquist_rate,
                                       left_cutoff, right_cutoff)

    ir_array = ir_array / max_value

    return ir_array


# ----------
def create_low_pass_fir_filter(sample_rate, cutoff_Hz, ripple_dB=80.0,  
                               width_Hz=5.0, fft_length=2**15):

    nyquist_rate = sample_rate / 2.0

    ir_length, beta = determine_Kaiser_parameters(ripple_dB,
                                                  width_Hz, nyquist_rate)

    ir_array = determine_lowpass_filter(ir_length, beta, cutoff_Hz,True, 
                                        nyquist_rate)

    return ir_array


# ----------
def generate_ids_filters_set(ids_filters_main_folder, current_mapping, 
                             analysis_name, sample_rate, ripple_dB=80.0, 
                             width_Hz=5.0):

    format_string = "f32"
    
    subbands_limits_array = \
        current_mapping.subbands_frequencies_array

    subbands_number = current_mapping.subbands_number

    nyquist_rate = sample_rate / 2
    ir_length, beta = determine_Kaiser_parameters(ripple_dB, width_Hz, 
                                                  nyquist_rate)

    tau = int((ir_length - 1) / 2)

    h1 = np.zeros(ir_length)
    h1[tau] = 1

    filters_subfolder_name = "h_" + analysis_name + "_"\
        + str(int(sample_rate/100)) + "_"\
        + str(int(ir_length))

    filters_folder_path = ids_filters_main_folder / filters_subfolder_name

    fldrTls.create_new_subfolder(filters_folder_path)

    for sb_index in range(0, subbands_number-1):
        the_index = subbands_number - sb_index

        left_cutoff = subbands_limits_array[the_index-1]
        right_cutoff = subbands_limits_array[the_index]

        h = determine_lowpass_filter(ir_length, beta,
                                     left_cutoff, right_cutoff,
                                     nyquist_rate)

        h1 = h1 - h

        the_filename = str(left_cutoff) + "_" + str(right_cutoff) + ".wav"
        
        # fig_name = the_filename[:-3] + "pdf"
        # the_path = ids_filters_main_folder / fig_name
        # plot_gain(h1, the_path, nyquist_rate, left_cutoff, 
        #           right_cutoff, True)

        # save h1
        wvwrtTls.create_and_write_wav_file(the_filename, filters_folder_path,
                                           sample_rate, format_string, h1)
        
        h1 = h

    the_filename = str(0) + "_" + str(left_cutoff) + ".wav"

    # save h1    
    wvwrtTls.create_and_write_wav_file(the_filename, filters_folder_path, 
                                       sample_rate, format_string, h1)

    # fig_name = the_filename[:-3] + "pdf"
    # the_path = ids_filters_main_folder / fig_name
    # plot_gain(h1, the_path, nyquist_rate, left_cutoff, right_cutoff, True)
    