#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name:       tools_wav_read.py

creation date:      26/09/2024, 12h33
modification date:  28/09/2024, 19h27

@author: Millot Laurent


    header = {
            "chunk_ID": "",
            "chunk_size": 0,
            "format": "",
            "subchunk1_ID": "",
            "subchunk1_size": 0,
            "audio_format": 0,
            "channels_number": 0,
            "sample_rate": 0,
            "byte_rate": 0,
            "block_align": 0,
            "bits_per_sample": 0,
            "data_position": 0,
            "subchunk2_ID": "",
            "Subchunk2_size": 0,
            "filename": filename,
            "samples_number": 0}
"""


import pathlib as pth
import numpy as np
import struct


# ----------
def print_wav_header(header):
    """
    print_wav_header(header)

    Parameters
    ----------
    header : dictionary
        a header of a valid wav file

    Returns
    -------
    None.
    
    display all the fields of the wav file's header

    """
    
    print("-" * 10)
    print("- wav header -")
    print("-" * 10)
    print()

    for key in header.keys():
        print("%s: " % (key), 
              header[key])


# ----------
def _is_wav_file(test_string, I_debug=True):
    """
    bool = _is_wav_file(test_string, I_debug=True)

    Parameters
    ----------
    test_string : binary string
        DESCRIPTION.
        
    I_debug : boolean, optional
        if True, the detail of the test result is displayed. 
        The default is True.

    Returns
    -------
    bool
        if true, there is a valid binary string in the file so it is a valid
        wav file. if False, it is not a valid wav file.

    """

    if test_string == b"RIFF":
        if I_debug is True:
            print("RIIF chunkID has been found!")
        return True
    else:
        return False


# ----------
def _search_subchunks(the_file_handler, I_debog):
    """
    fmt_chunk_location, data_chunk_location = \
        _search_subchunks(the_file_handler, I_debog)

    Parameters
    ----------
    the_file_handler : file handler
        handler for the wav file under study
        
    I_debog : boolean
        if True, the details of all the found chunks and subchunks will be
        displayed

    Returns
    -------
    fmt_chunk_location : int
        location in the wav file of the beginning of the format chunk
        
    data_chunk_location : int
        location in the wav file of the beginning of the data chunk

    """
    
    # Localize all subchunks and search for fmt 
    # and data subchunks
    chunks_list = []
    data_chunk_location = 0
    fmt_chunk_location = 0
    found_data_subchunk = 0
    found_fmt_subchunk = 0

    the_file_handler.seek(0, 2)  # Seek to end of file
    file_size = the_file_handler.tell()

    # skip the RIFF header
    next_subchunk_location = 12   
    # chunk_ID(4) + chunk_size(4) + "WAVE"(4)

    while ((found_fmt_subchunk == False) or (found_data_subchunk == False)):
        # Read subchunk header
        the_file_handler.seek(next_subchunk_location)
        buffer = the_file_handler.read(8)

        if buffer[0:4] == b"fmt ":
            fmt_chunk_location = next_subchunk_location
                
            found_fmt_subchunk = True

            if I_debog == True:
                print("- 'fmt ' subchunk found!")

        if buffer[0:4] == b"data":
            data_chunk_location = next_subchunk_location
                
            found_data_subchunk = True

            if I_debog == True:
                print("- 'data' subchunk found!")

        chunks_list.append(buffer[0:4])

        next_subchunk_location += (8 + struct.unpack("<I", buffer[4:8])[0])

        if next_subchunk_location >= file_size:
            break

    if I_debog == True:
        print()
        print()
        print("sub chunks list:")

        for x in chunks_list:
            print("- ", x)

        print()
        print()

    if ((found_fmt_subchunk == True) and (found_data_subchunk == True)):
        if I_debog == True:
            print("fmt_chunk_location: ", fmt_chunk_location)
            
            print("data_chunk_location:",  data_chunk_location)
            print()

        return fmt_chunk_location, data_chunk_location

    else:
        print("Error: neither 'fmt' nor 'data' subchunks have been found...")
        print("This is not a valid WAV file!")
        return -1


# ----------
def _get_header(the_file_handler, fmt_chunk_location, data_chunk_location,
                chunk_size, filename):
    """
    header = _get_header(the_file_handler, fmt_chunk_location, 
                         data_chunk_location, chunk_size, filename)    

    Parameters
    ----------
    the_file_handler : file handler
        file handler related to an open wav file
        
    fmt_chunk_location : int
        position of the beginning of the format chunk in the wav file
        
    data_chunk_location : int
        position of the beginning of the data chunk in the wav file
        
    chunk_size : int
        size of the header in the wav file
        
    filename : string
        filename of the studied wav file

    Returns
    -------
    header : TYPE
    
        structure of the dictionary which be returned:
        
        header = {
                "chunk_ID": "",
                "chunk_size": 0,
                "format": "",
                "subchunk1_ID": "",
                "subchunk1_size": 0,
                "audio_format": 0,
                "channels_number": 0,
                "sample_rate": 0,
                "byte_rate": 0,
                "block_align": 0,
                "bits_per_sample": 0,
                "data_position": 0,
                "subchunk2_ID": "",
                "Subchunk2_size": 0,
                "filename": filename,
                "samples_number": 0}

    """

    header = {
            "chunk_ID": "",
            "chunk_size": 0,
            "format": "",
            "subchunk1_ID": "",
            "subchunk1_size": 0,
            "audio_format": 0,
            "channels_number": 0,
            "sample_rate": 0,
            "byte_rate": 0,
            "block_align": 0,
            "bits_per_sample": 0,
            "data_position": 0,
            "subchunk2_ID": "",
            "Subchunk2_size": 0,
            "filename": filename,
            "samples_number": 0}

    # get chun_sSize
    the_file_handler.seek(0, 0)
    buffer = the_file_handler.read(12)
    
    header["chunk_ID"] = buffer[0:4]
    header["chunk_size"] = struct.unpack("<I", buffer[4:8])[0]
        
    header["format"] = buffer[8:12]

    # get subchunk1_size
    the_file_handler.seek(fmt_chunk_location, 0)
    buffer = the_file_handler.read(24)
    
    header["subchunk1_ID"] = buffer[0:4]
    
    header["subchunk1_size"] = struct.unpack("<I", buffer[4:8])[0]

    header["audio_format"] = struct.unpack("<h", buffer[8:10])[0]

    channels_number = struct.unpack("<h", buffer[10:12])[0]
    
    header["channels_number"] =  channels_number

    header["sample_rate"] = struct.unpack("<I", buffer[12:16])[0]

    header["byte_rate"] = struct.unpack("<I", buffer[16:20])[0]

    header["block_align"] = struct.unpack("<h", buffer[20:22])[0]

    bits_per_sample = struct.unpack("<h", buffer[22:24])[0]
    
    header["bits_per_sample"] = bits_per_sample

    header["data_position"] = data_chunk_location

    the_file_handler.seek(data_chunk_location, 0)
    buffer = the_file_handler.read(8)

    header["subchunk2_ID"] = buffer[0:4]

    sub_chunk2_size = struct.unpack("<I", buffer[4:8])[0]
    
    header["subchunk2_size"] = sub_chunk2_size

    samples_number = sub_chunk2_size // (channels_number * bits_per_sample // 8)
        
    header["samples_number"] = int(samples_number)        

    return header


# ----------
def _get_filename(the_path):
    
    the_filename = str(the_path)
    the_filename = the_filename.split("/")[-1]


# ----------
def open_wav(the_path, header):
    """
    the_file_handler, the_position = open_wav(the_path, header)

    Parameters
    ----------
    the_path: Pathlib
        complete path to the WAV file.
        
    header : dictionary
        a header of a valid wav file.
        
    Returns
    -------
    the_file_handler : a file handler
        file handler related to an open wav file
        
    the_position : int
        index of the beginning of the data in the WAV file
    """
    try:
        if not isinstance(the_path, pth.Path):
            the_path = pth.Path(the_path)

        # open the wav file in binary reading mode
        the_file_handler = open(the_path, "rb")

        # go to the beginning of the audio data in the WAV file
        the_file_handler.seek(header["data_position"] + 8)
        data_beg_index = the_file_handler.tell()
        
        return the_file_handler, data_beg_index

    except OSError:
        print("cannot open the file...")
        return -1


# ----------
def _close_wav(the_file_handler):
    """
    _close_wav(the_file_handler)

    Parameters
    ----------
    the_file_handler : a file handler
        file handler related to an open wav file

    Returns
    -------
    None.

    """
    
    the_file_handler.close()


# ----------
def _read_wav_header(the_path, I_debog=True):
    """
    the_file_handler, header = \
        _read_wav_header(the_path, I_debog=True)

    Parameters
    ----------
    the_path : Pathlib
        complete path to the WAV file. 
        
    I_debog : TYPE, optional
        DESCRIPTION. The default is True.

    Returns
    -------
    the_file_handler:
        file handler to perform all the operations before closing
        
    header:
        dictionary with all the fields found in the header of the wav file

    
    CAUTION: 
    - open the file, read the header and do not close the file when there is
    no encountered problem during the header's reading
    - manual closing may be used!
    """

    # open the chosen wav file
    try:
        if not isinstance(the_path, pth.Path):
            the_path = pth.Path(the_path)

        # open the wav file in binary reading mode
        the_file_handler = open(the_path, "rb")

        # ---- read chunk_ID
        chunk_ID = the_file_handler.read(4)

        if _is_wav_file(chunk_ID, I_debog):
            # --- read chunk_size
            buffer = the_file_handler.read(4)

            chunk_size = struct.unpack("<I", buffer)[0]

            total_size = chunk_size + 8

            if I_debog == True:
                print("file total size: ", total_size, "bytes")
                print()

            format_chunk = the_file_handler.read(4)

            if format_chunk == b"WAVE":
                if I_debog == True:
                    print("- 'WAVE' chunk found!")

                the_results = _search_subchunks(the_file_handler, I_debog)

                if the_results != -1:
                    fmt_chunk_location = the_results[0]
                    data_chunk_location = the_results[1]

                    the_filename = _get_filename(the_path)
                    
                    header = \
                        _get_header(the_file_handler, fmt_chunk_location,
                                    data_chunk_location, chunk_size, 
                                    the_filename)

                    if I_debog == True:
                        print_wav_header(header)

                    return the_file_handler, header

                else:
                    return -1

            else:
                print("Error: this is not a valid WAV file")
                return -1
        else:
            print("Sorry, this is not a valid wav file...")
            _close_wav(the_file_handler)
            return -1

    except OSError:
        print("cannot open the file...")
        return -1


# ----------
def read_wav_header(the_path):
    """
    header = read_wav_header(the_path)

    Parameters
    ----------       
    the_path : Pathlib
        complete path to acces to the wav file

    Returns
    -------
    header : dictionary
        complete wav header

        header fields constituting the wav header are 
        the following:
        - chunk_ID
        - chunk_size
        - format
        - subchunk1_ID
        - subchunk1_size
        - audio_format
        - channels_number
        - sample_rate
        - byte_rate
        - block_align
        - bits_per_sample
        - data_position
        - subchunk2_ID
        - subchunk2_size
        - filename
        - samples_number

        wav_header function:
        - manages opening and closing of the wav file
        - can be used simply after loading of the wav_read_tools library

    """

    the_file_handler, header = _read_wav_header(the_path, False)

    the_file_handler.close()

    return header


# ----------
def _what_pcm_type(header):
    """
    pcm_type = _what_pcm_type(header)

    Parameters
    ----------
    header : dictionary
        wav file's header

    Returns
    -------
    pcm_type : string
        according to the audio format of the samples, the returned string
        is i16, i24, i32 or f32
        i for integer representation and f for floats, the number indicates
        the number of bits used to encode each sample
    """
    
    audio_format = header["audio_format"]
    bytes_per_sample = header["bits_per_sample"]
    pcm_type = "i16"

    if audio_format == 3:
        pcm_type = "f32"

    elif audio_format == 1:
        if bytes_per_sample == 16:
            pcm_type = "i16"

        elif bytes_per_sample == 24:
            pcm_type = "i24"

        elif bytes_per_sample == 32:
            pcm_type = "i32"

    else:
        print("This is not an application known wav format...")
        pcm_type = ""

    return pcm_type


# ----------
def _what_dtype(header):
    """
    the_dtype = _what_dtype(header)

    Parameters
    ----------
    header : dictionary
        wav file's header

    Returns
    -------
    the_dtype : string
        string defining the binary format to read the samples
    """
    
    audio_format = header["audio_format"]
    bytes_per_sample = header["bits_per_sample"]
    the_dtype = "<i2"

    if audio_format == 3:
        the_dtype = "float32"

    elif audio_format == 1:
        if bytes_per_sample == 16:
            the_dtype = "<i2"

        elif bytes_per_sample == 24:
            the_dtype = "u1"

        elif bytes_per_sample == 32:
            the_dtype = "<i4"

    else:
        print("Unknown format...")
        the_dtype = ""

    return the_dtype


# ----------
def read_wav_buffer_int(the_file_handler, the_position, block_size, header):
    
    """
    samples_array, the_position =  \
        read_wav_buffer_int(the_file_handler, the_position, block_size, 
                            header)
    
    Parameters
    ----------
    the_file_handler : a wav file pointer over an open wav
        file handler to perform operations inside the WAV file
        
    the_position : int
        reading index where to begin the blocs reading in the wav
        
    block_size : int
        number of samples to be read
        
    header : dictionary
        dictionary built while reading the wav file header

    Returns
    -------
    samples_array: numpy array of int
        array of the samples block read in the wav file
        
    the_position:
        new position index in the wav file just after the last read sample


    CAUTION: no floating point conversion here as the data can be used 
    to generate another wav file without any processing!
    """

    channels_number = header["channels_number"]
    bytes_per_sample = header["bits_per_sample"]

    if header["audio_format"] == 3:
        is_IEEE = True
    else:
        is_IEEE = False

    """
    easier to take into account the non monophonic cases within this function
    as the buffer size is calculated in the monophonic case!
    """
    block_size = np.int32(block_size * channels_number)

    if bytes_per_sample == 8 or bytes_per_sample == 24:
        d_type = "u1"
        bytes_number = 1
    else:
        bytes_number = bytes_per_sample // 8
        d_type = "<i%d" % bytes_number

    if bytes_per_sample == 32 and is_IEEE:
        d_type = "float32"

    # go to the wanted position
    the_file_handler.seek(the_position)

    the_count = block_size

    # as bytes_number has been defined equal to 1
    if bytes_per_sample == 24:
        the_count = block_size * 3

    samples_array = np.fromfile(the_file_handler, dtype=d_type, 
                                count=the_count)

    # needed special processing for i24 wav files
    if bytes_per_sample == 24:
        a = np.empty((len(samples_array) // 3, 4), dtype="u1")
        
        a[:, :3] = samples_array.reshape((-1, 3))
        a[:, 3:] = (a[:, 3 - 1:3] >> 7) * 255
        
        samples_array = a.view("<i4").reshape(a.shape[:-1])

    if channels_number > 1:
        samples_array = samples_array.reshape(-1, channels_number)

    the_position = the_file_handler.tell()

    return samples_array, the_position


# ----------
def read_wav_file_int(the_path, header):

    """
    samples_array = read_wav_file_int(the_path, header)
    
    Parameters:
        the_path : Pathlib
            complete path to acces to the wav file        

        header: the complete wav file's header

    Returns:
        samples_array: numpy array with wav samples
        

    CAUTION:
    - no floating point conversion for the returned samples array
    - may be used for generation of anoter wav file with little or ideally
    without any intermediate operation
    """

    # CAUTION: no floating point conversion here as the data can be used 
    # to generate another wav file !
    
    the_file_handler, _ = open_wav(the_path, header)
    # open(the_path, "rb")

    channels_number = header["channels_number"]
    bytes_per_sample = header["bits_per_sample"]

    if header["audio_format"] == 3:
        is_IEEE = True
    else:
        is_IEEE = False

    # go to the data size position
    the_file_handler.seek(header["data_position"]+4, 0)
    data_size = struct.unpack("<i", the_file_handler.read(4))[0]

    if bytes_per_sample == 8 or bytes_per_sample == 24:
        d_type = "u1"
        bytes_number = 1
    else:
        bytes_number = bytes_per_sample // 8
        d_type = "<i%d" % bytes_number

    if bytes_per_sample == 32 and is_IEEE:
        d_type = "float32"

    samples_array = np.fromfile(the_file_handler, dtype=d_type, 
                                count=data_size//bytes_number)

    # needed special processing for i24 wav files
    if bytes_per_sample == 24:
        a = np.empty((len(samples_array) // 3, 4), dtype="u1")
        
        a[:, :3] = samples_array.reshape((-1, 3))
        a[:, 3:] = (a[:, 3 - 1:3] >> 7) * 255
        
        samples_array = a.view("<i4").reshape(a.shape[:-1])

    if channels_number > 1:
        samples_array = samples_array.reshape(-1, channels_number)

    if bool(data_size & 1):
        the_file_handler.seek(1, 1)

    the_file_handler.close()
    
    return samples_array


# ----------
def pcm2float(samples_array, pcm_type):
    """
    samples_array = pcm2float(samples_array, pcm_type)    

    Parameters
    ----------
    samples_array : numpy array
        array of int numbers to be converted in float numbers with the
        appropriate normalization factor
        
    pcm_type : string
        string defining the format of the samples in the array: i16, i24, i32
        or f32 (no normalization processed in this case)

    Returns
    -------
    samples_array : numpy array
        array of float numbers
    """

    if pcm_type == "f32":
        normalization_factor = 1.

    elif pcm_type == "i16":
        normalization_factor = 2 ** 15

    elif pcm_type == "i24":
        normalization_factor = 2 ** 23

    elif pcm_type == "i32":
        normalization_factor = 2 ** 31

    samples_array = np.float32(samples_array) * 1.0 / normalization_factor

    return samples_array


# ----------
def read_wav_file(the_path, header):

    """
    samples_array = read_wav_file(the_path, header)
    
    Parameters
    ----------
    the_path : Pathlib
            complete path to acces to the wav file
            
    header: the complete wav file's header

    Returns
    -------
    samples_array: numpy array with wav float samples
    the_position: current position index within the wav file

    CAUTION:
    - may be used to process block operations
    """
    
    samples_array = read_wav_file_int(the_path, header)

    pcm_type = _what_pcm_type(header)

    samples_array = pcm2float(samples_array, pcm_type)

    return samples_array


# ----------
def read_wav_buffer(the_file_handler, the_position, block_size, header):
    """
    samples_array, the_position =  \
        read_wav_buffer(the_file_handler, the_position, block_size, header)
    
    Parameters
    ----------
    the_file_handler: a wav file pointer over an open wav
        
    the_position : int
        reading index where to begin the blocs reading in the wav
        
    block_size : int
        number of samples to be read
        
    header : dictionary
        dictionary built while reading the wav file header

    Returns
    -------
    samples_array: numpy array of float
        array of the samples block read in the wav file
        
    the_position:
        new position index in the wav file just after the last read sample

    CAUTION: floating point conversion is performed!
    """

    
    samples_array, the_position = \
        read_wav_buffer_int(the_file_handler, the_position, block_size, 
                            header)

    pcm_type = _what_pcm_type(header)

    samples_array = pcm2float(samples_array, pcm_type)

    return samples_array, the_position
