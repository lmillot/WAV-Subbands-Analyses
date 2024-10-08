#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script_name :       test_wav_writing_dev.py

creation date:      26/09/2024, 17h26
modification date:  29/09/2024, 11h29

@author: Laurent Millot
"""


import numpy as np
import struct

from pathlib import Path




# ----------
def create_wav_file(file_name, file_path, sample_rate, format_string, 
                    channels_number, samples_number):
    """
    file_handler, the_position = \
        create_wav_file(file_name, file_path, sample_rate, format_string, 
                        channels_number, samples_number)

    Create a new WAV file with the specified parameters, write the header
    to the file and return a file handler and the current position within
    the file.

    Parameters:
    -----------
    file_name (str): The name of the file.
    
    file_path (Path): The path to the file.
    
    sample_rate (int): The sample rate.
    
    format_string (str): The format string ('i16', 'i24', 'i32', 'f32').
    
    channels_number (int): The number of channels.
    
    samples_number (int): The number of samples per channel.

    Returns:
    --------
    file_handler (file object): The file handler.
    
    the_position (int): The current position in the file.

    Example:
    file_handler, the_position = \
        create_wav_file("example.wav", Path("/path/to/directory"), 44100,
                        "f32", 2, 1000)
    """
    sample_rate = int(sample_rate)

    file_path = Path(file_path) / file_name
    file_handler = open(file_path, 'wb')

    # Write the header
    file_handler.write(b'RIFF')
    
    # Placeholder for file size
    file_handler.write(b'\x00\x00\x00\x00') 
    
    file_handler.write(b'WAVE')
    file_handler.write(b'fmt ')
    
    # Size of the format chunk
    file_handler.write(b'\x10\x00\x00\x00')
        
    # Write the audio format (3 = IEEE float)
    if format_string == 'f32':
        file_handler.write(b'\x03\x00')
    else:
        file_handler.write(b'\x01\x00') # PCM format
    
    file_handler.write(channels_number.to_bytes(2, 'little'))
    file_handler.write(sample_rate.to_bytes(4, 'little'))
    
    # Byte rate
    the_byte_rate = (sample_rate * channels_number * int(format_string[1:])\
                     // 8).to_bytes(4, 'little')
    file_handler.write(the_byte_rate) 
    
    # Block align
    block_align = (channels_number * int(format_string[1:])\
                   // 8).to_bytes(2, 'little')
    file_handler.write(block_align) 

    # Bits per sample
    file_handler.write((int(format_string[1:])).to_bytes(2, 'little')) 
    file_handler.write(b'data')
    
    # Placeholder for data size
    file_handler.write(b'\x00\x00\x00\x00') 

    the_position = file_handler.tell()
    
    return file_handler, the_position


# ----------
def close_wav_file(file_handler, the_position):
    """
    close_wav_file(file_handler, the_position)
    
    Update the header of the WAV file to reflect the actual size
    of the data, then close the file.

    Parameters:
    file_handler (file object): The file handler.
    the_position (int): The current position in the file.
    """
    # Update the file size in the header
    file_size = the_position - 8
    file_handler.seek(4)
    file_handler.write(file_size.to_bytes(4, 'little'))

    # Update the data size in the header
    data_size = the_position - 44
    file_handler.seek(40)
    file_handler.write(data_size.to_bytes(4, 'little'))

    # Close the file
    file_handler.close()


# ----------
def float_normalize(the_float_array, max_value):
    
    the_max = np.max(the_float_array)

    return the_float_array / the_max * max_value


# ----------
def float_to_int(the_float, the_format):
    
    if the_format == "i16":
        bytes_number = 15
    
    elif the_format == "i24":
        bytes_number = 23
        
    elif the_format == "i32":
        bytes_number = 31

    the_scale = 2 ** bytes_number
    the_float = the_float * the_scale
    the_float = np.clip(the_float, -the_scale - 1, the_scale)
    
    return the_float


# ----------
def write_data_to_file(file_handler, the_position, format_string, sig_array,
                       channels_number, samples_number):
    """
    file_handler, the_position = \
        write_data_to_file(file_handler, the_position, format_string, 
                           sig_array, channels_number, samples_number)
        
    Write data to the WAV file. The data is expected to be a numpy array
    of floats.

    Parameters:
    -----------
    file_handler (file object): The file handler.
    
    the_position (int): The current position in the file.
    
    format_string (str): The format string ('i16', 'i24', 'i32', 'f32').
    
    sig_array (numpy.ndarray): The data to write to the file. The array
    can have one or two channels.

    channels_number (int) : number of channels.
    
    samples_number (int) : number of samples per channel.

    Returns:
    --------
    file_handler (file object): The updated file handler.
    the_position (int): The updated position in the file.

    Example:
    # For mono data
    data = np.random.rand(1000).astype(np.float32)
    file_handler, the_position = \
        write_data_to_file(file_handler, the_position, 'f32', data, 1, 1000)

    # For stereo data
    data = np.random.rand(2, 1000).astype(np.float32)
    file_handler, the_position = \
        write_data_to_file(file_handler, the_position, 'f32', data, 2, 1000)
    """

#     """
#     the_format: "f" for f32, "h" for i16, "i" for i32
#     data formatting is made within this function

#     needed data format for wav writing:
#     - f32: 32-bit signed float, 
#     not always within [-1., 1.[
        
#     - i32: 32-bit signed integer 
#     within [-2**31, 2**31 - 1]
    
#     - i16: 16-bit signed integers 
#     within [-2**15, 2**15 - 1]
#     """
    

    # need some optimization...
    # Write data to file
    file_handler.seek(the_position)
    
    if channels_number == 1:
        if format_string == "f32":
            for i in range(0, samples_number):
                file_handler.write(struct.pack("<f", sig_array[i]))

        elif format_string == "i16":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i], format_string)
                file_handler.write(struct.pack("<h", 
                                               the_sample.astype(np.int16)))
                
        elif format_string == "i32":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i], format_string)
                file_handler.write(struct.pack("<i", 
                                               the_sample.astype(np.int32)))
                
        elif format_string == "i24":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i], format_string)
                the_sample = the_sample.astype(np.int32)
                the_sample = struct.pack("<i", the_sample)
                file_handler.write(the_sample[0: 3])

    elif channels_number == 2:        
        # print()
        # print(f"sig_array.shape: {sig_array.shape}")        
        # print(f"samples_number: {samples_number}")
        # print()

        if format_string == "f32":
            for i in range(0, samples_number):                  
                file_handler.write(struct.pack("<f", sig_array[i][0]))
                
                file_handler.write(struct.pack("<f", sig_array[i][1]))
                
        elif format_string == "i16":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i][0], format_string)
                file_handler.write(struct.pack("<h", 
                                               the_sample.astype(np.int16)))
                
                the_sample = float_to_int(sig_array[i][1], format_string)
                file_handler.write(struct.pack("<h", 
                                               the_sample.astype(np.int16)))
                 
        elif format_string == "i32":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i][0], format_string)
                file_handler.write(struct.pack("<i", 
                                               the_sample.astype(np.int32)))
                
                the_sample = float_to_int(sig_array[i][1], format_string)
                file_handler.write(struct.pack("<i", 
                                               the_sample.astype(np.int32)))

        elif format_string == "i24":
            for i in range(0, samples_number):
                the_sample = float_to_int(sig_array[i][0], format_string)
                the_sample = the_sample.astype(np.int32)
                the_sample = struct.pack("<i", the_sample)
                file_handler.write(the_sample[0: 3])

                the_sample = float_to_int(sig_array[i][1], format_string)
                the_sample = the_sample.astype(np.int32)
                the_sample = struct.pack("<i", the_sample)
                file_handler.write(the_sample[0: 3])

    the_position = file_handler.tell()
    
    return file_handler, the_position


# ----------
def create_and_write_wav_file(file_name, file_path, sample_rate, 
                              format_string, sig_array):
    """
    create_and_write_wav_file(file_name, file_path, sample_rate, 
                              format_string, sig_array)
    
    Create a new WAV file, write data to it, and close the file.

    Parameters:
    file_name (str): The name of the file.
    file_path (Path): The path to the file.
    sample_rate (int): The sample rate.
    format_string (str): The format string ('i16', 'i24', 'i32', 'f32').
    sig_array (numpy.ndarray): The data to write to the file. The array 
    can have one or two channels.

    Example:
    data = np.random.rand(2, 1000).astype(np.float32)
    create_and_write_wav_file("example.wav", Path("/path/to/directory"),
                              44100, "f32", data)
    """
    if sig_array.ndim == 1:
        channels_number = 1
        samples_number = len(sig_array)
    
    else:
        samples_number = sig_array.shape[0]
        channels_number = sig_array.shape[1]

    file_handler, the_position = \
        create_wav_file(file_name, file_path, sample_rate, format_string, 
                            channels_number, samples_number)
     
    file_handler, the_position = \
        write_data_to_file(file_handler, the_position, format_string, 
                           sig_array, channels_number, samples_number)
        
    close_wav_file(file_handler, the_position)
