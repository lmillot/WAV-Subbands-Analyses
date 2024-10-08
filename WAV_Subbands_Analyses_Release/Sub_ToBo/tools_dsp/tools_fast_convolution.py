#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
name:               tools_fast_convolution.py

creation date:      18/04/2021, 21h25
modification date:  14/06/2024, 10h54

@author: laurentmillot
"""


import numpy as np


# --------------------
def is_mono(the_array):
    
    """
    tests if an array is monophonic (just one row and 
    several columns)

    the_test = is_mono(the_array)

    Parameters
    ----------
    the_array : array of integers or floats

    Returns
    -------
    the_test : boolean
        True if the input array is monophonic,
        False if the input array is stereophonic.

    """

    the_dim = the_array.ndim

    if the_dim == 1:
        return True
    else:
        return False


# --------------------
def array_properties(the_array):
    
    """
    gives the number of rows and of columns for a given array
    permits to avoir the diffenrence of definition shape 
    property for arrays according if they are 1D or 2D (ND) 
    arrays

    the_rows, the_size = array_properties(the_array)

    Parameters
    ----------
    the_array : array of integers or floats
        array either monophonic ou stereophonic

    Returns
    -------
    the_rows : integer
        number of rows of the input array

    the_size : integer
        number of columns

    """

    if is_mono(the_array) is True:
        the_size = len(the_array)
        the_rows = 1

    else:
        the_rows, the_size = the_array.shape

    return the_rows, the_size


# --------------------
def next_2power(the_number):
    
    """
    calculates the next power of 2 for a given number

    the_2power = next_2power(the_number)

    Parameters
    ----------
    the_number : either an integer or a float

    Returns
    -------
    the_2power : TYPE
        returns the power of 2 just greater than the input 
        number

    """

    the_2power = 64

    while the_2power < the_number:
        the_2power = 2 * the_2power

    return the_2power


# --------------------
def fast_convo_mono(input_array, ir_array, min_fft_size=8192):
    """
    fast convolution of a monophonic input by a monophonic 
    impulse response

    output_array = fast_convo_mono(input_array, ir_array)

    Parameters
    ----------
    input_array : monophonic array of floats or integers

    ir_array : monophonic array of floats or integers

    Returns
    -------
    output_array : monophonic array of floats or integers
        returns the convolution of monophonic input_array by
        monophonic ir_array

    """

    input_length = np.size(input_array)
    ir_length = np.size(ir_array)

    output_length = input_length + ir_length - 1
    fft_length = next_2power(output_length)
    fft_length = np.max(np.array([fft_length, min_fft_size]))

    input_array = np.fft.fft(input_array, fft_length)
    ir_array = np.fft.fft(ir_array, fft_length)

    input_array = input_array * ir_array
    del ir_array

    input_array = np.fft.ifft(input_array)

    # on ne conserve que les output_length premiers samples
    input_array = input_array[:output_length]

    # on force les valeurs à être réelles
    input_array = np.real(input_array)

    return input_array


# --------------------
def fast_convo_stereo(input_array, ir_array, min_fft_size=8192):
    
    """
    fast convolution of a stereophonic input by a monophonic 
    impulse response

    output_array = fast_convo_stereo(input_array, ir_array)

    Parameters
    ----------
    input_array : stereophonic array of floats or integers

    ir_array : monophonic array of floats or integers

    Returns
    -------
    output_array : stereophonic array of floats or integers

        returns the convolution of stereophonic input_array by
        monophonic ir_array

    """

    _, input_length = input_array.shape
    ir_length = np.size(ir_array)

    output_length = input_length + ir_length - 1
    fft_length = next_2power(output_length)
    fft_length = np.max(np.array([fft_length, min_fft_size]))

    input_array = input_array[0, :] + 1j * input_array[1, :]

    input_array = np.fft.fft(input_array, fft_length)
    ir_array = np.fft.fft(ir_array, fft_length)

    input_array = input_array * ir_array
    del ir_array

    input_array = np.fft.ifft(input_array)

    # on ne conserve que les output_length premiers samples
    input_array = input_array[:output_length]

    # on force les valeurs à être réelles
    input_array = np.array([np.real(input_array), np.imag(input_array)])

    return input_array


# --------------------
def fast_convo(input_array, ir_array, min_fft_size=8192):
    
    """
    fast convolution of an input signal, either monophonic 
    or stereophonic, by a monophonic impulse response

    output_array = fast_convo(input_array, ir_array)

    Parameters
    ----------
    input_array : stereophonic or monophonic array of floats
    or integers
    input signal which will be filtered

    ir_array : monophonic array of floats or integers
    impulse array related to the chosen filter

    Returns
    -------
    output_array : stereophonic or monophonic array of floats
    or integers

        returns the convolution of either monophonic or 
        stereophonic input signal by monophonic impulse
        response

        enforces impulse response to be monophonic
        so, to use a stereophonic impulse response 
        with a monophonic input,
        just permutate input_array and ir_array

    """

    if not is_mono(ir_array):
        ir_array = ir_array[0, :]

    if is_mono(input_array):
        return fast_convo_mono(input_array, ir_array, min_fft_size)

    else:
        return fast_convo_stereo(input_array, ir_array, min_fft_size)
