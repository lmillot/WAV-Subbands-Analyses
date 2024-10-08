#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       D_Plot_corpus_IDS_profiles.py

creation date:      29/09/2024, 00h44
modification date:  07/10/2024, 21h17

@author: Millot Laurent
"""


import pathlib

import Sub_ToBo.tools_files_folders.tools_files_folders as fldrdTls
import Sub_ToBo.tools_ids_plot.manage_ids_profiles_plots as pltTls




main_path = pathlib.Path.cwd()

tools_data_path = main_path / "data_subbands_tools"
mappings_def_path = tools_data_path / "mappings_definitions"

analyses_data_path = main_path / "data_analyses_results"
csv_path = analyses_data_path / "ids_profiles_csv"
fig_path = analyses_data_path / "ids_profiles_figures"


# ----------
def process_plots(mapping_name, subfolder_name, I_scale=True):
    
    # path to the IDS profiles to be plotted 
    # (in subfolder named subsubfolder_name)
    main_csv_files_path = csv_path / mapping_name
    csv_files_path = main_csv_files_path / subfolder_name

    # list all the IDS profiles existing in the subfolder
    files_list = fldrdTls.list_given_extension_files(csv_files_path, ".csv")
    
    
    # path to the main figures folder for the chosen frequency mapping
    main_fig_path = fig_path / mapping_name

    if I_scale:      
        # add a postfix to the subfolder name where the IDS profiles plots 
        # will be saved
        fig_subfolder_name = subfolder_name + "_scaled"

        # complete the definition of the subfolder where the IDS profiles plots
        # will be saved
        the_fig_path = main_fig_path / fig_subfolder_name
        fldrdTls.create_new_subfolder(the_fig_path)

        pltTls.manage_scaled_ids_plotting(files_list, csv_files_path, 
                                          the_fig_path, mappings_def_path)

    else:
        # add a postfix to the subfolder name where the IDS profiles plots 
        # will be saved
        fig_subfolder_name = subfolder_name + "_unscaled"

        # complete the definition of the subfolder where the IDS profiles plots
        # will be saved
        the_fig_path = main_fig_path / fig_subfolder_name
        fldrdTls.create_new_subfolder(the_fig_path)       
        
        pltTls.manage_unscaled_ids_plotting(files_list, csv_files_path, 
                                            the_fig_path, mappings_def_path)

    print()
    print("-" * 15)
    the_subfolder = str(csv_files_path)
    the_subfolder = the_subfolder.split("/")[-1]
    print(f"subfolder: {the_subfolder}")
    print("figures created and saved at the following location:")
    print(the_fig_path)
    print()
    print(f"scaling: {I_scale}")
    print()
    print()


# ----------
# name of the chosen frequency mapping
mapping_name = "Audio"

# name of the subfolder wher the IDS profiles to plot are located
subfolder_name = "IDS_test_sounds_2"


# -----------------------------------------
# --- first example of use of this tool ---
# -----------------------------------------
# plots of the IDS profiles with the same scale to perform comparisons of 
# these IDS profiles
# scale's boolean must be equal to True
I_scale = True

# manage the creation of all plots and their saving
process_plots(mapping_name, subfolder_name, I_scale)

        
# ------------------------------------------
# --- second example of use of this tool ---
# ------------------------------------------
# plots of the IDS profiles with a different and adapted scale 
# for each IDS profile
# scale's boolean must be equal to False
I_scale = False

# manage the creation of all plots and their saving
process_plots(mapping_name, subfolder_name, I_scale)
