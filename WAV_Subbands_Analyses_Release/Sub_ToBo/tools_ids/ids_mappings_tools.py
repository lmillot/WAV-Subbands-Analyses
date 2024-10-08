# -*- coding: utf-8 -*-
"""
name:               ids_mappings_tools.py
status:             à reprendre !? Oui !

creation date:      11/06/2015, 18h13
modification date:  24/08/2024, 11h17

@author: Millot Laurent
"""


import copy
import csv
import pathlib

import Sub_ToBo.tools_ids.default_mappings_definitions as mpgTls


main_path = pathlib.Path.cwd()

main_path = pathlib.Path(main_path)

# ids_applications_private_data folder path
data_path = main_path / "ids_applications_private_data/"

# mappings folder path
mappings_folder_path = data_path / "ids_mappings"

# list of the mapping files (.csv) paths
mappings_paths_list = list(mappings_folder_path.glob("**/*.csv"))

# path of first mapping file
first_mapping_path = mappings_paths_list[0]

# name of the first mapping file
first_mapping = first_mapping_path.name


default_mappings = mpgTls.define_default_mappings()


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
    # -----
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

    # -----
    def display(self):
        print()
        print("--------------------")
        print("current mapping details: ")
        print("sampling frequency (Hz): ", self.sample_rate)
        print("mapping name: ", self.mapping_name)
        print("mapping key: ", self.mapping_key)
        print("subbands number: ", self.subbands_number)
        print("subbands frequencies: ")
        print(self.subbands_frequencies_array[0:])
        print("--------------------")
        print()


# ----------
def append_ids_mappings_header(the_mappings_file, current_mapping):
    
    # first line of the heading:
    # sampling frequency, 44100,
    # append a blanck line
    the_str = "sampling frequency," + str(current_mapping.sample_rate) \
        + ",\n"

    the_mappings_file.write(the_str)

    # second line of the heading
    # mapping_name, mapping_key, subbands_number,
    the_str = "mapping_name, mapping_key, subbands_number,\n"
    the_mappings_file.write(the_str)

    # third line of the heading
    the_str = "subbands frequencies,\n"
    the_mappings_file.write(the_str)


# ----------
def create_ids_mappings_file(current_mapping, maps_path=""):
    
    # generate the file name
    the_filename = "mappings_" + str(current_mapping.sample_rate) + ".csv"

    # create and open the mappings file
    the_mappings_file = open(maps_path / the_filename, "a")

    # append the heading
    append_ids_mappings_header(the_mappings_file, current_mapping)

    # close the mappings file
    the_mappings_file.close()

    append_a_new_mapping(current_mapping, maps_path)


# ----------
def append_a_new_mapping(current_mapping, maps_path=""):
    
    # generate the file name
    the_filename = "mappings_" + str(current_mapping.sample_rate) + ".csv"

    # create and open the mappings file
    the_mappings_file = open(maps_path / the_filename, "a")

    # append a blanck line
    the_mappings_file.write(",\n")

    the_str = current_mapping.mapping_name + "," + \
        current_mapping.mapping_key + "," + \
        str(current_mapping.subbands_number) + ",\n"

    the_mappings_file.write(the_str)
    the_str = ""

    for frequency in current_mapping.subbands_frequencies_array:
        the_str = the_str + str(frequency) + ","

    the_str = the_str + "\n"
    the_mappings_file.write(the_str)

    # close the mappings file
    the_mappings_file.close()


# ----------
def default_mapping(sample_rate, mapping_name):
    
    the_mappings = copy.deepcopy(default_mappings)

    mapping_key = the_mappings[mapping_name][0]
    subbands_number = the_mappings[mapping_name][1]
    subbandsArray = the_mappings[mapping_name][2]
    current_mapping = Mapping(sample_rate,
                             mapping_name, mapping_key,
                             subbands_number, subbandsArray)

    return current_mapping


# ----------
def defined_mappings(sample_rate, the_file_path):
    
    csv_filename = "mappings_" + str(sample_rate) + ".csv"

    try:
        mappings_dico = \
            load_one_mapping_file(csv_filename, the_file_path)
            
    except FileNotFoundError:
        mappings_dico = copy.deepcopy(default_mappings)

    return mappings_dico


# est-ce en fait utilise ? car ca ne renvoie pas un Mapping
# # ----------
def new_default_mapping(sample_rate, mapping_name,
                        the_file_path=mappings_folder_path):

    mappings_dico = \
        defined_mappings(sample_rate, the_file_path)

    try:
        current_mapping = mappings_dico[mapping_name]
    except KeyError:
        current_mapping = mappings_dico["Leipp"]

    return current_mapping


# ----------
def append_default_mapping(sample_rate, mapping_name):
    
    current_mapping = default_mapping(sample_rate, mapping_name)
    current_mapping.display()
    append_a_new_mapping(current_mapping)


# ----------
def load_one_mapping_file(csv_filename=first_mapping,
                          the_file_path=mappings_folder_path):
    """
        return a dictionary of defined mappings within the chosen file

        each element of the dictionary follows this structure:
        - key: mapping name
        - mapping details dictionnary:
        -   mapping_name
        -   mapping_key
        -   sample_rate
        -   subbands_number
        -   subbands_frequencies_array
    """

    data_list = []

    file = open(the_file_path / csv_filename, newline="")
    fichier_csv = csv.reader(file)
    data_list = list(fichier_csv)
    file.close()

    lines_number = len(data_list)

    sample_rate = int(data_list[0][1])

    mappings_dico = {}
    the_index = 4

    the_counter = 0

    mapping = []

    while the_index < lines_number:
        mapping_name = data_list[the_index][0]
        mapping_key = data_list[the_index][1]
        subbands_number = int(data_list[the_index][2])
        subbands_frequencies_array = []

        the_index = the_index + 1
        theList = data_list[the_index]

        for sbIndex in range(len(theList)-2):
            newLimit = int(theList[sbIndex])
            subbands_frequencies_array.append(newLimit)

        mapping = Mapping(sample_rate, mapping_name,
                          mapping_key, subbands_number,
                          subbands_frequencies_array)

        mappings_dico[mapping_name] = mapping

        the_index = the_index + 2
        the_counter = the_counter + 1

    return mappings_dico


# ----------
def create_reference_mappings_file(sample_rate, maps_path=""):

    current_mapping = default_mapping(sample_rate, "Audio")
    current_mapping.display()

    create_ids_mappings_file(current_mapping, maps_path)

    mappings_list = ["Leipp", "Octaves", "Studio", "Sono"]

    for the_name in mappings_list:
        the_map = default_mapping(sample_rate, the_name)
        the_map.display()
        append_a_new_mapping(the_map, maps_path)
