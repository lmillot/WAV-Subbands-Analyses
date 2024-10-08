# -*- coding: utf-8 -*-
"""
application:          ids_profiles_tools.py

creation date:        12/06/2015, 10h01
modification date:    15/04/2024, 19h21

@author: Laurent Millot
"""


import numpy as np


# ----------
class IDS_Profile(object):
    def __init__(self, current_mapping, profile_name, channels_number,
                 mean_level_array, relative_weights_array, samples_number=0):

        self.sample_rate = current_mapping.sample_rate
        self.mapping_name = current_mapping.mapping_name
        self.mapping_key = current_mapping.mapping_key
        self.subbands_number = current_mapping.subbands_number
        self.subbands_frequencies_array = \
            current_mapping.subbands_frequencies_array
            
        self.profile_name = profile_name
        self.channels_number = channels_number

        if channels_number == 1:
            self.mean_level_array = 0
            self.relative_weights_array = np.zeros(self.subbands_number)

            self.mean_level_array = mean_level_array
            self.relative_weights_array = relative_weights_array
            
        else:
            self.mean_level_array = np.zeros(channels_number)
            self.relative_weights_array = np.zeros((channels_number,
                                                    self.subbands_number))

            self.mean_level_array = mean_level_array
            self.relative_weights_array = relative_weights_array

        self.samples_number = samples_number

    def display(self):
        print()
        print("--------------------")
        print("IDS Profile: ")
        print("mapping name: ", self.mapping_name)
        print("mapping key: ", self.mapping_key)
        print("subbands number: ", self.subbands_number)
        print("subband frequencies: ")
        print(self.subbands_frequencies_array)
        print()
        
        print("profile name: ", self.profile_name)
        print("sample rate: ", self.sample_rate)
        print("channels number: ", self.channels_number)
        print("samples number: ", self.samples_number)
        
        if self.channels_number == 1:
            print("mean level:", self.mean_level_array)
            print("relative_weights_array: ")
            print(self.relative_weights_array)
            
        else:
            print("mean levels:", self.mean_level_array)
            print("relative_weights_array: ")
            print(self.relative_weights_array[0, :])
            print(self.relative_weights_array[1, :])

        print()


# ----------
def add_ids_profiles(ids_profile_1, ids_profile_2, newprofile_name,
                     current_mapping):

    channels_number = ids_profile_1.channels_number

    mean_level_array = ids_profile_1.mean_level_array \
        + ids_profile_2.mean_level_array

    relative_weights_array = ids_profile_1.relative_weights_array \
        + ids_profile_2.relative_weights_array

    samples_number = 0    # ids_profile_1.samples_number

    New_profile = IDS_Profile(current_mapping, newprofile_name,
                             channels_number, mean_level_array,
                             relative_weights_array, samples_number)

    return New_profile


# ----------
def create_null_ids_profile(current_mapping, newprofile_name,
                            channels_number=1, samples_number=0):

    mean_level_array = [0] * channels_number

    if (channels_number == 1):
        relative_weights_array = [0] * current_mapping.subbands_number

    else:   # création d'un tableau de zéros
        # de taille channels_number x subbands_number
        relative_weights_array = [0] * current_mapping.subbands_number
        
        for i in range(channels_number):
            relative_weights_array[i] = [0] * current_mapping.subbands_number

    New_profile = IDS_Profile(current_mapping, newprofile_name,
                             channels_number, mean_level_array,
                             relative_weights_array, samples_number)

    return New_profile
