#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       E_corpus_IDS_analyses_and_resynthesis.py

creation date:      18/08/2024, 13h25
modification date:  07/10/2024, 21h26

@author: Millot Laurent



For each WAV file existing within the subfolder, the tool:
- performs the IDS analysis with generation of subbands WAV files
- plots the IDS profile
- copies the orginal WAV file within 
    data_resynthesis/Data_{mapping_name}/wav_origfiles
- saves the WAV subbands files within 
    data_resynthesis/Data_{mapping_name}/wav_sbfiles
- saves the plot of the IDS profile within 
    data_resynthesis/Data_{mapping_name}/ids_figures
- saves the IDS profile within 
    data_resynthesis/Data_{mapping_name}/ids_profiles_csv

This folders' structure is used by the real time resysnthetizer coded in Max
related to the mappling frequency
(for example, ids_Leipp_resynthesis.maxpat for the Leipp frequency mapping)
"""



import pathlib

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrTls
import Sub_ToBo.tools_ids.manage_ids_analyses_resynthesis as anlTls



main_path = pathlib.Path.cwd()

# mappings definition and related filters sets
tools_data_path = main_path / "data_subbands_tools"
mappings_def_path = tools_data_path / "mappings_definitions"
subbands_filters_path = tools_data_path / "subbands_filters"

# analyses results (csv files)
data_path = main_path / "data_resynthesis"



# ----------
def process_IDS_analyses_for_a_folder(corpus_path, mapping_name):
    
    file_names_list = fldrTls.list_given_extension_files(corpus_path, ".wav")

    alias_names_list = []

    for the_file in file_names_list:
        the_file = the_file[:-9] + ".wav"
        alias_names_list.append(the_file)
    
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
    
    print()
    print("-" * 20)
    print("IDS Analyses")
    print(f"subfolder under analysis: {subfolder_name}")
    print(f"frequency mapping used: {mapping_name}")
    print()

    anlTls.analyses_the_corpus(mapping_name, file_names_list, 
                               alias_names_list, corpus_path, 
                               mappings_def_path, subbands_filters_path, 
                               csv_path, fig_path, wav_orig_path, wav_sb_path)

    print()
    print()
    print("All needed data have been created",
          f" within data_resynthesis/{subfolder_name}")
    print()
    print(f"You just need to copy them into the {subfolder_name} subfolder"\
              + " used by the Max resynthetizer: ")
    print("ids_" + mapping_name + "_resynthesis.maxpat")


# ----------
## IDS analyses for a whole folder of wav files
# chosen frequency mapping name
mapping_name = "Leipp"

# list of WAV files' subfolders 
folder_names_list = ["IDS_test_sounds", "IDS_test_sounds_2"]

# index of the chosen subfolder name
folder_name_index = 1

# path to the subfolder where the selected WAV files can be found
folder_name = folder_names_list[folder_name_index]
corpus_path = main_path.parent / "sounds" / folder_name

# management of the whole preparation of IDS resynthesis
process_IDS_analyses_for_a_folder(corpus_path, mapping_name)
