#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name :       D_Plot_one_IDS_profile.py

creation date:      29/09/2024, 00h35
modification date:  07/10/2024, 21h20

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
def process_plots(files_list, mapping_name, fig_subfolder_name, I_scale=True):

    the_fig_path = fig_path / mapping_name / fig_subfolder_name

    csv_files_path = csv_path / mapping_name / subfolder_name

    fldrdTls.create_new_subfolder(the_fig_path)
    
    if I_scale:      
        pltTls.manage_scaled_ids_plotting(files_list, csv_files_path, 
                                          the_fig_path, mappings_def_path)

    else:
        pltTls.manage_unscaled_ids_plotting(files_list, csv_files_path, 
                                            the_fig_path, mappings_def_path)
    
    print()
    print("-" * 15)
    print(f"studied IDS profile: {files_list[0]}")
    print()
    print("plot of the IDS profile can be found at the following location:")
    print(the_fig_path)
    print()


# ----------
# chosen frequency mapping
mapping_name = "Leipp"

# path to the subfolder where the chosen IDS profile can be found
subfolder_name = "IDS_test_sounds_2"

# list of some IDS profiles which can be found in the chosen subfolder
profiles_list = ["Autopscience_44263L.ids.csv", "english_44263L.ids.csv",
                 "classe_VS_terrain_44263L.ids.csv", "french_44263L.ids.csv",
                 "strange_44263L.ids.csv"]

# index of the chosen IDS profile to be plotted
profile_index = 2

# path to the location where the IDS profile plot will be saved
fig_subfolder_name = "single_plot_test"

# -----
# plots of one IDS profile
# no scaling can be performed with only one IDS profile to be plotted
I_scale = False

# get the profile name
profile_name = profiles_list[profile_index]

# manage the creation and saving of the plotted IDS profile
process_plots([profile_name], mapping_name, fig_subfolder_name, I_scale)
