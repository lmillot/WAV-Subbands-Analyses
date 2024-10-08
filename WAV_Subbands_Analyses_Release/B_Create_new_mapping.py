#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       B_Create_new_mapping.py

creation date:      15/08/2024, 14h55
modification date:  04/10/2024, 14h33

@author: Millot Laurent
"""


import Sub_ToBo.tools_ids_configuration.tools_mapping_creation as mpgTls



# ----------
def process_mapping_creation(sample_rate, mapping_name, mapping_key, 
                             subbands_number, subbands_frequencies_limits_array,
                             ripple_dB=80.0, width_Hz=5.0):
    
    new_mapping = \
        mpgTls.Mapping(sample_rate, mapping_name, mapping_key, subbands_number,
                       subbands_frequencies_limits_array)

    mpgTls.create_new_mapping(new_mapping.mapping_name, new_mapping, 
                              sample_rate, ripple_dB, width_Hz)

    print("2. After mapping creation") 
    mpgTls.list_installed_mappings()


# ----------
print("1. Before mapping creation")
mpgTls.list_installed_mappings()


# ----- mapping's parameters
# minimum attenuation in stop-band (in dB)
ripple_dB=80.0

# width of the transition subband (in Hz)
width_Hz=5.0

# sample rate (in Hz)
sample_rate = 44100

# mapping name
mapping_name = "Test"

# capital letter to identify the maaping
mapping_key = "T"

# subbands frequencies without Nyquist frequency (sample_rate // 2) which would be added
# automatically during the installation process
subbands_frequencies_limits_array = [0, 1000, 2000, 4000, 8000]

# number fo the subbands constituting the frequency mapping
subbands_number = len(subbands_frequencies_limits_array)

# ----------
# launch the creation of the user-defined frequency mapping
process_mapping_creation(sample_rate, mapping_name, mapping_key, 
                         subbands_number,  subbands_frequencies_limits_array, 
                         ripple_dB, width_Hz)
