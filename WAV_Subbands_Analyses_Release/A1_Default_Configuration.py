#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       A1_Default_Configuration.py

creation date:      15/08/2024, 14h49
modification date:  07/10/2024, 14h33

@author: Millot Laurent



----------
What this regular version does:

- installation of pre-defined mapping(s) (Audio, Leipp, Octaves or Sono)
- configuration of the tools (creation of all needed folders and relative
  subfolders, of the mapping's files and of sets of the subbands filters)


----------
Pre-defined frequency mappings

mapping name / key letter / subbands number / subbands limits frequencies

Audio / A / 13 / 0, 30, 60, 80, 100, 120, 250, 500, 1000, 2000, 4000, 8000, 
                16000

Leipp / L / 10 / 0, 50, 200, 400, 800, 1200, 1800, 3000, 6000, 15000

Octaves / O / 11 / 0, 22, 44, 88, 176, 353, 707, 1414, 2828, 5656, 11313

Sono / S / 14 / 0, 25, 33, 55, 80, 120, 250, 500, 1000, 2000, 4500, 7000, 
                10000, 15000

"""



import Sub_ToBo.tools_ids_configuration.tools_mapping_creation as mpgTls



# ----- configuration's parameters
# minimum attenuation in stop-band (in dB)
ripple_dB = 80.0

# width of the transition subband (in Hz)
width_Hz = 5.0

# choose the names of the frequency mappings to be created
# (at least one mapping)
# mapping_names_list = ["Audio", "Leipp", "Octaves", "Sono"]
mapping_names_list = ["Leipp"]

# choose the sample rates of the wav files you want to analyse 
# (at least one sample rate)
# sample_rates_list = [44100, 48000, 96000]
sample_rates_list = [44100]

# launch the installation process and the creation of the chosen 
# frequency mapping(s)
mpgTls.process_mappings_creation(mapping_names_list, sample_rates_list,
                                 ripple_dB, width_Hz)

mpgTls.list_installed_mappings()
