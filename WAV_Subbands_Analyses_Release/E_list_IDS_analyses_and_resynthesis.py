#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       E_list_IDS_analyses_and_resynthesis.py

creation date:      18/08/2024, 13h25
modification date:  07/10/2024, 21h31

@author: Millot Laurent



For each WAV file existing within the list, the tool:
- performs the IDS analysis with generation of subbands WAV files
- plots the IDS profile
- copies the orginal WAV file within 
    data_resynthesis/Data_{mapping_name}/wav_origfiles
- saves the WAV subbands files within 
    data_resynthesis/Data_{mapping_name}/wav_sbfiles
- saves the plot of the IDS profile 
    within data_resynthesis/Data_{mapping_name}/ids_figures
- saves the IDS profile within 
    data_resynthesis/Data_{mapping_name}/ids_profiles_csv

This folders' structure is used by the real time resynthetizer coded in Max
related to the mappling frequency 
(for example, ids_Leipp_resynthesis.maxpat for the Leipp frequency mapping)
"""



import pathlib

import Sub_ToBo.tools_ids.manage_ids_analyses_resynthesis as anlTls
import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls

main_path = pathlib.Path.cwd()

# mappings definition and related filters sets
tools_data_path = main_path / "data_subbands_tools"
mappings_def_path = tools_data_path / "mappings_definitions"
subbands_filters_path = tools_data_path / "subbands_filters"

# analyses results (csv files)
data_path = main_path / "data_resynthesis"



# ----------
def process_list_IDS_analyses(corpus_path, wav_files_list, wav_alias_list, 
                              mapping_name):
      
    subfolder_name = "Data_" + mapping_name
    results_main_path = data_path / subfolder_name
    fldrTls.create_new_subfolder(results_main_path)

    fig_path = results_main_path / "ids_figures"
    fldrTls.create_new_subfolder(fig_path)

    csv_path = results_main_path / "ids_profiles_csv"
    fldrTls.create_new_subfolder(csv_path)

    wav_orig_path = results_main_path / "wav_origfiles"
    fldrTls.create_new_subfolder(wav_orig_path)

    wav_sb_path = results_main_path / "wav_sbfiles"
    fldrTls.create_new_subfolder(wav_sb_path)

    anlTls.analyses_the_corpus(mapping_name, wav_files_list, wav_alias_list, 
                                corpus_path, mappings_def_path, 
                                subbands_filters_path, csv_path, fig_path, 
                                wav_orig_path, wav_sb_path)
    
    print()
    print()
    print("All needed data have been created",
          f" within data_resynthesis/{subfolder_name}")
    print()
    print(f"You just need to copy them into the {subfolder_name} subfolder"\
              + " used by the Max resynthetizer: ")
    print("ids_" + mapping_name + "_resynthesis.maxpat")
          


# ----------
# IDS analyses of a given list of wav files within the same folder
# chosen frequency mapping name
mapping_name = "Audio"

# path to the subfolder where the selected WAV files can be found
corpus_path = main_path.parent / "sounds" / "IDS_test_sounds_2"

# list of the names of the chosen WAV files
wav_files_list = ["Autopscience_m441.wav", "classe_VS_terrain_s441.wav", 
                  "strange_s441.wav"]

# list of the related alias names
wav_alias_list = ["Autopscience.wav", "classe_VS_terrain.wav", "strange.wav"]

# management of the whole preparation of IDS resynthesis
process_list_IDS_analyses(corpus_path, wav_files_list, wav_alias_list, 
                          mapping_name)
