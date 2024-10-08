# -*- coding: utf-8 -*-
"""
script name :       tools_mapping_creation.py

creation date:      10/08/2024, 18h53
modification date:  07/10/2024, 18h26

@author: Millot Laurent
"""


import pathlib

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls
import Sub_ToBo.tools_ids.manage_ids_analyses as anlTls
import Sub_ToBo.tools_ids.tools_ids_mappings as mpgTls
import Sub_ToBo.tools_ids.tools_ids_filters as fltrTls


main_path = pathlib.Path.cwd()


# 1. frequency mappings and related filters sets
# subfolder where the frequency mappings and the analysis filters sets
# will be created
tools_data_path = main_path / "data_subbands_tools"
fldrTls.create_new_subfolder(tools_data_path)

# subfolder where the csv files defining the frequency mappings will
# be created
mappings_def_path = tools_data_path / "mappings_definitions"
fldrTls.create_new_subfolder(mappings_def_path)

# subfolder where the subbands analyses filters sets will be created
subbands_filters_path = tools_data_path / "subbands_filters"
fldrTls.create_new_subfolder(subbands_filters_path)

# 2. analyses results (csv files and plots)
# subfolder where all the results will be created for analyses
analyses_data_path = main_path / "data_analyses_results"
fldrTls.create_new_subfolder(analyses_data_path)

# subfolder where the csv files will be created
csv_path = analyses_data_path / "ids_profiles_csv"
fldrTls.create_new_subfolder(csv_path)

# subfolder where the figures will be created
fig_path = analyses_data_path / "ids_profiles_figures"
fldrTls.create_new_subfolder(fig_path)

# 3. data needed for re-synthesis
# subfolder where all the data needed to feed the re-synthesizer will be 
# created
# It will be necessary to copy these data in the dedicated data subfolder
#  (related to the name of the frequency mapping: Data + "_" + mapping_name) 
resynthesis_data_path = main_path / "data_resynthesis"
fldrTls.create_new_subfolder(resynthesis_data_path)



# ----------
class Mapping(object):	
    def __init__(self, sample_rate, mapping_name, mapping_key, 
                 subbands_number, subbands_frequencies_array):
        self.sample_rate = sample_rate
        self.mapping_name = mapping_name
        self.mapping_key = mapping_key
        self.subbands_number = subbands_number
        self.subbands_frequencies_array = subbands_frequencies_array
        self.subbands_frequencies_array.append(sample_rate // 2)
        
    def display(self):
        print()
        print("-" * 20)
        print("current mapping details: ")
        print("sampling frequency (Hz): ", self.sample_rate)
        print("mapping name: ", self.mapping_name)
        print("mapping key: ", self.mapping_key)
        print("subbands number: ", self.subbands_number)
        print("subbands frequencies: ")
        print(self.subbands_frequencies_array[0:])
        print("-" * 20)
        print() 


# ----------
def create_needed_subfolders(mapping_name):
    
    # 1. subfolder mapping_name within analyses_results/ids_profiles_csv
    the_path = csv_path / mapping_name
    fldrTls.create_new_subfolder(the_path)
    
    # 2. subfolder mapping_name within analyses_results/analyses_results
    the_path = fig_path / mapping_name
    fldrTls.create_new_subfolder(the_path)   
    
    # 3. subfolder Data_ + mapping_name and needed subfolders
    subfolder_name = "Data_" + mapping_name
    beg_path = resynthesis_data_path / subfolder_name
    fldrTls.create_new_subfolder(beg_path)

    the_path = beg_path / "ids_figures"
    fldrTls.create_new_subfolder(the_path)

    the_path = beg_path / "ids_profiles_csv"
    fldrTls.create_new_subfolder(the_path)

    the_path = beg_path / "wav_origfiles"
    fldrTls.create_new_subfolder(the_path)

    the_path = beg_path / "wav_sbfiles"
    fldrTls.create_new_subfolder(the_path)    


# ----------
def create_new_mapping(mapping_name, current_mapping, sample_rate,
                   ripple_dB=80.0, width_Hz=5.0):

    create_needed_subfolders(mapping_name)
    
    mpgTls.create_mapping_def_file(current_mapping, mappings_def_path)
    
    fltrTls.generate_ids_filters_set(subbands_filters_path, 
                                     current_mapping, mapping_name,
                                     sample_rate, ripple_dB, 
                                     width_Hz)


# ----------
def process_mappings_creation(mapping_names_list, sample_rates_list, 
                              ripple_dB=80.0, width_Hz=5.0):
    
    for sample_rate in sample_rates_list:
        for mapping_name in mapping_names_list:
            create_needed_subfolders(mapping_name)

            current_mapping = mpgTls.default_mapping(sample_rate, 
                                                     mapping_name)
            
            
            mpgTls.create_mapping_def_file(current_mapping, mappings_def_path)
            
            fltrTls.generate_ids_filters_set(subbands_filters_path, 
                                             current_mapping, mapping_name,
                                             sample_rate, ripple_dB, 
                                             width_Hz)


# ----------
def list_installed_mappings():
    
    mappings_list = \
        fldrTls.list_given_extension_files(mappings_def_path, ".csv")
    
    print()
    print("Installed frequency mappings:")
    print()
    for the_mapping in mappings_list:
        the_mapping = anlTls.load_mapping(the_mapping, mappings_def_path)
        the_str = f"{the_mapping.mapping_name} ({the_mapping.mapping_key})"\
        f" / {the_mapping.subbands_number} / "\
            + str(the_mapping.subbands_frequencies_array)
        print(the_str)
        print()
    print()


# ----------
def remove_one_mapping(mapping_name, sample_rate, ripple_dB, width_Hz):
    # delete mapping related folders and their content
    # subfolder mapping_name within analyses_results/ids_profiles_csv
    the_path = csv_path / mapping_name
    fldrTls.delete_folder(the_path)
    
    # subfolder mapping_name within analyses_results/analyses_results
    the_path = fig_path / mapping_name
    fldrTls.delete_folder(the_path)  
    
    # subfolder Data_ + mapping_name and needed subfolders
    subfolder_name = "Data_" + mapping_name
    the_path = resynthesis_data_path / subfolder_name
    fldrTls.delete_folder(the_path)

    # generate the file name
    the_file_name = "mapping_" + mapping_name + "_" + str(sample_rate)\
        + ".csv"
    
    # delete the mapping definition file 
    fldrTls.delete_a_file(mappings_def_path / the_file_name)
    
    # delete the filters set folder
    ir_length, _ = fltrTls.determine_Kaiser_parameters(ripple_dB, width_Hz, 
                                                       sample_rate // 2)

    filters_subfolder_name = "h_" + mapping_name + "_"\
        + str(int(sample_rate/100)) + "_" + str(int(ir_length))

    the_path = subbands_filters_path / filters_subfolder_name
    fldrTls.delete_folder(the_path)
    
