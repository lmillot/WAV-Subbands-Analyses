#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script:             ids_resynthesis_central_core.py

creation date:      25/08/2024, 20h51
modification date:  29/09/2024, 22h36

@author: Millot Laurent
"""



import numpy as np

import Sub_ToBo.tools_dsp.tools_fast_convolution as cnvTls
import Sub_ToBo.tools_ids.csv_ids_profiles_tools as csvTls
import Sub_ToBo.tools_ids.ids_profiles_tools as prflTls
import Sub_ToBo.tools_ids_plot.tools_ids_profiles_plot_resynthesis as pltTls
import Sub_ToBo.tools_wav.tools_wav_read as wvrdTls
import Sub_ToBo.tools_wav.tools_wav_write as wvwrTls

     
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
    ir_header = wvrdTls.read_wav_header(file_path)
    ir_array = wvrdTls.read_wav_file(file_path, ir_header)
    
    tau = int((len(ir_array) - 1) / 2)
    
    # Apply the filter
    output_array = cnvTls.fast_convo_stereo(input_array, ir_array)
    output_array = output_array[:, tau:-tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = bloc_energy_cumul_stereo(output_array)

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
    ir_header = wvrdTls.read_wav_header(file_path)
    ir_array = wvrdTls.read_wav_file(file_path, ir_header)

    tau = int((len(ir_array) - 1) / 2)

    # Apply the filter
    output_array = cnvTls.fast_convo_mono(input_array, ir_array)

    output_array = output_array[tau:-tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = bloc_energy_cumul_mono(output_array)

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

    in_path = input_path / input_file_name
    in_header = wvrdTls.read_wav_header(in_path)
    input_array = wvrdTls.read_wav_file(in_path, in_header)

    channels_number = header['channels_number']

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
    sample_rate = data['sample_rate']

    # Read the filter IR
    filter_path = filters_path / filter_name
    ir_header = wvrdTls.read_wav_header(filter_path)
    ir_array = wvrdTls.read_wav_file(filter_path, ir_header)

    ir_length = len(ir_array)
    Nh1 = int(ir_length - 1)
    tau = int(Nh1 / 2)

    # Open the input signal
    in_header = wvrdTls.read_wav_header(in_path)
    in_handle, in_position = wvrdTls.open_wav(in_path, in_header)

    # Create the output wav header and open the wav file
    out_file_name = data['alias'] + "_sb" + str(current_subband_index + 1)\
        + "_" + data['mapping_key'] + ".wav"

    format_string = "f32"
        
    out_handler, out_position = \
        wvwrTls.create_wav_file(out_file_name, data['wav_sb_path'], 
                                sample_rate, format_string, 2,
                                data['output_length'])

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
    convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)
            
    to_write_array = convo_array[:, : buffer_length]

    # suppress tau samples for the first block
    to_write_array = to_write_array[:, tau:]

    # Calculate the energy cumul
    subband_energy_cumul = subband_energy_cumul\
        + bloc_energy_cumul_stereo(to_write_array)

    # update the residue
    to_keep_array = convo_array[:, buffer_length: ]

    # write the first output block
    _, samples_number = to_write_array.shape
    
    out_handler, out_position = \
        wvwrTls.write_data_to_file(out_handler, out_position, format_string, 
                           to_write_array.T, 2, samples_number)
        
    total_written_samples = total_written_samples + samples_number
   
    if blocks_number > 2:
    # ---- process median blocks ----
        for i in range(2, blocks_number):
            # buffer used for input reading and output writing
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
            to_write_array[:, : Nh1] = convo_array[:, : Nh1] \
                + to_keep_array[:, : Nh1]

            to_write_array[:, Nh1: ] = convo_array[:, Nh1: buffer_length]

            # Calculate the energy cumul
            subband_energy_cumul = subband_energy_cumul\
                + bloc_energy_cumul_stereo(to_write_array)

            # update the residue
            to_keep_array = convo_array[:, buffer_length: ]

            # write a new block
            _, samples_number = to_write_array.shape
            
            out_handler, out_position = \
                wvwrTls.write_data_to_file(out_handler, out_position, 
                                           format_string, to_write_array.T, 2,
                                           samples_number)
                
            total_written_samples = total_written_samples + samples_number
      
    # ---- process the last shorter block ----
    samples_to_be_read = (blocks_number - 1) * buffer_length \
        + last_block_length

    # Read the last buffer of last_block_length samples
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, last_block_length, 
                                in_header)

    in_handle.close()
    
    input_array = input_array.T

    _, read_samples_number = input_array.shape
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

    convo_array = cnvTls.fast_convo_stereo(input_array, ir_array)

    # Manage the overlapping
    convo_array[:, : Nh1] = convo_array[:, : Nh1] + to_keep_array[:, :]
    convo_array = convo_array[:, : -tau]

    # Calculate the energy of the filtered signal
    subband_energy_cumul = subband_energy_cumul + \
        bloc_energy_cumul_stereo(convo_array)

    # write last block
    _, samples_number = convo_array.shape
       
    out_handler, out_position = \
        wvwrTls.write_data_to_file(out_handler, out_position, format_string, 
                           convo_array.T, 2, samples_number)
        
    total_written_samples = total_written_samples + samples_number
    
    wvwrTls.close_wav_file(out_handler, out_position)

    total_written_samples = total_written_samples + samples_number

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul

    
# ----------
def analyse_one_subband_mono(filter_name, data, in_path, 
                             current_subband_index, blocks_number, 
                             last_block_length, buffer_length):
    
    filters_path = data['filters_path']
    sample_rate = data['sample_rate']
   
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

    # Create the output wav header and open the wav file
    out_file_name = data['alias'] + "_sb" + str(current_subband_index + 1)\
        + "_" + data['mapping_key'] + ".wav"

    format_string = "f32"

    out_handler, out_position = \
        wvwrTls.create_wav_file(out_file_name, data['wav_sb_path'], 
                                sample_rate, format_string, 1,
                                data['output_length'])

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

    # write the first output block
    samples_number = len(to_write_array)
    
    out_handler, out_position = \
        wvwrTls.write_data_to_file(out_handler, out_position, format_string,
                                   to_write_array, 1, samples_number)
        
    total_written_samples = total_written_samples + samples_number

    # Calculate the energy cumul
    subband_energy_cumul = subband_energy_cumul\
        + bloc_energy_cumul_mono(to_write_array)


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

            samples_number = len(to_write_array)
            
            out_handler, out_position = \
                wvwrTls.write_data_to_file(out_handler, out_position, 
                                           format_string, to_write_array, 1,
                                           samples_number)
                
            total_written_samples = total_written_samples + samples_number

            # Calculate the energy cumul
            subband_energy_cumul = subband_energy_cumul\
                + bloc_energy_cumul_mono(to_write_array)

        
    # ---- process the last shorter block ----
    samples_to_be_read = (blocks_number - 1) * buffer_length \
        + last_block_length

    # Read the last buffer of last_block_length samples
    input_array, in_position =  \
        wvrdTls.read_wav_buffer(in_handle, in_position, last_block_length, 
                                in_header)

    in_handle.close()
    
    read_samples_number = len(input_array)
    
    total_read_samples = total_read_samples + read_samples_number

    if total_read_samples != samples_to_be_read:
        print("")
        print(f"number of samples to be read: {samples_to_be_read}")
        print(f"number of read samples: {total_read_samples}")
        print("As both numbers should be equal, there is a problem...")
        print("")
        
    if current_subband_index == 0:
        orig_energy_cumul = orig_energy_cumul \
            + bloc_energy_cumul_mono(input_array)

    # Manage the overlapping
    convo_array = cnvTls.fast_convo_mono(input_array, ir_array)
   
    convo_array[: Nh1] = convo_array[: Nh1] + to_keep_array[:]
    convo_array = convo_array[: -tau]

    # write last block
    samples_number = len(convo_array)
    
    out_handler, out_position = \
        wvwrTls.write_data_to_file(out_handler, out_position, format_string, 
                           convo_array, 1, samples_number)
        
    total_written_samples = total_written_samples + samples_number
    
    wvwrTls.close_wav_file(out_handler, out_position)

    # Calculate the energy of the filtered signal
    subband_energy_cumul = subband_energy_cumul + \
        bloc_energy_cumul_mono(convo_array)

    if current_subband_index == 0:
        return subband_energy_cumul, orig_energy_cumul

    else:
        return subband_energy_cumul

  
# ----------
def analyse_one_file_multi_blocks(data, in_header, blocs_number,
                                  last_block_length, buffer_length):

    filters_names_list = data['filters_name_list']

    input_file_name = data['input_filename']
    input_path = data['input_path']

    in_path = input_path / input_file_name
    
    channels_number = in_header['channels_number']

    filters_number = len(filters_names_list)
    
    if channels_number == 1:
        energies_cumul = np.zeros(filters_number + 1)

        for current_subband_index in range(filters_number):
 
            filter_name = filters_names_list[current_subband_index]

        
            if current_subband_index == 0:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_subband_mono(filter_name, data, in_path, 
                                             current_subband_index,
                                             blocs_number, last_block_length,
                                             buffer_length)

                energies_cumul[-1] = orig_energy_cumul
                energies_cumul[0] = subband_energy_cumul

            else:
                subband_energy_cumul = \
                    analyse_one_subband_mono(filter_name, data, in_path, 
                                             current_subband_index,
                                             blocs_number, last_block_length, 
                                             buffer_length)        

                energies_cumul[current_subband_index] = subband_energy_cumul
        
    else:
        energies_cumul = np.zeros((filters_number + 1, 2))

        for current_subband_index in range(filters_number):

            filter_name = filters_names_list[current_subband_index]
       
            if current_subband_index == 0:
                subband_energy_cumul, orig_energy_cumul = \
                    analyse_one_subband_stereo(filter_name, data, in_path, 
                                               current_subband_index,
                                               blocs_number, 
                                               last_block_length, 
                                               buffer_length)

                energies_cumul[-1, :] = orig_energy_cumul
                energies_cumul[0, :] = subband_energy_cumul

            else:
                subband_energy_cumul = \
                    analyse_one_subband_stereo(filter_name, data, in_path, 
                                               current_subband_index,
                                               blocs_number, 
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
        # mean_dBFS_level = 0
        mean_dBFS_level = \
            10 * np.log10(energies_cumul[-1] / data['input_length'])
    else:
        mean_dBFS_level = [0, 0]
        mean_dBFS_level[0] = \
            10 * np.log10(energies_cumul[-1, 0] / data['input_length'])

        mean_dBFS_level[1] = \
            10 * np.log10(energies_cumul[-1, 1] / data['input_length'])

    ids_weights_array = np.round(ids_weights_array, 2)
    mean_dBFS_level = np.round(mean_dBFS_level, 2)

    wavInfos = \
        csvTls.WavInformations(
            data['input_filename'],
            data['input_path'], data['input_length'],
            data['channels_number'],
            data['sample_rate'],
            data['bits_per_sample'])

    profile_name = data['alias'] + '_' + str(data['ir_length']) \
        + mapping_key + '.ids.csv'

    The_profile = \
        prflTls.IDS_Profile(current_mapping,
                        profile_name,
                        data['channels_number'],
                        mean_dBFS_level,
                        ids_weights_array.transpose(),
                        data['input_length'])

    csvTls.create_csv_profile(wavInfos, The_profile, data['ir_length'],
                              data['csv_path'], profile_name)
        
    min_ids_value = ids_weights_array.min()
    max_ids_value = ids_weights_array.max()
    
    fig_name = data['alias'] + "_" + current_mapping.mapping_key
    freq_array = np.array(current_mapping.subbands_frequencies_array)
    
    pltTls.plot_IDS_profile(ids_weights_array, mean_dBFS_level, freq_array,
                            data['channels_number'], min_ids_value, 
                            max_ids_value, fig_name, data["fig_path"], 
                            the_radical="")


# ----------
def analyse_one_file(data, current_mapping):
    
    buffer_length = data['buffer_length']
    input_length = data['input_length']

    in_header = wvrdTls.read_wav_header(data['input_path'] 
                                        / data['input_filename'])
            
    input_length = in_header['samples_number']
    
    print()
    print("-" * 20)
    
    if input_length <= buffer_length:
        # launch mono bloc analyse
        energies_cumul = analyse_one_file_mono_block(data, in_header)
        
    else:
        blocks_number = int(np.ceil(input_length / buffer_length))
        last_block_length = input_length - buffer_length * (blocks_number - 1)
        
        print(f"input_length : {input_length}")
        print(f"buffer_length : {buffer_length}")
        print(f"last_block_length : {last_block_length}")
        print(f"blocks_number : {blocks_number}")
        print()
        
        # launch muli blocks analyse
        energies_cumul = \
            analyse_one_file_multi_blocks(data, in_header, blocks_number,
                                          last_block_length, buffer_length)

    create_and_save_ids_profile(data, energies_cumul, current_mapping)
    