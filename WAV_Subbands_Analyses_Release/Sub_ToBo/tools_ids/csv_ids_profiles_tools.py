# -*- coding: utf-8 -*-
"""
application:          csv_ids_profiles_tools.py

creation date:        12/06/2015, 14h15
modification date:    23/08/2024, 22h14

@author: Laurent Millot
"""


import csv
import numpy as np
import pathlib

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls
import Sub_ToBo.tools_ids.tools_ids_mappings as mpgTls
import Sub_ToBo.tools_ids.ids_profiles_tools as prflTls



# ----------
class WavInformations():
    # -----
    def __init__(self, wav_filename, wav_file_path,
                 samples_number, channels_number=1,
                 sample_rate=44100,
                 bits_per_sample=32):

        self.radical_name = wav_filename[:-4]
        self.wav_file_path = wav_file_path
        self.samples_number = samples_number
        self.channels_number = channels_number
        self.sample_rate = sample_rate
        self.bits_per_sample = bits_per_sample

    # -----
    def display(self):
        print()
        print("--------------------")
        print("wav informations: ")
        print("radical name: ", self.radical_name)
        print("wav file path:")
        print(self.wav_file_path)
        print()

        print("sampling frequency (Hz): ", self.sample_rate)
        print("channels number: ", self.channels_number)
        print("samples number: ", self.samples_number)
        print("bits per sample: ", self.bits_per_sample)
        print("--------------------")
        print()


# ----------
def create_csv_profile(Wav_file_infos, Profile, filters_length, the_path="",
                       the_filename=""):

    # generate the file name
    if the_filename == "":
        the_filename = Wav_file_infos.radical_name \
                    + "_" \
                    + str(filters_length) \
                    + Profile.mapping_key + ".ids.csv"

    # create and open the csv profile file
    the_path = pathlib.Path(the_path)

    the_profile_file = open(the_path / the_filename, "w")

    # heading of the ids profile csv file
    # append a blanck line
    the_profile_file.write(",\n")

    the_str = "IDS file version,0.91,\n"
    the_profile_file.write(the_str)

    the_str = "Wave file path," + str(Wav_file_infos.wav_file_path) + ",\n"
    the_profile_file.write(the_str)

    the_str = "Wav file name," + Wav_file_infos.radical_name + ".wav,\n"
    the_profile_file.write(the_str)

    # append a blanck line
    the_profile_file.write(",\n")

    # useful informations
    the_str = "Number of channels," + str(Profile.channels_number) + ",\n"
    the_profile_file.write(the_str)

    the_str = "Number of samples," + str(Profile.samples_number) + ",\n"
    the_profile_file.write(the_str)

    the_str = "Sample rate (Hz)," + str(Profile.sample_rate) + ",\n"
    the_profile_file.write(the_str)

    the_str = "Bits per samples," + str(Wav_file_infos.bits_per_sample) + ",\n"
    the_profile_file.write(the_str)

    the_str = "Analysis type," + Profile.mapping_name.upper() + ",\n"
    the_profile_file.write(the_str)

    the_str = "Filter size," + str(filters_length) + ",\n"
    the_profile_file.write(the_str)

    # append a blanck line
    the_profile_file.write(",\n")

    the_str = "Subband relative energy (dB):,\n"
    the_profile_file.write(the_str)

    the_str = "Channel name,"

    for i in range(Profile.channels_number):
        the_str = the_str + str(i+1) + ","

    the_profile_file.write(the_str+"\n")

    # print()
    # Profile.display()
    # print()

    for i in range(Profile.subbands_number):
        the_str = \
            str(Profile.subbands_frequencies_array[i]) \
            + "-" + \
            str(Profile.subbands_frequencies_array[i+1])\
            + ","

        if Profile.channels_number == 1:
            the_str = the_str + \
                str(np.round(Profile.relative_weights_array[i], 2)) \
                + ","
        else:
            # zozo = Profile.relative_weights_array
            # print()
            # print("zozo.ndim: ", zozo.ndim)
            # print("zozo.shape: ", zozo.shape)
            # print()
            for j in range(Profile.channels_number):
                ids_level = Profile.relative_weights_array[i, j]
                the_str = the_str + str(np.round(ids_level, 2)) + ","

        the_str = the_str + "\n"
        the_profile_file.write(the_str)

    # append a blanck line
    the_profile_file.write(",\n")
    the_str = "Channel energy (dB FS),"

    if  Profile.channels_number == 1:
        the_str = the_str \
            + str(np.round(Profile.mean_level_array, 2))\
            + ","
            
    else:
        for i in range(Profile.channels_number):
            the_str = the_str \
                + str(np.round(Profile.mean_level_array[i], 2)) \
                + ","

    the_profile_file.write(the_str)

    # close the mappings file
    the_profile_file.close()


# ----------
def load_csv_profile(csv_filename, the_path, mappings_def_path):
    
    the_path = pathlib.Path(the_path)

    file = open(the_path / csv_filename, newline="")
    data_list = csv.reader(file)
    data_list = list(data_list)
    file.close()

    # on ne prend pas en compte les 2 premières lignes
    wav_file_path = data_list[2][1]
    wav_filename = data_list[3][1]

    # on ne prend pas en compte la 4ème ligne
    channels_number = int(data_list[5][1])
    samples_number = int(data_list[6][1])
    sample_rate = int(data_list[7][1])
    bits_per_sample = int(data_list[8][1])

    mapping_name = data_list[9][1].lower()
    
    # mapping_Leipp_44100.csv
    cvs_mapping_filename = "mapping_" + mapping_name + "_"\
        + str(sample_rate) + ".csv"
    
    current_mapping = \
        mpgTls.load_mapping_file(cvs_mapping_filename, mappings_def_path)

    filters_length = int(data_list[10][1])

    # on ne prend pas en compte les 3 lignes suivantes
    # lecture itérative des subbands_number lignes suivantes avec traitement
    # différent suivant que l'on a un portrait mono ou non

    # l'utilisation de np.zeros conduit à une encapsulation avec
    # les délimiteurs array([]) donc il faut avoir deux indices de tableaux
    # pour accéder au contenu d'une case du tableau, un indice pour accéder
    # à une ligne par contre, on peut additionner/soustraire ces tableaux
    # avec +/- notamment !
    
#    mean_level_array = np.zeros((1, channels_number))
    # relative_weights_array = np.zeros((channels_number, 
    #                                    current_mapping.subbands_number))

    subbands_number = current_mapping.subbands_number
    
    if channels_number == 1:
        relative_weights_array = np.zeros(subbands_number)
    else:
        mean_level_array = np.zeros(2)
        relative_weights_array = np.zeros((channels_number, subbands_number))        
    
    for subband_index in range(subbands_number):
        the_index = 14 + subband_index
        
        if channels_number == 1:
            # relative_weights_array[0][subband_index] = \
            #     float(data_list[the_index][1])

            relative_weights_array[subband_index] = \
                float(data_list[the_index][1])
        else:
            # for channel_index in range(channels_number):
            #     relative_weights_array[channel_index][subband_index] = \
            #         float(data_list[the_index][channel_index+1])

            relative_weights_array[0, subband_index] = \
                    float(data_list[the_index][1])
                    
            relative_weights_array[1, subband_index] = \
                    float(data_list[the_index][2])

    # on ne prend pas en compte la ligne suivante
    # dernière ligne : mean_level_array
    the_index = 14 + current_mapping.subbands_number + 1
    
    if channels_number == 1:
#        mean_level_array[0][0] = float(data_list[the_index][1])
        mean_level_array = float(data_list[the_index][1])

    else:
        # for channel_index in range(channels_number):
        #     mean_level_array[0][channel_index] = \
        #         float(data_list[the_index][channel_index+1])

        mean_level_array[0] =  float(data_list[the_index][1])

        mean_level_array[1] = float(data_list[the_index][2])

    The_wav_infos = WavInformations(wav_filename, wav_file_path, 
                                    samples_number, channels_number, 
                                    sample_rate, bits_per_sample)

    profile_name = wav_filename[:-4]

    The_profile = prflTls.IDS_Profile(current_mapping, profile_name, 
                                      channels_number, mean_level_array, 
                                      relative_weights_array, samples_number)

    return [profile_name, current_mapping, The_profile, The_wav_infos, 
            filters_length]


# ----------
def fast_load_csv_profile(csv_filename, the_path, mappings_def_path):
    
    the_path = pathlib.Path(the_path)
    file = open(the_path / csv_filename, newline="")
    data_list = csv.reader(file)
    data_list = list(data_list)
    file.close()

    # do not take into account lines 0 to 2
    profile_name = data_list[3][1]
    profile_name = profile_name[:-4]

    # do not take into account line 4

    channels_number = int(data_list[5][1])

    # do not take into account line 6

    sample_rate = int(data_list[7][1])

    # do not take into account line 8

    # get the mapping name and get the related Mapping
    mapping_name = data_list[9][1].lower()
    mapping_name = mapping_name.capitalize()

    # mapping_Leipp_44100.csv
    cvs_mapping_filename = "mapping_" + mapping_name + "_"\
        + str(sample_rate) + ".csv"
    
    current_mapping = \
        mpgTls.load_mapping_file(cvs_mapping_filename, mappings_def_path)

    # do not take into account line 10 to 13

    # get the subbands relative weights
    subbands_number = current_mapping.subbands_number
    
    if channels_number == 1:
        relative_weights_array = np.zeros(subbands_number)
    else:
        mean_level_array = np.zeros(2)
        relative_weights_array = np.zeros((channels_number, subbands_number))        
    
    # if channels_number == 2:
    #     mean_level_array = np.zeros((1, channels_number))
        
    #     relative_weights_array = \
    #         np.zeros((channels_number, current_mapping.subbands_number))
    # else:
    #     relative_weights_array = \
    #         np.zeros((1, current_mapping.subbands_number))

        # relative_weights_array = relative_weights_array.flatten()

    for subband_index in range(current_mapping.subbands_number):
        the_index = 14 + subband_index
        
        # if (channels_number == 1):
        #     relative_weights_array[subband_index] = float(data_list[the_index][1])
        # else:
        #     relative_weights_array[0][subband_index] = \
        #         float(data_list[the_index][1])
                
        #     relative_weights_array[1][subband_index] =  \
        #         float(data_list[the_index][2])

        if channels_number == 1:
            relative_weights_array[subband_index] = \
                float(data_list[the_index][1])
        else:
            relative_weights_array[0, subband_index] = \
                    float(data_list[the_index][1])
                    
            relative_weights_array[1, subband_index] = \
                    float(data_list[the_index][2])

    # do not take into account next line

    # last line: mean_level_array
    the_index = 14 + current_mapping.subbands_number + 1
    
    # if (channels_number == 1):
    #     mean_level_array = float(data_list[the_index][1])
        
    # else:
    #     for channel_index in range(channels_number):
    #         mean_level_array[0][channel_index] = \
    #             float(data_list[the_index][channel_index+1])
                
    if channels_number == 1:
        mean_level_array = float(data_list[the_index][1])

    else:
        mean_level_array[0] =  float(data_list[the_index][1])

        mean_level_array[1] = float(data_list[the_index][2])



    return [profile_name, current_mapping, channels_number,
            mean_level_array, relative_weights_array]


# ----------
def get_minMax_weights(csv_filename, the_path, mappings_def_path):
    
    the_path = pathlib.Path(the_path)
    
    file = open(the_path / csv_filename, newline="")
    data_list = csv.reader(file)
    data_list = list(data_list)
    file.close()

    channels_number = int(data_list[5][1])
    sample_rate = int(data_list[7][1])

    mapping_name = data_list[9][1].lower()
    mapping_name = mapping_name.capitalize()

    # mapping_Leipp_44100.csv
    cvs_mapping_filename = "mapping_" + mapping_name + "_"\
        + str(sample_rate) + ".csv"
    
    current_mapping = \
        mpgTls.load_mapping_file(cvs_mapping_filename, mappings_def_path)

    # get the subbands relative weights
    # relative_weights_array = np.zeros((channels_number,
    #                                  current_mapping.subbands_number))

    subbands_number = current_mapping.subbands_number

    if channels_number == 1:
        relative_weights_array = np.zeros(subbands_number)
    else:
        relative_weights_array = np.zeros((channels_number, subbands_number))        
 
    for subband_index in range(current_mapping.subbands_number):
        the_index = 14 + subband_index

        # if (channels_number == 1):
        #     relative_weights_array[0][subband_index] = \
        #         float(data_list[the_index][1])
        # else:
        #     for channel_index in range(channels_number):
        #         relative_weights_array[channel_index][subband_index] =\
        #             float(data_list[the_index][channel_index+1])

        if channels_number == 1:
            relative_weights_array[subband_index] = \
                float(data_list[the_index][1])
        else:
            relative_weights_array[0, subband_index] = \
                    float(data_list[the_index][1])
                    
            relative_weights_array[1, subband_index] = \
                    float(data_list[the_index][2])

    min_val = relative_weights_array.min()
    max_val = relative_weights_array.max()

    return min_val, max_val


# ----------
def create_renamed_csv_profile(beg_filename, beg_path, end_filename, 
                               end_path):

    fldrTls.duplicate_file(beg_path, beg_filename, end_path, end_filename)

