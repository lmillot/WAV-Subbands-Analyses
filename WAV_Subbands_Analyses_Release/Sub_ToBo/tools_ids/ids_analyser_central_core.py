#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script:             ids_analyser_central_core.py

creation date:      13/08/2024, 19h14
modification date:  07/10/2024, 18h19

@author: Millot
"""



import numpy as np

import Sub_ToBo.tools_dsp.tools_fast_convolution as cnvTls
import Sub_ToBo.tools_wav.tools_wav_read as wvrdTls
import Sub_ToBo.tools_ids.csv_ids_profiles_tools as csvTls
import Sub_ToBo.tools_ids.ids_profiles_tools as prflTls


     
# ----------
def bloc_energy_cumul_mono(the_array):
    
        return sum([x**2 for x in the_array])


# ----------
def bloc_energy_cumul_stereo(the_array):
    
    return np.array([sum([x**2 for x in the_array[0]]),
                     sum([x**2 for x in the_array[1]])])


# ----------
def analyse_one_block_stereo(filters_path, filters_name, input_array, 
                             current_subband_index):

    if current_subband_index == 0:
        orig_energy_cumul = bloc_energy_cumul_stereo(input_array)

    # Read the filter
    file_path = filters_path / filters_name
    ir_array = wvrdTls.all_read_wav_samples_float(file_path)
    tau = int((len(ir_array) - 1) / 2)
    
    # Apply the filter
    convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)
    convo_array = convo_array[:, tau:-tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = bloc_energy_cumul_stereo(convo_array)

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul


# ----------
def analyse_one_block_mono(filters_path, filters_name, input_array, 
                           current_subband_index):

    if current_subband_index == 0:
        orig_energy_cumul = bloc_energy_cumul_mono(input_array)

    # Read the filter
    file_path = filters_path / filters_name
    ir_array = wvrdTls.all_read_wav_samples_float(file_path)
    tau = int((len(ir_array) - 1) / 2)

    # Apply the filter
    convo_array = cnvTls.fast_convo_mono(input_array, ir_array)

    convo_array = convo_array[tau:-tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = bloc_energy_cumul_mono(convo_array)

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul


# ----------
def analyse_one_file_mono_block(data, header):
    # only on file and one block / monophonic or stereophonic wav file
    
    filters_names_list = data['filters_name_list']
    filters_path = data['filters_path']

    input_file_name = data['input_filename']
    input_path = data['input_path']

    the_path = input_path / input_file_name
    input_array = wvrdTls.all_read_wav_samples_float(the_path)
    
    channels_number = header['num_channels']

    filters_number = len(filters_names_list)
    
    # monophonic case
    if channels_number == 1:
        energies_cumul = np.zeros(filters_number + 1)

        for current_subband_index in range(filters_number):
            filters_name = filters_names_list[current_subband_index]
        
            if current_subband_index == 0:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_block_mono(filters_path, filters_name, 
                                           input_array, current_subband_index)

                energies_cumul[-1] = orig_energy_cumul
                energies_cumul[0] = subband_energy_cumul
            else:
                subband_energy_cumul = \
                    analyse_one_block_mono(filters_path, filters_name, 
                                           input_array, current_subband_index)        

                energies_cumul[current_subband_index] = subband_energy_cumul

    # stereophonic case
    else:
        energies_cumul = np.zeros((filters_number + 1, 2))

        for current_subband_index in range(filters_number):
            filters_name = filters_names_list[current_subband_index]
        
            if current_subband_index == 0:
                subband_energy_cumul = \
                    analyse_one_block_stereo(filters_path, filters_name, 
                                             input_array, 
                                             current_subband_index)

                energies_cumul[-1, :] = orig_energy_cumul
                energies_cumul[0, :] = subband_energy_cumul

            else:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_block_stereo(filters_path, filters_name, 
                                             input_array, 
                                             current_subband_index)

                energies_cumul[current_subband_index, :] = \
                    subband_energy_cumul

    return energies_cumul


# ----------
def analyse_one_subband_stereo(filter_name, data, in_path, 
                               current_subband_index, blocks_number, 
                               last_block_length, buffer_length):

    # calculate one subband for long stereophonic wav
    # thus, multi block analyse
    
    filters_path = data['filters_path']

    # Read the filter IR
    filter_path = filters_path / filter_name
    ir_header = wvrdTls.read_wav_header(filter_path)
    ir_array = wvrdTls.read_wav_file(filter_path, ir_header)

    ir_length = len(ir_array)
    Nh1 = ir_length - 1
    tau = int(Nh1 / 2)

    # Open the input signal
    in_header = wvrdTls.read_wav_header(in_path)
    in_handle, in_position = wvrdTls.open_wav(in_path, in_header)

    total_read_samples = 0
    total_written_samples = 0
    
    orig_energy_cumul = np.array([0, 0])
    subband_energy_cumul = np.array([0, 0])

    # buffer used for input reading and output writing
    to_write_array = np.zeros((2, buffer_length))

    # buffer used for the overlapping residue
    to_keep_array = np.zeros((2, Nh1))

    # ---- process first block ----
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, buffer_length, 
                                in_header)

    input_array = input_array.T
    
    _, read_samples_number = input_array.shape

    total_read_samples = total_read_samples + read_samples_number

    if current_subband_index == 0:
        orig_energy_cumul = orig_energy_cumul + \
            bloc_energy_cumul_stereo(input_array)

    # Apply the filter
    # calculate the first bloc array with fast_convo
    convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)

    to_write_array = convo_array[:, : buffer_length]

    # suppress tau samples for the first block
    to_write_array = to_write_array[:, tau:]
        
    # update the residue
    to_keep_array = convo_array[:, buffer_length: ]
    
    # Calculate the energy cumul
    subband_energy_cumul = subband_energy_cumul\
        + bloc_energy_cumul_stereo(to_write_array)

    _, to_write_array_length = to_write_array.shape
    total_written_samples = total_written_samples + to_write_array_length

    if blocks_number > 2:
    # ---- process median blocks ----
        for i in range(2, blocks_number):
            # print(f"block #{i} / {blocks_number}")
            # buffer used for output writing
            to_write_array = np.zeros((2, buffer_length))
            
            # read new block of buffer_length samples
            input_array, in_position =  \
                wvrdTls.read_wav_buffer(in_handle, in_position, buffer_length, 
                                        in_header)

            input_array = input_array.T
                        
            _, read_samples_number = input_array.shape
                
            total_read_samples = total_read_samples + read_samples_number

            if current_subband_index == 0:
                orig_energy_cumul = orig_energy_cumul + \
                    bloc_energy_cumul_stereo(input_array)   

            # Apply the filter
            convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)
                        
            # Manage the overlapping
            to_write_array[:, : Nh1] = convo_array[:, : Nh1]\
                + to_keep_array[:, : ]
                
            to_write_array[:, Nh1: ] = convo_array[:, Nh1: buffer_length]

            to_keep_array = convo_array[:, buffer_length: ]

            # Calculate the energy cumul
            subband_energy_cumul = subband_energy_cumul\
                + bloc_energy_cumul_stereo(to_write_array)

            _, to_write_array_length = to_write_array.shape
            
            total_written_samples = total_written_samples \
                + to_write_array_length
          
    # ---- process the last shorter block ----
    samples_to_be_read = (blocks_number - 1) * buffer_length \
        + last_block_length

    # Read the last buffer of last_block_length samples
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, last_block_length, 
                                in_header)

    input_array = input_array.T
    
    _, read_samples_number = input_array.shape
    
    in_handle.close()

    total_read_samples = total_read_samples + read_samples_number

    if total_read_samples != samples_to_be_read:
        print("")
        print(f"number of samples to be read: {samples_to_be_read}")
        print(f"number of read samples: {total_read_samples}")
        print("As both numbers should be equal, there is a problem...")
        print("")

    if current_subband_index == 0:
        orig_energy_cumul = orig_energy_cumul \
            + bloc_energy_cumul_stereo(input_array)

    # Manage the overlapping
    convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)

    convo_array[:, : Nh1] = convo_array[:, : Nh1] + to_keep_array[:, :]
    convo_array = convo_array[:, : -tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = subband_energy_cumul + \
        bloc_energy_cumul_stereo(convo_array)

    _, convo_array_length = convo_array.shape
    total_written_samples = total_written_samples + convo_array_length

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul 


# ----------
def analyse_one_subband_mono(filter_name, data, in_path, 
                             current_subband_index, blocks_number, 
                             last_block_length, buffer_length):

    filters_path = data['filters_path']
   
    # calculate one subband for long monophonic wav
    # thus, multi block analyse

    # Read the filter IR
    filter_path = filters_path / filter_name
    ir_header = wvrdTls.read_wav_header(filter_path)
    ir_array = wvrdTls.read_wav_file(filter_path, ir_header)

    ir_length = len(ir_array)
    Nh1 = ir_length - 1
    tau = int(Nh1 / 2)

    # Open the input signal
    in_header = wvrdTls.read_wav_header(in_path)
    in_handle, in_position = wvrdTls.open_wav(in_path, in_header)

    total_read_samples = 0
    total_written_samples = 0
    
    orig_energy_cumul = 0
    subband_energy_cumul = 0

    # buffer used for input reading and output writing
    to_write_array = np.zeros(buffer_length)

    # buffer used for the overlapping residue
    to_keep_array = np.zeros(Nh1)

    # ---- process first block ----
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, buffer_length, 
                                in_header)

    read_samples_number = len(input_array)

    total_read_samples = total_read_samples + read_samples_number

    if current_subband_index == 0:
        orig_energy_cumul = orig_energy_cumul + \
            bloc_energy_cumul_mono(input_array)

    # Apply the filter
    # calculate the first bloc array with fast_convo
    convo_array = cnvTls.fast_convo_mono(input_array, ir_array)

    to_write_array[:] = convo_array[: buffer_length]

    # suppress tau samples for the first block
    to_write_array = to_write_array[tau: ]

    # update the residue
    to_keep_array = convo_array[buffer_length: ]

    # Calculate the energy cumul
    subband_energy_cumul = subband_energy_cumul\
        + bloc_energy_cumul_mono(to_write_array)

    total_written_samples = total_written_samples + len(to_write_array)

    if blocks_number > 2:
    # ---- process median blocks ----
        for i in range(2, blocks_number):
            # buffer used for output writing
            to_write_array = np.zeros(buffer_length)

            # read new block of buffer_length samples
            input_array, in_position =  \
                wvrdTls.read_wav_buffer(in_handle, in_position, buffer_length, 
                                        in_header)

            read_samples_number = len(input_array)
                
            total_read_samples = total_read_samples + read_samples_number

            if current_subband_index == 0:
                orig_energy_cumul = orig_energy_cumul + \
                    bloc_energy_cumul_mono(input_array)   

            # Apply the filter
            convo_array = cnvTls.fast_convo_mono(input_array, ir_array)
            
            # Manage the overlapping
            to_write_array[: Nh1] = convo_array[: Nh1] + to_keep_array[: ]        
            to_write_array[Nh1: ] = convo_array[Nh1: buffer_length]

            to_keep_array = convo_array[buffer_length: ]

            # Calculate the energy cumul
            subband_energy_cumul = subband_energy_cumul\
                + bloc_energy_cumul_mono(to_write_array)

            total_written_samples = total_written_samples + len(to_write_array)
        
    # ---- process the last shorter block ----
    samples_to_be_read = (blocks_number - 1) * buffer_length \
        + last_block_length
        
    # Read the last buffer of last_block_length samples
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, last_block_length, 
                                in_header)

    read_samples_number = len(input_array)

    total_read_samples = total_read_samples + read_samples_number

    if total_read_samples != samples_to_be_read:
        print("")
        print(f"number of samples to be read: {samples_to_be_read}")
        print(f"number of read samples: {total_read_samples}")
        print("As both numbers should be equal, there is a problem...")
        print("")
        
    in_handle.close()

    if current_subband_index == 0:
        orig_energy_cumul = orig_energy_cumul \
            + bloc_energy_cumul_mono(input_array)

    # Manage the overlapping
    convo_array = cnvTls.fast_convo_mono(input_array, ir_array)
   
    convo_array[: Nh1] = convo_array[: Nh1] + to_keep_array[:]
    convo_array = convo_array[: -tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = subband_energy_cumul + \
        bloc_energy_cumul_mono(convo_array)

    total_written_samples = total_written_samples + len(convo_array)

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul


# ----------
def analyse_one_file_multi_blocks(data, header, blocks_number,
                                  last_block_length, buffer_length):

    filters_names_list = data['filters_name_list']
    # filters_path = data['filters_path']

    input_file_name = data['input_filename']
    input_path = data['input_path']

    the_path = input_path / input_file_name
    
    channels_number = header['channels_number']

    filters_number = len(filters_names_list)
    
    if channels_number == 1:
        energies_cumul = np.zeros(filters_number + 1)

        for current_subband_index in range(filters_number):
            filter_name = filters_names_list[current_subband_index]
        
            if current_subband_index == 0:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_subband_mono(filter_name, data, the_path, 
                                                 current_subband_index, 
                                                 blocks_number, 
                                                 last_block_length, 
                                                 buffer_length)

                energies_cumul[-1] = orig_energy_cumul
                energies_cumul[0] = subband_energy_cumul

            else:
                subband_energy_cumul = \
                    analyse_one_subband_mono(filter_name, data, the_path, 
                                                 current_subband_index, 
                                                 blocks_number, 
                                                 last_block_length, 
                                                 buffer_length)

                energies_cumul[current_subband_index] = subband_energy_cumul
        
    else:
        energies_cumul = np.zeros((filters_number + 1, 2))

        for current_subband_index in range(filters_number):
            filter_name = filters_names_list[current_subband_index]
        
            if current_subband_index == 0:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_subband_stereo(filter_name, data, the_path, 
                                               current_subband_index,
                                               blocks_number, 
                                               last_block_length, 
                                               buffer_length)

                energies_cumul[-1, :] = orig_energy_cumul
                energies_cumul[0, :] = subband_energy_cumul

            else:
                subband_energy_cumul = \
                    analyse_one_subband_stereo(filter_name, data, the_path, 
                                               current_subband_index,
                                               blocks_number, 
                                               last_block_length,
                                               buffer_length)        

                energies_cumul[current_subband_index, :] = \
                    subband_energy_cumul

    return energies_cumul


# ----------
def create_and_save_ids_profile(data, energies_cumul, current_mapping):

    subbands_number = current_mapping.subbands_number
    mapping_key = current_mapping.mapping_key
    
    if data['channels_number'] == 1:
        ids_weights_array = np.zeros(subbands_number)
        
    else:
        ids_weights_array = np.zeros((data['channels_number'], 
                                      subbands_number))

    for i in range(subbands_number):
                
        if data['channels_number'] == 1:
            ids_weights_array[i] = \
                10 * np.log10(energies_cumul[i] / energies_cumul[-1])
        else:
            ids_weights_array[0, i] = \
                10 * np.log10(energies_cumul[i, 0] / energies_cumul[-1, 0])

            ids_weights_array[1, i] = \
                10 * np.log10(energies_cumul[i, 1]  / energies_cumul[-1, 1])

    if data['channels_number'] == 1:
        mean_dBFS_level = \
            10 * np.log10(energies_cumul[-1] / data['input_length'])
    else:
        mean_dBFS_level = [0, 0]
        mean_dBFS_level[0] = \
            10 * np.log10(energies_cumul[-1, 0] / data['input_length'])

        mean_dBFS_level[1] = \
            10 * np.log10(energies_cumul[-1, 1] / data['input_length'])

    wavInfos = \
        csvTls.WavInformations(
            data['input_filename'],
            data['input_path'], data['input_length'],
            data['channels_number'],
            data['sample_rate'],
            data['bits_per_sample'])

    profile_name = data['alias'][:-4] + '_' + str(data['ir_length']) \
        + mapping_key + '.ids.csv'
    
    mean_dBFS_level = np.round(mean_dBFS_level, 2)
    ids_weights_array = np.round(ids_weights_array, 2)
    
    The_profile = \
        prflTls.IDS_Profile(current_mapping,
                        profile_name,
                        data['channels_number'],
                        mean_dBFS_level,
                        ids_weights_array.transpose(),
                        data['input_length'])

    csvTls.create_csv_profile(wavInfos, The_profile, data['ir_length'],
                              data['output_path'], profile_name)


# ----------
def analyse_one_file(data, current_mapping):

    buffer_length = data['buffer_length']
    input_length = data['input_length']
    
    input_filename = data['input_filename']
    input_path = data['input_path']

    header = wvrdTls.read_wav_header(input_path / input_filename)
            
    input_length = header['samples_number']

    
    if input_length <= buffer_length:
        # launch mono bloc analyse
        energies_cumul = analyse_one_file_mono_block(data, header)
        
    else:
        blocks_number = int(np.ceil(input_length / buffer_length))
        last_block_length = input_length - (blocks_number - 1) * buffer_length
                
        # launch muli blocks analyse
        energies_cumul = \
            analyse_one_file_multi_blocks(data, header, blocks_number,
                                          last_block_length, buffer_length)

    create_and_save_ids_profile(data, energies_cumul, current_mapping)
    