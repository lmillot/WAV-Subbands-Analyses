# -*- coding: utf-8 -*-
"""
script name :       manage_ids_analyses.py

creation date:      11/08/2024, 01h20
modification date:  07/10/2024, 16h31

@author: Millot
"""


from scipy.signal import kaiserord

import Sub_ToBo.tools_ids.ids_analyser_central_core as anlTls
import Sub_ToBo.tools_ids.tools_ids_mappings as mpgTls
import Sub_ToBo.tools_wav.tools_wav_read as wvrdTls


# ----------
def IR_length(ripple_dB, width_Hz, sample_rate=44100):

    width = 2 * width_Hz / sample_rate

    ir_length, beta = kaiserord(ripple_dB, width)

    # force an odd number of coefficients
    if ir_length % 2 == 0:
        ir_length = ir_length - 1

    return ir_length


# ----------
def load_mapping(mapping_file_name, mappings_def_path):    

    current_mapping = mpgTls.load_mapping_file(mapping_file_name, 
                                               mappings_def_path)
    
    return current_mapping
        

# ----------
def create_filters_names_list(current_mapping):

    filters_names_list = []
    
    for k in range(current_mapping.subbands_number):
        filter_name = str(current_mapping.subbands_frequencies_array[k])\
            + "_" + str(current_mapping.subbands_frequencies_array[k + 1])\
            + ".wav"
            
        filters_names_list.append(filter_name)
        
    return filters_names_list

    pass

    
# ----------
def analyses_the_corpus(mapping_name, file_names_list, alias_names_list, 
                        corpus_path, mappings_def_path, subbands_filters_path,
                        ids_profiles_path, ripple_dB=80., width_Hz=5.,
                        buffer_length=2**16):


    header = wvrdTls.read_wav_header(corpus_path / file_names_list[0])
    sample_rate = header['sample_rate']
    
    filters_length = IR_length(ripple_dB, width_Hz, sample_rate)

    # sub_folder: h_Audio_441_44263
    subfolder_name = "h_" + mapping_name + "_" + str(int(sample_rate / 100))\
        + "_" + str(int(filters_length))
    
    filters_path = subbands_filters_path / subfolder_name

    # mapping_Audio_44100.csv
    mapping_file_name = "mapping_" + mapping_name + "_"\
        + str(int(sample_rate)) + ".csv"

    current_mapping = mpgTls.load_mapping_file(mapping_file_name, 
                                               mappings_def_path)
     
    files_number = len(file_names_list)
        
    data = {'input_length': 0, 'ir_length': filters_length,
            'ir_array': 0, 'channels_number': 0,
            'input_filename': '', 'input_path': corpus_path,
            'output_filename': '', 'output_path': ids_profiles_path,
            'buffer_length': buffer_length, 'alias': '', 
            'sample_rate': sample_rate}


    for k in range(files_number):
        print("-" * 10)
        print(f"processing file #{k + 1}  / {files_number}")
        
        file_name = file_names_list[k]
        
        print(f"file name: {file_name}")
        print()

        header = wvrdTls.read_wav_header(corpus_path / file_name)
                
        data['input_length'] = header['samples_number']
        data['channels_number'] = header['channels_number']
        data['sample_rate'] = header['sample_rate']
        data['bits_per_sample'] = header['bits_per_sample']
        
        data['input_filename'] = file_name
        data['alias'] = alias_names_list[k]
        
        filters_names_list = create_filters_names_list(current_mapping)
        data['filters_name_list'] = filters_names_list
        
        data['filters_path'] = filters_path

        anlTls.analyse_one_file(data, current_mapping)
