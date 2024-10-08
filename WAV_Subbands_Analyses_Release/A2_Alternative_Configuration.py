#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       A2_Alternative_Configuration.py

creation date:      04/10/2024, 10h50
modification date:  07/10/2024, 14h33

@author: Millot Laurent


----------
What this alternative version does:

- no installation of one of the pre-defined mappings (Audio, Leipp, Octaves 
  or Sono)
- definition and creation of a frequency mapping defined by the user
- configuration of the tools (creation of all needed folders and relative
  subfolders)

"""



import Sub_ToBo.tools_ids_configuration.tools_mapping_creation as mpgTls



# ----------
def process_configuration(sample_rate, mapping_name, mapping_key, 
                          subbands_number, subbands_frequencies_limits_array, 
                          ripple_dB=80.0, width_Hz=5.0):
    
    new_mapping = mpgTls.Mapping(sample_rate, mapping_name, mapping_key, 
                                 subbands_number,  
                                 subbands_frequencies_limits_array)

    mpgTls.create_new_mapping(new_mapping.mapping_name, new_mapping, 
                          sample_rate, ripple_dB, width_Hz)

    mpgTls.list_installed_mappings()

   

"""
Examples of pre-defined frequency mappings

convention:
mapping name / key letter / subbands number / subbands limits frequencies

examples:    
Audio / A / 13 / 0, 30, 60, 80, 100, 120, 250, 500, 1000, 2000, 4000, 8000, 
16000
    
Leipp / L / 10 / 0, 50, 200, 400, 800, 1200, 1800, 3000, 6000, 15000
    
Octaves / O / 11 / 0, 22, 44, 88, 176, 353, 707, 1414, 2828, 5656, 11313
    
Sono / S / 14 / 0, 25, 33, 55, 80, 120, 250, 500, 1000, 2000, 4500, 7000, 
10000, 15000
"""

# ----------
# ----- mapping's parameters
# minimum attenuation in stop-band (in dB)
ripple_dB = 80.0

# width of the transition subband (in Hz)
width_Hz = 5.0

# sample rate (in Hz)
sample_rate = 44100

# mapping name
mapping_name = "Test"

# capital letter to identify the mapping
mapping_key = "T"

# subbands frequencies without Nyquist frequency (sample_rate // 2) 
# which would be added automatically during the installation process
subbands_frequencies_limits_array = [0, 1000, 2000, 4000, 8000]

# number fo the subbands constituting the frequency mapping
subbands_number = len(subbands_frequencies_limits_array)

# launch the installation process and the creation of the user-defined 
# frequency mapping
process_configuration(sample_rate, mapping_name, mapping_key, subbands_number,
                      subbands_frequencies_limits_array, ripple_dB, width_Hz)
