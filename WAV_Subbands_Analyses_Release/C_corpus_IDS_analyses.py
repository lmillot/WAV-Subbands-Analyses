#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       C_corpus_IDS_analyses.py

creation date:      15/08/2024, 15h01
modification date:  07/10/2024, 22h21

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
def process_IDS_analyses_for_a_folder(corpus_path, mapping_name, folder_name):
    
    print()
    print("-" * 20)
    print("IDS analyses")
    print(f"folder to be analyzed: {folder_name}")
    print(f"using frequency mapping:  {mapping_name}")
    print()
    
    files_names_list = fldrTls.list_given_extension_files(corpus_path, ".wav")

    alias_names_list = []

    for the_file in files_names_list:
        the_file = the_file[:-9] + ".wav"
        alias_names_list.append(the_file)

    main_profiles_path = csv_path / mapping_name
    fldrTls.create_new_subfolder(main_profiles_path)
    
    ids_profiles_path  = main_profiles_path / folder_name
    fldrTls.create_new_subfolder(ids_profiles_path)
    
    anlTls.analyses_the_corpus(mapping_name, files_names_list, alias_names_list, corpus_path, 
                               mappings_def_path, subbands_filters_path, 
                               ids_profiles_path)


# ----------
# IDS analyses for a whole folder of WAV files
# chosen frequency mapping
mapping_name = "Audio"

# pre-defined subfolders names where there are WAV files
folder_names_list = ["IDS_test_sounds", "IDS_test_sounds_2"]
folder_name_index = 1

# -----
folder_name = folder_names_list[folder_name_index]

# path to the subfolders defined in folder_names_list
# main_path.parent: parent folder of WAV_Subbands_Analyses_Release
corpus_path = main_path.parent / "sounds" / folder_name

# launches the analyses
process_IDS_analyses_for_a_folder(corpus_path, mapping_name, folder_name)
