# -*- coding: utf-8 -*-
"""
name:        tools_ids_mappings.py

creation date:      11/08/2024, 07h32
modification date:  24/08/2024, 11h15

@author: Millot Laurent
"""


import copy
import csv

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls



default_mappings_dico =\
    {
    "Audio": ["A", 13,
              [0, 30, 60, 80, 100, 120, 250, 500, 1000, 2000, 4000, 
               8000, 16000]],
    "Leipp": ["L", 10,
              [0, 50, 200, 400, 800, 1200, 1800, 3000, 6000, 15000]],
    "Octaves": ["O", 11,
                [0, 22, 44, 88, 176, 353, 707, 1414, 2828, 5656, 11313]],
    "Sono": ["S", 14, 
             [0, 25, 33, 55, 80, 120, 250, 500, 1000, 2000, 4500, 7000, 
              10000, 15000]]
        }


# ----------
def suppress_doublons(the_array):

    short_array = []
    short_array.append(the_array[0])
    
    the_length = len(the_array)
    
    for k in range(1, the_length):
        the_element = the_array[k]
        
        if the_element not in short_array:
            short_array.append(the_element)
    
    return short_array


# ----------
class Mapping(object):	
    def __init__(self, sample_rate, mapping_name, mapping_key, 
                 subbands_number, subbands_frequencies_array):

        self.sample_rate = sample_rate
        self.mapping_name = mapping_name
        self.mapping_key = mapping_key
        self.subbands_number = subbands_number

        subbands_frequencies_array.append(sample_rate // 2)
        subbands_frequencies_array = \
            suppress_doublons(subbands_frequencies_array)
        
        self.subbands_frequencies_array = subbands_frequencies_array
        
    def display(self):
        print()
        print("--------------------")
        print("current mapping details: ")
        print("sampling frequency (Hz): ", self.sample_rate)
        print("mapping name: ", self.mapping_name)
        print("mapping key: ", self.mapping_key)
        print("subbands number: ", self.subbands_number)
        print("subbands frequencies: ")
        print(self.subbands_frequencies_array[:])
        print("--------------------")
        print() 


# ----------
def default_mapping(sample_rate, mapping_name):
    
    the_mappings = copy.deepcopy(default_mappings_dico)

    mapping_key = the_mappings[mapping_name][0]
    subbands_number = the_mappings[mapping_name][1]
    subbands_array = the_mappings[mapping_name][2]
    
    current_mapping = Mapping(sample_rate, mapping_name, mapping_key,
                             subbands_number, subbands_array)
                
    return current_mapping


# ----------
def list_defined_mapping_files(mappings_folder_path):

    # list of the mapping files (.csv) paths    
    mappings_files_list = \
        fldrTls.list_given_extension_files(mappings_folder_path, ".csv")
    
    return mappings_files_list


# ----------
def create_mapping_def_file(current_mapping, mapping_path):

    # generate the file name
    the_file_name = "mapping_" + current_mapping.mapping_name + "_"\
        + str(current_mapping.sample_rate) + ".csv"
    
    # create and open the mappings file
    if fldrTls.is_file_existing(mapping_path / the_file_name):
        fldrTls.delete_a_file(mapping_path / the_file_name)
    
    the_mapping_file = open(mapping_path / the_file_name, "a")
    
    the_str = "sample rate," + str(current_mapping.sample_rate)\
        + ",\n"
    the_mapping_file.write(the_str)
    
    the_str ="mapping_name," + current_mapping.mapping_name +",\n"
    the_mapping_file.write(the_str)

    the_str ="mapping_key," + current_mapping.mapping_key +",\n"
    the_mapping_file.write(the_str)    

    the_str ="subbands_number," + str(current_mapping.subbands_number)\
        +",\n"
    the_mapping_file.write(the_str)   
    
    the_str = "subbands frequencies,\n"
    the_mapping_file.write(the_str)

    the_str = ""
    
    for frequency in current_mapping.subbands_frequencies_array:
        the_str = the_str + str(frequency) + ","
        
    the_str = the_str + "\n"       
    the_mapping_file.write(the_str)  
    
    # close the mappings file
    the_mapping_file.close()


# ----------
def load_mapping_file(csv_filename, the_file_path):
    """
        return the mapping defined within the chosen file

        structure of the mapping:
        -  sample_rate
        -  mapping_name
        -  mapping_key
        -  subbands_number
        -  subbands_frequencies_array
    """

    data_list = []

    file = open(the_file_path / csv_filename, newline="")
    fichier_csv = csv.reader(file)
    data_list = list(fichier_csv)
    file.close()


    sample_rate = int(data_list[0][1])
    mapping_name = data_list[1][1]
    mapping_key = data_list[2][1]
    subbands_number = int(data_list[3][1])
    
    subbands_frequencies_array = []

    freq_list = data_list[5]

    for sb_index in range(subbands_number):
        new_limit = int(freq_list[sb_index])
        subbands_frequencies_array.append(new_limit)

    current_mapping = Mapping(sample_rate, mapping_name, mapping_key, 
                      subbands_number, subbands_frequencies_array)

    return current_mapping
