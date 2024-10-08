# -*- coding: utf-8 -*-
"""
script name :       manage_ids_analyses_resynthesis.py

creation date:      25/08/2024, 20h49
modification date:  07/10/2024, 22h19

@author: Millot
"""


import pathlib
import shutil

from scipy.signal import kaiserord

import Sub_ToBo.tools_ids.ids_resynthesis_central_core as anlTls
import Sub_ToBo.tools_ids.tools_ids_mappings as mpgTls
import Sub_ToBo.tools_wav.tools_wav_read as wvrdTls
import Sub_ToBo.tools_wav.tools_wav_write as wvwrtTls


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


# -----------
def copy_original_wav(original_path, input_filename, copy_path, 
                      output_filename, data):

    original_path = pathlib.Path(original_path)
    copy_path = pathlib.Path(copy_path)

    if data["audio_format"] == 3:
        shutil.copyfile(original_path / input_filename,
                        copy_path / output_filename)

    else:
        the_path = original_path / input_filename
        header = wvrdTls.read_wav_header(the_path)
        samples_array = wvrdTls.read_wav_file(the_path, header)

        sample_rate = data["sample_rate"]
        format_string = "f32"
        wvwrtTls.create_and_write_wav_file(output_filename, copy_path, 
                                           sample_rate, format_string, 
                                           samples_array)
      

# ----------
def analyses_the_corpus(mapping_name, file_names_list, alias_names_list, 
                        corpus_path, mappings_def_path, subbands_filters_path,
                        csv_path, fig_path, wav_orig_path, wav_sb_path, 
                        ripple_dB=80., width_Hz=5., buffer_length=2**16):   
    
    # 1. collect sample_rate, filters_length, filters subfolder name,
    # filters subfolder path, mapping file name and current mapping        
    header = wvrdTls.read_wav_header(corpus_path / file_names_list[0])

    sample_rate = header["sample_rate"]
        
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

    # 2. manage the ids analysis and resynthesis preparation for all
    # wav files
    # useful variables initialisation        
    data = {'input_length': 0, 'ir_length': filters_length,
            'ir_array': 0, 'channels_number': 0, 'output_length': 0,
            'input_filename': '', 'input_path': corpus_path,
            'output_filename': '', 'csv_path': csv_path,
            'fig_path': fig_path, 'wav_orig_path': wav_orig_path,
            'wav_sb_path': wav_sb_path,
            'buffer_length': buffer_length, 'alias': '', 
            'sample_rate': sample_rate,
            'mapping_name': mapping_name,
            'mapping_file_name': mapping_file_name,
            'mapping_key':current_mapping.mapping_key}
        
    files_number = len(file_names_list)

    for k in range(files_number):
        print("-" * 15)
        print(f"processing file #{k + 1}  / {files_number}")
        
        file_name = file_names_list[k]
        
        print(f"filename: {file_name}")

        header = wvrdTls.read_wav_header(corpus_path / file_name)
                
        data['input_length'] = header['samples_number']
        data['output_length'] = data['input_length'] + data['ir_length'] - 1
        
        data['channels_number'] = header['channels_number']
        data['sample_rate'] = header['sample_rate']
        
        data['bits_per_sample'] = header['bits_per_sample']
        data['audio_format'] = header['audio_format']

        data['input_filename'] = file_name
        data['alias'] = alias_names_list[k][:-4]
        
        filters_names_list = create_filters_names_list(current_mapping)
        data['filters_name_list'] = filters_names_list
        
        data['filters_path'] = filters_path

        # copy original wav
        copy_original_wav(data["input_path"], data["input_filename"],
                          data["wav_orig_path"], data["alias"] + ".wav",
                          data)

        anlTls.analyse_one_file(data, current_mapping)
