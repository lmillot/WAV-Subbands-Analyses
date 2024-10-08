#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       Delete_one_mapping.py

creation date:      15/08/2024, 14h58
modification date:  07/10/2024, 18h28

@author: Millot Laurent 


CAUTION: Deleting a frequency mapping has side effects!

Indeed, deleting a frequency mapping deletes:
- related main subfolder (and subfolders within it) within 
    data_analyses_results 
- related main subfolder (and subfolders within it) within 
    data_resynthesis
- frequency maping definition within 
    data_subbands_tools/mappings_definitions
- subbands filters set within 
    data_subbands_tools/subbands_filters
"""


import Sub_ToBo.tools_ids_configuration.tools_mapping_creation as mpgTls


# ----------
def process_mapping_destruction(mapping_name, sample_rate, ripple_dB=80.0, 
                                width_Hz=5.0):
    
    mpgTls.remove_one_mapping(mapping_name, sample_rate, ripple_dB, width_Hz)

    print("2. After mapping elimination") 
    mpgTls.list_installed_mappings()


# ----------
print("1. Before mapping elimination")
mpgTls.list_installed_mappings()

# minimum attenuation in stop-band (in dB)
ripple_dB = 80.0

# width of the transition subband (in Hz)
width_Hz = 5.0

# mapping parameters
sample_rate = 44100
mapping_name = "Test"

process_mapping_destruction(mapping_name, sample_rate, ripple_dB, width_Hz)
