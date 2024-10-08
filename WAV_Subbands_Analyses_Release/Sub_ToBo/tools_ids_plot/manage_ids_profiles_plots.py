#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script:             manage_ids_profiles_plots.py

creation date:      16/08/2024, 20h05
modification date:  07/10/2024, 14h41

@author: Millot Laurent
"""


import numpy as np

import Sub_ToBo.tools_ids.csv_ids_profiles_tools as csvTls
import Sub_ToBo.tools_ids_plot.tools_ids_profiles_plot as pltTls
import Sub_ToBo.tools_ids_plot.tools_ids_ylimits_determination as lmtTls


# ----------
def manage_scaled_ids_plotting(files_list, the_csv_path, the_fig_path, 
                               mappings_def_path):
    
    # 1. determine minimum and maximum ids weights values for the corpus
    files_number = len(files_list)

    for file_index in range(files_number):
        csv_filename = files_list[file_index]

        # 1. load the profile
        if file_index == 0:
            min_ids_value, max_ids_value = \
                csvTls.get_minMax_weights(csv_filename, the_csv_path, 
                                          mappings_def_path)
        else:
            the_min_ids_value, the_max_ids_value = \
                csvTls.get_minMax_weights(csv_filename, the_csv_path, 
                                          mappings_def_path)

            min_ids_value = np.array([min_ids_value, the_min_ids_value]).min()
            max_ids_value = np.array([max_ids_value, the_max_ids_value]).max()

    # 2. calculate adpated y limits for the corpus
    min_ids_value, max_ids_value = \
        lmtTls.calculate_plot_ylimits(min_ids_value, max_ids_value)

    # 3. create and save plots for each profile of the corpus
    for file_index in range(files_number):
        csv_filename = files_list[file_index]

        # 3.1 load the profile
        profile_info = csvTls.fast_load_csv_profile(csv_filename, 
                                                    the_csv_path,
                                                    mappings_def_path)

        profile_name = profile_info[0]
        current_mapping = profile_info[1]
        channels_number = profile_info[2]
        mean_level_array = profile_info[3]
        ids_array = profile_info[4]

        if channels_number == 2:
            mean_level_array = mean_level_array.flatten()

        str_length = len(".ids.csv")
        profile_name = csv_filename[:-str_length]

        # 3.2 create and save the plot
        fig_name = profile_name + "_" + current_mapping.mapping_key

        freq_array = np.array(current_mapping.subbands_frequencies_array)

        pltTls.plot_IDS_profile(ids_array, mean_level_array, freq_array,
                                channels_number, min_ids_value,
                                max_ids_value, fig_name, the_fig_path, "")


# ----------
def manage_unscaled_ids_plotting(files_list, the_csv_path, the_fig_path, 
                                 mappings_def_path):
    
    # 1. determine minimum and maximum ids weights values for the corpus
    files_number = len(files_list)
    
    for file_index in range(files_number):
        csv_filename = files_list[file_index]

        # 1. load the profile
        profile_info = csvTls.fast_load_csv_profile(csv_filename, 
                                                    the_csv_path,
                                                    mappings_def_path)

        profile_name = profile_info[0]
        current_mapping = profile_info[1]
        channels_number = profile_info[2]
        mean_level_array = profile_info[3]
        
        if channels_number == 2:
            mean_level_array = mean_level_array.flatten()

        ids_array = profile_info[4]

        # 2. create and save the plot
        str_length = len(".ids.csv")
        profile_name = csv_filename[:-str_length]

        # 3.2 create and save the plot
        fig_name = profile_name + "_" + current_mapping.mapping_key

        freq_array = np.array(current_mapping.subbands_frequencies_array)

        min_ids_value = ids_array.min()
        max_ids_value = ids_array.max()

        # mmodification ici, 2024/09/29 @ 01h14
        min_ids_value = np.floor(min_ids_value)
        max_ids_value = np.ceil(max_ids_value)

        pltTls.plot_IDS_profile(ids_array, mean_level_array, freq_array,
                                channels_number, min_ids_value,
                                max_ids_value, fig_name, the_fig_path, "")
