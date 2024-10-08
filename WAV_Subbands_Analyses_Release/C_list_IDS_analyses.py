#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       C_list_IDS_analyses.py

creation date:      15/08/2024, 15h01
modification date:  07/10/2024, 21h16

@author: Millot Laurent
"""


import pathlib

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls
import Sub_ToBo.tools_ids.manage_ids_analyses as anlTls



main_path = pathlib.Path.cwd()

# mappings definition and related filters sets
tools_data_path = main_path / "data_subbands_tools"
mappings_def_path = tools_data_path / "mappings_definitions"
subbands_filters_path = tools_data_path / "subbands_filters"

# analyses results (csv files)
analyses_data_path = main_path / "data_analyses_results"
csv_path = analyses_data_path / "ids_profiles_csv"
fig_path = analyses_data_path / "ids_profiles_figures"



# ----------
def process_IDS_analyses_for_a_files_list(corpus_path, wav_files_list, 
                                          wav_alias_list, mapping_name):
    
        
    print()
    print("-" * 20)
    print("IDS analyses of a selection of WAV files")
    print(f"using frequency mapping:  {mapping_name}")
    print()
    
    ids_profiles_path = csv_path / mapping_name
    fldrTls.create_new_subfolder(ids_profiles_path)
    
    anlTls.analyses_the_corpus(mapping_name, wav_files_list, wav_alias_list, 
                               corpus_path, mappings_def_path, 
                               subbands_filters_path, ids_profiles_path)


# name of the frequency mapping to be used: 
mapping_name = "Audio"

# definition of the path where the WAV to be analyzed are located
corpus_path = main_path.parent / "sounds" / "IDS_test_sounds_2"

# list of the names of the WAV files to analyze
wav_files_list = ["Autopscience_m441.wav", "english_m441.wav", 
                  "french_m441.wav", "strange_s441.wav"]

# list of related alias (shorter names) for the WAV files to analyze
wav_alias_list = ["Autopscience.wav", "english.wav", "french_m441.wav",
                  "strange"]

# manage the IDS analyses of all the selected WAV files
process_IDS_analyses_for_a_files_list(corpus_path, wav_files_list, 
                                      wav_alias_list, mapping_name)
